import hid
import struct
import sys

status = sys.argv[1]

# Update with your directory
file = open("/Users/dustin/swiftbar-key/path.log", "r")
PATH = file.read().encode('utf-8')
file.close()

# constants
CMD_VIA_LIGHTING_SET_VALUE = 0x07
VIALRGB_SET_MODE = 0x41
QMK_RGBLIGHT_BRIGHTNESS = 0x80
QMK_RGBLIGHT_EFFECT = 0x81
QMK_RGBLIGHT_COLOR = 0x83
MSG_LEN = 32

# helper functions
def change_rgb_mode(mode):
    msg = struct.pack(">BBB", CMD_VIA_LIGHTING_SET_VALUE, QMK_RGBLIGHT_EFFECT, mode)
    return(msg)

def change_rgb_brightness(v):
    msg = struct.pack(">BBB", CMD_VIA_LIGHTING_SET_VALUE, QMK_RGBLIGHT_BRIGHTNESS, v)
    return(msg)

def change_rgb_color(h, s):
    msg = struct.pack(">BBBB", CMD_VIA_LIGHTING_SET_VALUE, QMK_RGBLIGHT_COLOR, h, s)
    return(msg)

def format_msg(msg):
    msg += b"\x00" * (MSG_LEN - len(msg))
    return(msg)

def send_msg(dev, msg):
    dev.write(b"\x00" + msg)
if status == 'green':
    mode = 3
    dev = hid.Device(path=PATH)
    msg = format_msg(change_rgb_mode(mode))
    send_msg(dev, msg)
    dev.close()

    dev = hid.Device(path=PATH)
    msg = format_msg(change_rgb_color(80, 255))
    send_msg(dev, msg)
    dev.close()
elif status == 'red':
    mode = 3
    dev = hid.Device(path=PATH)
    msg = format_msg(change_rgb_mode(mode))
    send_msg(dev, msg)
    dev.close()

    dev = hid.Device(path=PATH)
    msg = format_msg(change_rgb_color(0, 255))
    send_msg(dev, msg)
    dev.close()
elif status == 'idle':
    mode = 9
    dev = hid.Device(path=PATH)
    msg = format_msg(change_rgb_mode(mode))
    send_msg(dev, msg)
    dev.close()