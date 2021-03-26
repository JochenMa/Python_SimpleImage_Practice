"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image
    :param figure_img: SimpleImage, green screen figure image
    :return: figure_img, SimpleImage, figure img with  green screen pixels replaced by pixels of background
    """
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            pixel_figure = figure_img.get_pixel(x, y)
            bigger = max(pixel_figure.red, pixel_figure.blue)  # return the one that is bigger
            if pixel_figure.green > bigger*2:
                # replacement
                pixel_background = background_img.get_pixel(x, y)
                pixel_figure.red = pixel_background.red
                pixel_figure.green = pixel_background.green
                pixel_figure.blue = pixel_background.blue
    return figure_img


def main():
    """
    This function conducts green screen replacement
    that is able to photoshop a person onto any background
    """
    background = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    background.make_as_big_as(figure)
    result = combine(background, figure)
    result.show()


if __name__ == '__main__':
    main()
