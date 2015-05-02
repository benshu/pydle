## IRCv3.1 support.
from . import cap, sasl, ircv3_1

from .cap import CapabilityNegotiationSupport
from .sasl import SASLSupport
from .ircv3_1 import IRCv3_1Support


## IRCv3.2 support.
from . import monitor, tags, ircv3_2

from .monitor import MonitoringSupport
from .tags import TaggedMessageSupport
from .ircv3_2 import IRCv3_2Support


class IRCv3Support(IRCv3_2Support, IRCv3_1Support):
    pass
