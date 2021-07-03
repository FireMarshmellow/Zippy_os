from approxeng.input import CentredAxis, TriggerAxis, Button, Controller, BinaryAxis
from approxeng.input.selectbinder import ControllerResource
from approxeng.input.controllers import ControllerRequirement, print_devices
from time import sleep



class WirelessXBoxOnePad(Controller):
    """
    Wireless XBox One controller, tested with the older controller that do not use bluetooth and are supplied with the
    XBox One 2014 through USB wire connection.
    """

    def __init__(self, dead_zone=0.1, hot_zone=0.05):
        """
        Create a new xbox one controller instance
        :param float dead_zone:
            Used to set the dead zone for each :class:`approxeng.input.CentredAxis` and
            :class:`approxeng.input.TriggerAxis` in the controller.
        :param float hot_zone:
            Used to set the hot zone for each :class:`approxeng.input.CentredAxis` and
            :class:`approxeng.input.TriggerAxis` in the controller.
        """
        super(WirelessXBoxOnePad, self).__init__(
            controls=[
                Button("BTN_NORTH", 307, sname='square'),
                Button("BTN_WEST", 308, sname='triangle'),
                Button("BTN_B", 305, sname='circle'),
                Button("BTN_A", 304, sname='cross'),
                Button("BTN_THUMBR", 318, sname='rs'),
                Button("BTN_THUMBL", 317, sname='ls'),
                Button("BTN_SELECT", 314, sname='select'),
                Button("BTN_START", 315, sname='start'),
                Button("BTN_MODE", 316, sname='home'),
                Button("BTN_TL", 310, sname='l1'),
                Button("BTN_TR", 311, sname='r1'),
                CentredAxis("ABS_X", -32768, 32767, 0, sname='lx'),
                CentredAxis("ABS_Y", -32768, 32767, 1, invert=True, sname='ly'),
                CentredAxis("ABS_RX", -32768, 32767, 3, sname='rx'),
                CentredAxis("ABS_RY", -32768, 32767, 4, invert=True, sname='ry'),
                TriggerAxis("ABS_Z", 0, 1023, 2, sname='lt', button_sname='l2', button_trigger_value=0.2),
                TriggerAxis("ABS_RZ", 0, 1023, 5, sname='rt', button_sname='r2', button_trigger_value=0.2),
                BinaryAxis("ABS_HAT0X", 16, b1name='dleft', b2name='dright'),
                BinaryAxis("ABS_HAT0Y", 17, b1name='dup', b2name='ddown')
            ],
            dead_zone=dead_zone,
            hot_zone=hot_zone)
# Get a joystick
with ControllerResource() as joystick:
    # Loop until we're disconnected
    while joystick.connected:
        left_y = joystick['rt']
        print(left_y[0:4])
        sleep(0.5)

