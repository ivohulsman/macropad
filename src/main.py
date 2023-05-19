from kb import KMKKeyboard

import supervisor

from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.handlers.sequences import simple_key_sequence


# Disable hot reloading on save
supervisor.runtime.autoreload = True


keyboard = KMKKeyboard()
layers = Layers()
modtap = ModTap()

# Debug mode
keyboard.debug_enabled = False

# Append extensions to KMK
keyboard.extensions.append(keyboard.rgb)
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(keyboard.oled)


# Init Rotary Encoder
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (keyboard.rot_a_pin, keyboard.rot_b_pin,
     keyboard.rot_bt_pin, False, 4),  # encoder #1
)

keyboard.modules = [layers, encoder_handler, modtap]

# Define layers
LYR_NOR, LYR_RGB, LYR_MOD = 0, 1, 2

# Define custom keys
MOD_OR_NORM = KC.MT(KC.TO(LYR_NOR), KC.MO(LYR_MOD))

# Save VIM macro
VIM_WBUF = simple_key_sequence(
    (
        KC.ESC,
        KC.COLN,
        KC.W,
        KC.ENTER,
    )
)

# Define Keymaps
keyboard.keymap = [
    [
        # Normal Layer
        KC.A, KC.B, KC.C, KC.D,
        VIM_WBUF, KC.F, KC.G, KC.H,
        KC.I, KC.J, KC.K, MOD_OR_NORM,
    ],
    [
        # RGB Layer
        KC.RGB_VAI, KC.RGB_VAD, KC.RGB_HUI, KC.RGB_HUD,
        KC.RGB_SAI, KC.RGB_SAD, KC.RGB_MODE_PLAIN, KC.RGB_MODE_BREATHE,
        KC.RGB_MODE_RAINBOW, KC.RGB_MODE_BREATHE_RAINBOW, KC.RGB_MODE_SWIRL, KC.MO(
            LYR_MOD),
    ],
    [
        # Mode Layer
        KC.TO(LYR_NOR), KC.B, KC.C, KC.D,
        KC.E, KC.F, KC.G, KC.H,
        KC.TO(LYR_RGB), KC.J, KC.RELOAD, KC.L,
    ]
]

# Define Rotary Encoder Keymaps
encoder_handler.map = [((KC.VOLD, KC.VOLU, KC.MUTE),),  # Standard
                                ((KC.VOLD, KC.VOLU, KC.MUTE),),  # Extra
                                ]

if __name__ == '__main__':
    keyboard.go()
