
from ..model import component as comp
from ..model import rdl_types as rdlt

        
class PropertyRuleBook:
    def __init__(self):
        pass
        
#===============================================================================
# Mutual Exclude property groups
grp_A = set()
grp_B = set()
grp_C = set()
grp_D = set()
grp_E = set()
grp_F = set()
grp_G = set()
grp_H = set()
grp_I = set()
grp_J = set()
grp_K = set()
grp_L = set()
grp_M = set()
grp_N = set()
grp_O = set()
grp_P = set()
grp_Q = set()
grp_R = set()
        
#===============================================================================
# Base property
#===============================================================================
class PropertyRule:
    bindable_to = []
    valid_types = []
    default = None
    dyn_assign_allowed = True
    mutex_set = None

#===============================================================================
# General Properties
#===============================================================================
class Prop_name(PropertyRule):
    bindable_to = [comp.Addrmap, comp.Field, comp.Mem, comp.Reg, comp.Regfile, comp.Signal]
    valid_types = [str]
    default = ""
    dyn_assign_allowed = True
    mutex_set = None

class Prop_desc(PropertyRule):
    bindable_to = [comp.Addrmap, comp.Field, comp.Mem, comp.Reg, comp.Regfile, comp.Signal]
    valid_types = [str]
    default = ""
    dyn_assign_allowed = True
    mutex_set = None

class Prop_ispresent(PropertyRule):
    bindable_to = [comp.Addrmap, comp.Field, comp.Mem, comp.Reg, comp.Regfile, comp.Signal]
    valid_types = [bool]
    default = True
    dyn_assign_allowed = True
    mutex_set = None

class Prop_donttest(PropertyRule):
    """
    Indicates the component is not included in structural testing.
    """
    bindable_to = [comp.Addrmap, comp.Reg, comp.Regfile, comp.Field]
    valid_types = [bool, int]
    default = False
    dyn_assign_allowed = True
    mutex_set = grp_O

class Prop_dontcompare(PropertyRule):
    """
    Indicates the components read data shall be discarded and not compared
    against expected results.
    """
    bindable_to = [comp.Addrmap, comp.Reg, comp.Regfile, comp.Field]
    valid_types = [bool, int]
    default = False
    dyn_assign_allowed = True
    mutex_set = grp_O

class Prop_errextbus(PropertyRule):
    bindable_to = [comp.Addrmap, comp.Reg, comp.Regfile]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = False
    mutex_set = None

class Prop_hdl_path(PropertyRule):
    bindable_to = [comp.Addrmap, comp.Reg, comp.Regfile]
    valid_types = [str]
    default = None
    dyn_assign_allowed = True
    mutex_set = None

class Prop_hdl_path_gate(PropertyRule):
    bindable_to = [comp.Addrmap, comp.Reg, comp.Regfile]
    valid_types = [str]
    default = None
    dyn_assign_allowed = True
    mutex_set = None

class Prop_hdl_path_gate_slice(PropertyRule):
    bindable_to = [comp.Addrmap, comp.Reg, comp.Regfile]
    valid_types = [TODO] # <-- Array of string
    default = None
    dyn_assign_allowed = True
    mutex_set = None

class Prop_hdl_path_slice(PropertyRule):
    bindable_to = [comp.Addrmap, comp.Reg, comp.Regfile]
    valid_types = [TODO] # <-- Array of string
    default = None
    dyn_assign_allowed = True
    mutex_set = None

#===============================================================================
# Signal Properties
#===============================================================================

class Prop_signalwidth(PropertyRule):
    """
    Width of the signal.
    """
    bindable_to = [comp.Signal]
    valid_types = [int]
    default = TODO
    dyn_assign_allowed = False
    mutex_set = None

class Prop_sync(PropertyRule):
    """
    Signal is synchronous to the clock of the component.
    """
    bindable_to = [comp.Signal]
    valid_types = [bool]
    default = TODO
    dyn_assign_allowed = True
    mutex_set = grp_N

class Prop_async(PropertyRule):
    """
    Signal is asynchronous to the clock of the component.
    """
    bindable_to = [comp.Signal]
    valid_types = [bool]
    default = TODO
    dyn_assign_allowed = True
    mutex_set = grp_N

class Prop_cpuif_reset(PropertyRule):
    """
    Default signal to use for resetting the software interface logic. If
    cpuif_reset is not defined, this reverts to the default reset signal. This
    parameter only controls the CPU interface of a generated slave.
    """
    bindable_to = [comp.Signal]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = True
    mutex_set = None

class Prop_field_reset(PropertyRule):
    """
    Default signal to use for resetting field implementations. If field_reset
    is not defined, this reverts to the default reset signal.
    """
    bindable_to = [comp.Signal]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = True
    mutex_set = None

class Prop_activelow(PropertyRule):
    bindable_to = [comp.Signal]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = True
    mutex_set = grp_A

class Prop_activehigh(PropertyRule):
    bindable_to = [comp.Signal]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = True
    mutex_set = grp_A

#===============================================================================
# Field Properties
#===============================================================================

#-------------------------------------------------------------------------------
# Field access Properties
#-------------------------------------------------------------------------------
class Prop_hw(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [rdlt.AccessType]
    default = rdlt.AccessType.rw
    dyn_assign_allowed = False
    mutex_set = None

class Prop_sw(PropertyRule):
    bindable_to = [comp.Field, comp.Mem]
    valid_types = [rdlt.AccessType]
    default = rdlt.AccessType.rw
    dyn_assign_allowed = True
    mutex_set = None

#-------------------------------------------------------------------------------
# Hardware Signal Properties
#-------------------------------------------------------------------------------
class Prop_next(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [comp.FieldInst]
    default = None
    dyn_assign_allowed = True
    mutex_set = None

class Prop_reset(PropertyRule):
    """
    The reset value for the field when resetsignal is asserted.
    """
    bindable_to = [comp.Field]
    valid_types = [int, comp.FieldInst]
    default = None
    dyn_assign_allowed = True
    mutex_set = None

class Prop_resetsignal(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [comp.Signal]
    default = None
    dyn_assign_allowed = True
    mutex_set = None

#-------------------------------------------------------------------------------
# Software access properties
#-------------------------------------------------------------------------------

class Prop_rclr(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = True
    mutex_set = grp_P

class Prop_rset(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = True
    mutex_set = grp_P
    
class Prop_onread(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [rdlt.OnReadType]
    default = None
    dyn_assign_allowed = True
    mutex_set = grp_P
    
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Prop_woclr(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = True
    mutex_set = grp_B

class Prop_woset(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = True
    mutex_set = grp_B

class Prop_onwrite(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [rdlt.OnWriteType]
    default = None
    dyn_assign_allowed = True
    mutex_set = grp_B

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Prop_swwe(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool, TODO]
    default = TODO
    dyn_assign_allowed = True
    mutex_set = grp_R

class Prop_swwel(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool, TODO]
    default = TODO
    dyn_assign_allowed = True
    mutex_set = grp_R

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Prop_swmod(PropertyRule):
    """
    Indicates a generated output signal shall notify hardware when this field is
    modified by software
    """
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = True
    mutex_set = None

class Prop_swacc(PropertyRule):
    """
    Indicates a generated output signal shall notify hardware when this field is
    accessed by software
    """
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = True
    mutex_set = None

class Prop_singlepulse(PropertyRule):
    """
    Field asserts for one cycle when written 1 and then clears back to 0
    on the next cycle
    If set, field shall be instantiated with a width of 1 and the reset value
    shall be specified as 0
    """
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = True
    mutex_set = None

#-------------------------------------------------------------------------------
# Hardware access properties
#-------------------------------------------------------------------------------

class Prop_we(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool, TODO]
    default = TODO
    dyn_assign_allowed = True
    mutex_set = grp_C

class Prop_wel(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool, TODO]
    default = TODO
    dyn_assign_allowed = True
    mutex_set = grp_C

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Prop_anded(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = True
    mutex_set = None

class Prop_ored(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = True
    mutex_set = None

class Prop_xored(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = TODO
    dyn_assign_allowed = True
    mutex_set = None

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Prop_fieldwidth(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [int]
    default = TODO
    dyn_assign_allowed = False
    mutex_set = None

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Prop_hwclr(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = True
    mutex_set = None

class Prop_hwset(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = True
    mutex_set = None

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Prop_hwenable(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [comp.FieldInst]
    default = None
    dyn_assign_allowed = True
    mutex_set = grp_D

class Prop_hwmask(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [comp.FieldInst]
    default = None
    dyn_assign_allowed = True
    mutex_set = grp_D


#-------------------------------------------------------------------------------
# Counter field properties
#-------------------------------------------------------------------------------

class Prop_counter(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = True
    mutex_set = grp_E

class Prop_threshold(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool, int TODO]
    default = TODO
    dyn_assign_allowed = True
    mutex_set = None

class Prop_saturate(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool, int, TODO]
    default = TODO
    dyn_assign_allowed = True
    mutex_set = None

class Prop_incrthreshold(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool, int, comp.SignalInst]
    default = False
    dyn_assign_allowed = True
    mutex_set = None

class Prop_incrsaturate(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool, int, comp.SignalInst]
    default = False
    dyn_assign_allowed = True
    mutex_set = None

class Prop_overflow(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = TODO
    dyn_assign_allowed = True
    mutex_set = None

class Prop_underflow(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = TODO
    dyn_assign_allowed = True
    mutex_set = None

class Prop_incr(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [comp.SignalInst]
    default = None
    dyn_assign_allowed = True
    mutex_set = None

class Prop_incrvalue(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [int, comp.SignalInst]
    default = None
    dyn_assign_allowed = True
    mutex_set = grp_F

class Prop_incrwidth(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [int]
    default = None
    dyn_assign_allowed = True
    mutex_set = grp_F

class Prop_decrvalue(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [int, comp.SignalInst]
    default = None
    dyn_assign_allowed = True
    mutex_set = grp_G

class Prop_decr(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [comp.SignalInst]
    default = None
    dyn_assign_allowed = True
    mutex_set = None

class Prop_decrwidth(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [int]
    default = None
    dyn_assign_allowed = True
    mutex_set = grp_G

class Prop_decrsaturate(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool, int, comp.SignalInst]
    default = False
    dyn_assign_allowed = True
    mutex_set = None

class Prop_decrthreshold(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool, int, comp.SignalInst]
    default = False
    dyn_assign_allowed = True
    mutex_set = None

#-------------------------------------------------------------------------------
# Field access interrupt properties
#-------------------------------------------------------------------------------

# TODO: Implement a storage location for interrupt modifiers somehow

class Prop_intr(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = True
    mutex_set = grp_E

class Prop_enable(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [comp.FieldInst]
    default = None
    dyn_assign_allowed = True
    mutex_set = grp_J

class Prop_mask(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [comp.FieldInst]
    default = None
    dyn_assign_allowed = True
    mutex_set = grp_J

class Prop_haltenable(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [comp.FieldInst]
    default = None
    dyn_assign_allowed = True
    mutex_set = grp_K

class Prop_haltmask(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [comp.FieldInst]
    default = None
    dyn_assign_allowed = True
    mutex_set = grp_K

class Prop_sticky(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = TODO
    dyn_assign_allowed = True
    mutex_set = grp_I

class Prop_stickybit(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = TODO
    dyn_assign_allowed = True
    mutex_set = grp_I

#-------------------------------------------------------------------------------
# Misc properties
#-------------------------------------------------------------------------------
class Prop_encode(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [rdlt.UserEnum]
    default = None
    dyn_assign_allowed = True
    mutex_set = None

class Prop_precedence(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [TODO]
    default = TODO
    dyn_assign_allowed = True
    mutex_set = None

class Prop_paritycheck(PropertyRule):
    bindable_to = [comp.Field]
    valid_types = [bool]
    default = TODO
    dyn_assign_allowed = False
    mutex_set = None

#===============================================================================
# Reg Properties
#===============================================================================

class Prop_regwidth(PropertyRule):
    bindable_to = [comp.Reg]
    valid_types = [int]
    default = TODO
    dyn_assign_allowed = False
    mutex_set = None

class Prop_accesswidth(PropertyRule):
    bindable_to = [comp.Reg]
    valid_types = [int]
    default = TODO
    dyn_assign_allowed = True
    mutex_set = None

class Prop_shared(PropertyRule):
    bindable_to = [comp.Reg]
    valid_types = [bool]
    default = TODO
    dyn_assign_allowed = False
    mutex_set = None

#===============================================================================
# Mem Properties
#===============================================================================

class Prop_mementries(PropertyRule):
    bindable_to = [comp.Mem]
    valid_types = [int]
    default = 1
    dyn_assign_allowed = False
    mutex_set = None

class Prop_memwidth(PropertyRule):
    bindable_to = [comp.Mem]
    valid_types = [int]
    default = TODO
    dyn_assign_allowed = False
    mutex_set = None

#===============================================================================
# Register file properties
#===============================================================================

class Prop_alignment(PropertyRule):
    bindable_to = [comp.Addrmap, comp.Regfile]
    valid_types = [int]
    default = None
    dyn_assign_allowed = False
    mutex_set = None

class Prop_sharedextbus(PropertyRule):
    bindable_to = [comp.Addrmap, comp.Regfile]
    valid_types = [bool]
    default = TODO
    dyn_assign_allowed = False
    mutex_set = None
#===============================================================================
# Address map properties
#===============================================================================

class Prop_bigendian(PropertyRule):
    bindable_to = [comp.Addrmap]
    valid_types = [bool]
    default = TODO
    dyn_assign_allowed = True
    mutex_set = grp_L

class Prop_littleendian(PropertyRule):
    bindable_to = [comp.Addrmap]
    valid_types = [bool]
    default = TODO
    dyn_assign_allowed = True
    mutex_set = grp_L

class Prop_addressing(PropertyRule):
    bindable_to = [comp.Addrmap]
    valid_types = [rdlt.AddressingType]
    default = rdlt.AddressingType.regalign
    dyn_assign_allowed = False
    mutex_set = None

class Prop_rsvdset(PropertyRule):
    bindable_to = [comp.Addrmap]
    valid_types = [bool]
    default = TODO
    dyn_assign_allowed = False
    mutex_set = grp_Q

class Prop_rsvdsetX(PropertyRule):
    bindable_to = [comp.Addrmap]
    valid_types = [bool]
    default = TODO
    dyn_assign_allowed = False
    mutex_set = grp_Q

class Prop_msb0(PropertyRule):
    bindable_to = [comp.Addrmap]
    valid_types = [bool]
    default = TODO
    dyn_assign_allowed = False
    mutex_set = grp_M

class Prop_lsb0(PropertyRule):
    bindable_to = [comp.Addrmap]
    valid_types = [bool]
    default = TODO
    dyn_assign_allowed = False
    mutex_set = grp_M

#-------------------------------------------------------------------------------
class Prop_bridge(PropertyRule):
    bindable_to = [comp.Addrmap]
    valid_types = [bool]
    default = False
    dyn_assign_allowed = False
    mutex_set = None
