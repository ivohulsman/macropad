import os
import board
import busio 
import neopixel

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.extensions.rgb import RGB
from kmk.extensions.oled import Oled, TextEntry, ImageEntry # New OLED extension


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP8,
        board.GP7,
        board.GP6,
        board.GP5,
    )

    row_pins = (
        board.GP4,
        board.GP3,
        board.GP2,
    )

    diode_orientation = DiodeOrientation.ROWS

    bl_pin = board.GP13
    ug_pin = board.GP12

    rot_a_pin = board.GP10
    rot_b_pin = board.GP11
    rot_bt_pin = board.GP9

    SCL = board.GP1
    SDA = board.GP0

# Init RGB
    pixels = (
        neopixel.NeoPixel(bl_pin, 12,),
        neopixel.NeoPixel(ug_pin, 4,)
    )

    rgb = RGB(pixel_pin=None, pixels=pixels,
              hue_default=os.getenv("RGB_HUE"),
              sat_default=os.getenv("RGB_SAT"),
              val_default=os.getenv("RGB_BOOT_VAL"),
              val_limit=os.getenv("RGB_VAL"),
              val_step=36)

    oled = Oled(
        entries=[
            TextEntry(text='my', x=128, y=0, x_anchor='R'),
            TextEntry(text='keyboard', x=128, y=10, x_anchor='R'),
            TextEntry(text='left', x=128, y=20, x_anchor='R', side='L'),
            TextEntry(text='right', x=128, y=20, x_anchor='R', side='R'),
            TextEntry(text='Layer: ', x=0, y=32, y_anchor='B'),
            TextEntry(text='BASE', x=40, y=32, y_anchor='B', layer=0),
            TextEntry(text='LOWER', x=40, y=32, y_anchor='B', layer=1),
            TextEntry(text='RAISE', x=40, y=32, y_anchor='B', layer=2),
            TextEntry(text='RGB', x=40, y=32, y_anchor='B', layer=3),
            TextEntry(text='SETTINGS', x=40, y=32, y_anchor='B', layer=4),
            TextEntry(text='0 1 2 3 4', x=0, y=4),
            TextEntry(text='0', x=0, y=4, inverted=True, layer=0),
            TextEntry(text='1', x=12, y=4, inverted=True, layer=1),
            TextEntry(text='2', x=24, y=4, inverted=True, layer=2),
            TextEntry(text='3', x=36, y=4, inverted=True, layer=3),
            TextEntry(text='4', x=48, y=4, inverted=True, layer=4),
        ],
        i2c=busio.I2C(SCL, SDA),
        device_address=0x3C,
        width=128,
        height=64,
        flip=False,
        flip_left=False,
        flip_right=True,
        dim_time=10,
        dim_target=0.1,
        off_time=30,
        powersave_dim_time=5,
        powersave_dim_target=0.1,
        powersave_off_time=120,
        brightness=1,
        brightness_step=0.1,
    )

# i2c = io.I2C(scl=board.GP1, sda=board.GP0, frequency=400000)
