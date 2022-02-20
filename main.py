import struct

import usb.core
from constants import RESPONSE_CODES as RC

from camera import Camera

""" out
0000   01 01 28 01 10 00 00 00 00 00 00 00 00 00 00 00
0010   da 0d 00 00 00 00 00 00 00 00 20 01 03 03 01 02
0020   06 01 01 00 da 04 82 23 | 10 00 00 00 01 00 02 94
0030   4d 04 00 00 40 00 00 02
"""

""" in
0000   01 01 28 01 22 00 00 00 00 00 00 00 00 00 00 00
0010   db 0d 00 00 00 00 00 00 00 00 20 01 03 03 82 02
0020   06 01 01 00 da 04 82 23 | 22 00 00 00 02 00 02 94
0030   4d 04 00 00 41 00 00 02 02 00 00 00 38 00 42 00
0040   00 02 04 00 00 00 1c 00 dc 00
"""


# Convert to bytestring
# bytes(string, 'raw_unicode_escape')

if __name__ == '__main__':
    import time
    c = Camera()
    time.sleep(5)
    c.set_iso(200)
    time.sleep(5)
    c.set_iso(400)
    time.sleep(5)
    c.set_iso(3200)
    c.snap()

# if __name__ == '__main__':
#     import time
#     count = 0
#     c = Camera()
#     for i in range(150):
#         c.snap()
#         r = c.read()
#         if RC[r.code[0]] == 'OK':
#             count += 1
#             print("Next")
#             time.sleep(0.33)
#         else:
#             code = RC[r.code[0]]
#             while code != "OK":
#                 print(f"Retrying: {RC[r.code[0]]}")
#                 c.snap()
#                 r = c.read()
#                 code = RC[r.code[0]]
#                 time.sleep(1)
#             print("Retry success, next")
#             count += 1
#
#     print(f"Total photos: {count}")
