#!/usr/bin/env python3

"""
usage: python solarize.py <image_file>

out: result.jpg
"""

import sys

from PIL import Image

from solarize import solarize


img = Image.open(sys.argv[1])

img = solarize(img, progress_bar=True)

img.save('result.jpg', subsampling=0, quality=100)

