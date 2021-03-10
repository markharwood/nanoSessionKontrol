#Embedded file name: /Users/versonator/Hudson/live/Projects/AppLive/Resources/MIDI Remote Scripts/MackieControl/__init__.py
from .MHControl import MHControl
import Live

def create_instance(c_instance):
    return MHControl(c_instance)

