"""
File: blur.py
Name: Jo
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(old_img):
    """
    :param old_img: SimpleImage, the original image
    :return: new_img: SimpleImage, the image after blur
    """

    old_img = SimpleImage("images/smiley-face.png")
    # blank image for blurred
    new_img = SimpleImage.blank(old_img.width, old_img.height)
    for x in range(old_img.width):
        for y in range(old_img.height):
            # initiate with 0
            r_sum = 0
            g_sum = 0
            b_sum = 0
            count = 0
            # find pixel of x-1, x, x+1 and y-1, y, y+1 and add it with the neighbors
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x+i
                    pixel_y = y+j
                    if 0 <= pixel_x < old_img.width:
                        if 0 <= pixel_y < old_img.height:
                            pixel = old_img.get_pixel(pixel_x, pixel_y)
                            r_sum += pixel.red
                            g_sum += pixel.green
                            b_sum += pixel.blue
                            # count the number of neighbors
                            count += 1
            new_pixel = new_img.get_pixel(x, y)
            new_pixel.red = r_sum / count
            new_pixel.green = g_sum / count
            new_pixel.blue = b_sum / count
    return new_img


def main():
    """
    The program conducts blur function for the original image for 10 times
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    # first time blur
    blurred_img = blur(old_img)
    # 4 times blur
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
