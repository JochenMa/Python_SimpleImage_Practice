"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,ㄧㄢ
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file path of the original image
    :return img: The image with 1/4 size
    """
    img = SimpleImage('images/poppy.png')
    # blank image that is 1/4 size
    new_img = SimpleImage.blank(img.width//2, img.height//2)
    for x in range(new_img.width):
        for y in range(new_img.height):
            # colored pixel
            img_pixel = img.get_pixel(2*x, 2*y)
            # empty pixel
            new_img_pixel = new_img.get_pixel(x, y)
            # replacement
            new_img_pixel.red = img_pixel.red
            new_img_pixel.green = img_pixel.green
            new_img_pixel.blue = img_pixel.blue
    return new_img


def main():
    """
    This function is to make the original photo into 1/4 size
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    # shrink function
    after_shrink = shrink('images/poppy.png')
    after_shrink.show()


if __name__ == '__main__':
    main()
