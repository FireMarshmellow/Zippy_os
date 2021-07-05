from approxeng.input.selectbinder import ControllerResource
from time import sleep


            Used to set the hot zone for each :class:`approxeng.input.CentredAxis` and
with ControllerResource() as joystick:
    # Loop until we're disconnected
    while joystick.connected:
        left_y = joystick['rt']
        wet1, dry1 = 0, 1.0
        plant1prosent = (int(((left_y - wet1) * 100) / (dry1 - wet1)))
        print(plant1prosent)
        sleep(0.5)

