"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage

# Constants
HURDLE_FACTOR = 1.05   # Controls the threshold of detecting green screen pixel


def highlight_fires(filename):
    """
    :param filename:str, the file path of the original image
    :return: img: The image with highlighted fire
    """
    highlighted_fire = SimpleImage('images/greenland-fire.png')
    for pixel in highlighted_fire:
        # The average can make the picture gray
        avg = (pixel.red+pixel.blue+pixel.green)//3
        # Only highlight the red part
        if pixel.red > avg*HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            # gray
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return highlighted_fire


def main():
    """
    This function conducts the highlighted of fire
    that is able to detect the fire place and turn the over area to gray
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
