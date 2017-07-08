# -*- coding: utf8 -*-
from PIL import ImageGrab

import time
time.sleep(10)
# if os.path.exists(fileNamePicture):
#     os.remove(fileNamePicture)
image = ImageGrab.grab()
image.save("test.png")