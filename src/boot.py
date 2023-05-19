import usb_hid
import displayio

displayio.release_displays()
usb_hid.enable(boot_device=1)