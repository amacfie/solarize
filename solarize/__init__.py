from functools import cache
from itertools import product

from PIL import Image
import tqdm


palette = [
    (0, 43, 54),
    (7, 54, 66),
    (88, 110, 117),
    (101, 123, 131),
    (131, 148, 150),
    (147, 161, 161),
    (238, 232, 213),
    (253, 246, 227),
    (181, 137, 0),
    (203, 75, 22),
    (220, 50, 47),
    (211, 54, 130),
    (108, 113, 196),
    (38, 139, 210),
    (42, 161, 152),
    (133, 153, 0),
]

def distsq(pixel1, pixel2):
    return sum([(a - b) ** 2 for a, b in zip(pixel1, pixel2)])


@cache
def palette_col(r: int, g: int, b: int):
    distsqs = [distsq(c, (r, g, b)) for c in palette]
    index, _ = min(enumerate(distsqs), key=lambda x: x[1])
    return palette[index]


def solarize(img: Image, progress_bar: bool = False) -> Image:
    # TODO: faster algorithm? see
    # * https://en.m.wikipedia.org/wiki/Nearest_neighbor_search
    # * "Efficient Computation of 3D Clipped Voronoi Diagram"
    # * https://stackoverflow.com/questions/20189203/nearest-neighbor-using-voronoi-diagram
    # * https://en.wikipedia.org/wiki/Point_location#Higher_dimensions

    img = img.convert("RGB")

    if progress_bar:
        xys = tqdm.tqdm(
            product(range(img.width), range(img.height)),
            total=img.height * img.width,
        )
    else:
        xys = product(range(img.width), range(img.height))

    for x, y in xys:
        img.putpixel((x, y), palette_col(*img.getpixel((x, y))))

    return img

