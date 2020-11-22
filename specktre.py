# -*- encoding: utf-8 -*-
"""Generate checkerboard wallpaper images.

Usage:
  specktre.py new --size=<size> --start=<start> --end=<end> [--squares | --triangles | --hexagons] [--name=<name>]
  specktre.py -h

Options:
  -h --help          Show this screen.
  --size=<size>      Size in pixels - WxH (e.g. 100x200)
  --start=<start>    Start of the color range (hex, e.g. #01ab23)
  --end=<end>        End of the color range (hex, e.g. #01ab23)
  --squares          Tile with squares.
  --triangles        Tile with triangles.
  --hexagons         Tile with hexagons.
  --name=<name>      (Optional) Name of the file to save to.

"""  # noqa

import collections
import sys

import docopt
from PIL import Image, ImageDraw

import cli
from colors import random_color, random_color_neue, random_color_hybrid
from tilings import generate_hexagons, generate_squares, generate_triangles
from utils import new_filename

Settings = collections.namedtuple(
    "Settings", ["generator", "width", "height", "start_color", "end_color", "name"]
)


def parse_args(argv):
    """Parse the command line arguments.
    """

    # TODO; Add args back into the code when there's an opportunity.

    # args = docopt.docopt(__doc__, argv)

    args = {}

    try:
        if args["--squares"]:
            generator = generate_squares
        elif args["--triangles"]:
            generator = generate_triangles
        elif args["--hexagons"]:
            generator = generate_hexagons
    except KeyError:
        generator = generate_triangles

    # TODO: Un-hard-code the size and color values used here.

    width = 1000
    height = 1000

    start_color = cli.check_color_input("#01ab23")
    end_color = cli.check_color_input("#000000")

    name = "test_image.png"

    return Settings(
        generator=generator,
        width=width,
        height=height,
        start_color=start_color,
        end_color=end_color,
        name=name,
    )


def draw_speckled_wallpaper(settings):
    im = Image.new(mode="RGB", size=(settings.width, settings.height))
    squares = settings.generator(settings.width, settings.height)
    # colors = random_color(settings.start_color, settings.end_color)
    colors = random_color_neue(settings.start_color, settings.end_color)
    # colors = random_color_hybrid(settings.start_color, settings.end_color)
    for sq, color in zip(squares, colors):
        ImageDraw.Draw(im).polygon(sq, fill=color)
    return im


def save_speckled_wallpaper(settings):
    im = draw_speckled_wallpaper(settings)
    if settings.name:
        filename = settings.name
    else:
        filename = new_filename()
    im.save(filename)
    print("Saved new wallpaper as %s" % filename)


def main():
    settings = parse_args(sys.argv)
    save_speckled_wallpaper(settings)


if __name__ == "__main__":
    main()
