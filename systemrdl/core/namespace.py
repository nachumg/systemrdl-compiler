from typing import TYPE_CHECKING, Dict, List, Union, Type, Tuple

from .parameter import Parameter

from .. import component as comp
from ..source_ref import SourceRefBase

if TYPE_CHECKING:
    from ..compiler import RDLEnvironment
    from .. import rdltypes
    from ..ast import ASTNode

TypeNSRef = Union[comp.Component, Type['rdltypes.UserEnum'], Type['rdltypes.UserStruct']]
TypeNSEntry = TypeNSRef
TypeNSScope = Dict[str, TypeNSEntry]

ElementNSRef = Union[comp.Component, Parameter]
ElementNSEntry = Tuple[ElementNSRef, comp.Component]
ElementNSScope = Dict[str, ElementNSEntry]

DefaultNSRef = Union['ASTNode', bool, 'rdltypes.InterruptType']
DefaultNSEntry = Tuple[SourceRefBase, DefaultNSRef]
DefaultNSScope = Dict[str, DefaultNSEntry]

class NamespaceRegistry():

    def __init__(self, env: 'RDLEnvironment'):
        self.env = env
        self.msg = env.msg

        self.type_ns_stack = [{}] # type: List[TypeNSScope]
        self.element_ns_stack = [{}] # type: List[ElementNSScope]
        self.default_property_ns_stack = [{}] # type: List[DefaultNSScope]

        # Control if Parameter objects are visible from parent scopes
        self.parent_parameters_visible = True

    def register_type(self, name: str, ref: TypeNSRef, src_ref: SourceRefBase) -> None:
        other_ref = self.type_ns_stack[-1].get(name)
        if other_ref:
            self._fatal_already_defined(name, src_ref, other_ref,
                                        "Multiple declarations of type '%s'")
        self.type_ns_stack[-1][name] = ref

    def register_element(self, name: str, ref: ElementNSRef, parent_comp_def: comp.Component, src_ref: SourceRefBase) -> None:
        other_ref, _ = self.element_ns_stack[-1].get(name, (None, None))
        if other_ref:
            self._fatal_already_defined(name, src_ref, other_ref,
                                        "Multiple declarations of instance '%s'")
        self.element_ns_stack[-1][name] = (ref, parent_comp_def)

    def register_default_property(self, name: str, ref: DefaultNSRef, src_ref: SourceRefBase, overwrite_ok: bool=False) -> None:
        if not overwrite_ok:
            other_ref, _ = self.default_property_ns_stack[-1].get(name, (None, None))
            if other_ref:
                self._fatal_already_defined(
                    name, src_ref, other_ref,
                    "Default property '%s' was already assigned in this scope")

        self.default_property_ns_stack[-1][name] = (src_ref, ref)

    def _fatal_already_defined(self, name: str, src_ref: SourceRefBase,
                               other_ref: Union[comp.Component, Parameter, SourceRefBase, TypeNSRef],
                               err_fmt: str) -> None:
        other_src_refs = None
        if (isinstance(other_ref, comp.Component) and
              (other_ref.inst_src_ref or other_ref.def_src_ref)):
            other_src_refs = [other_ref.inst_src_ref or other_ref.def_src_ref]
        elif (isinstance(other_ref, Parameter) and
              other_ref.expr and
              other_ref.expr.src_ref):
            other_src_refs = [other_ref.expr.src_ref]
        elif isinstance(other_ref, SourceRefBase):
            other_src_refs = [other_ref]

        self.msg.fatal(err_fmt % name, src_ref, other_src_refs)

    def lookup_type(self, name: str) -> TypeNSEntry:
        for scope in reversed(self.type_ns_stack):
            if name in scope:
                return scope[name]
        return None

    def lookup_element(self, name: str) -> ElementNSEntry:
        """
        Look up the element (component instance, or parameter) visible in the
        current scope.

        Returns a tuple:
            (element, parent_def)

        Where 'element' is the Component or Parameter being fetched
        and 'parent_def' is the component definition that encloses it.
        """
        for i, scope in enumerate(reversed(self.element_ns_stack)):
            if name in scope:
                el, parent_def = scope[name]
                if i == 0:
                    # Return anything from local namespace
                    return (el, parent_def)
                elif isinstance(el, comp.Signal):
                    # Signals are allowed to be found in parent namespaces
                    return (el, parent_def)
                elif self.parent_parameters_visible and isinstance(el, Parameter):
                    # Parameters are allowed to be found in parent namespaces,
                    # except in some contexts
                    return (el, parent_def)
        return (None, None)

    def get_default_properties(self, comp_type):
        # type: (Type[comp.Component]) -> DefaultNSScope
        """
        Returns a flattened dictionary of all default property assignments
        visible in the current scope that apply to the current component type.
        """
        # Flatten out all the default assignments that apply to the current scope
        # This does not include any default assignments made within the current
        # scope, so exclude those.
        props = {}
        for scope in self.default_property_ns_stack[:-1]:
            props.update(scope)

        # filter out properties that are not relevant
        prop_names = list(props.keys())
        for prop_name in prop_names:
            rule = self.env.property_rules.lookup_property(prop_name)
            if rule is None:
                self.msg.fatal(
                    "Unrecognized property '%s'" % prop_name,
                    props[prop_name][0]
                )
            if comp_type not in rule.bindable_to:
                del props[prop_name]

        return props

    def enter_scope(self) -> None:
        self.type_ns_stack.append({})
        self.element_ns_stack.append({})
        self.default_property_ns_stack.append({})

    def exit_scope(self) -> None:
        self.type_ns_stack.pop()
        self.element_ns_stack.pop()
        self.default_property_ns_stack.pop()
