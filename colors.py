# -*- encoding: utf-8 -*-
"""Generate random colors between two other colors."""

import collections
import random
import warnings

from palettes.palettes import Palettes

RGBColor = collections.namedtuple("RGBColor", ["red", "green", "blue"])


def Color(*args, **kwargs):
    warnings.warn("Color is deprecated, use RGBColor instead.", DeprecationWarning)
    return RGBColor(*args, **kwargs)


def random_color(start, end):
    """Create a random color within the user-defined range. Vary
    contrast slightly between outputs.
    """
    d_red = start.red - end.red
    d_green = start.green - end.green
    d_blue = start.blue - end.blue
    while True:
        chosen_d = random.uniform(0, 1)
        yield Color(
            start.red - int(d_red * chosen_d),
            start.green - int(d_green * chosen_d),
            start.blue - int(d_blue * chosen_d),
        )


def random_color_neue(start, end):
    """Retrieves a painter goblin palette and outputs a color per
    polygon to return to specktre's drawing function.
    """
    label, palette = Palettes().get_palette()
    while True:
        color = int(random.uniform(0, len(palette)))
        chosen_d = palette[color]
        yield Color(
            chosen_d[0],
            chosen_d[1],
            chosen_d[2],
        )


def random_color_hybrid(start, end):
    """Uses specktre's original algorithm to enhance brightness and
    bring in different color variations to the painter goblin original
    palettes.
    """
    label, palette = Palettes().get_palette()
    while True:
        color = int(random.uniform(0, len(palette)))
        chosen_d = palette[color]
        chosen_d_mod = random.uniform(0, 2)
        yield Color(
            int(chosen_d[0] * chosen_d_mod),
            int(chosen_d[1] * chosen_d_mod),
            int(chosen_d[2] * chosen_d_mod),
        )
