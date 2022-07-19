import hid
import struct

# hid device path
PATH = b'DevSrvsID:4295239847'

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

mode = 9
dev = hid.Device(path=PATH)
msg = format_msg(change_rgb_mode(mode))
send_msg(dev, msg)
dev.close()