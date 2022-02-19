import usb.core
from constants import LMX_EVENT_ID

VENDOR_ID = 0x04da
PRODUCT_ID = 0x2382  # Panasonic G9

# TODO: Figure out what each of these do
_SUFFIX = 0x000010809404000100000010

SINGLE_SHOT = _SUFFIX.to_bytes(12, 'little') + \
              LMX_EVENT_ID.LMX_DEF_LIB_TAG_REC_CTRL_RELEASE_ONESHOT.value.to_bytes(4, 'little')


class Camera:
    def __init__(self, product_id=PRODUCT_ID, vendor_id=VENDOR_ID):
        self._device = usb.core.find(idProduct=product_id, idVendor=vendor_id)
        self._configuration = self._device.get_active_configuration()
        self._device.set_configuration(self._configuration)
        self._device.reset()

    @property
    def interface(self):
        return self._configuration.interfaces()[0]

    @property
    def endpoints(self):
        return self.interface.endpoints()

    def snap(self):
        self.endpoints[0].write(SINGLE_SHOT)

    def read(self):
        return self.endpoints[1].read(self.endpoints[1].wMaxPacketSize)

    def write(self, data):
        return self.endpoints[0].write(data)
