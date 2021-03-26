"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def main():
    """
    This function a mirrored image of poppy.png by
    inserting old pixels into the empty one
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    blank_img = SimpleImage.blank(original_mt.width, original_mt.height*2)

    for x in range(original_mt.width):
        for y in range(original_mt.height):
            # colored pixel
            old_pixel = original_mt.get_pixel(x, y)
            # empty pixel 1
            new_pixel1 = blank_img.get_pixel(x, y)
            # empty pixel 2
            new_pixel2 = blank_img.get_pixel(x, blank_img.height-y-1)
            # insert pixel 1
            new_pixel1.red = old_pixel.red
            new_pixel1.green = old_pixel.green
            new_pixel1.blue = old_pixel.blue
            # insert pixel 2
            new_pixel2.red = old_pixel.red
            new_pixel2.green = old_pixel.green
            new_pixel2.blue = old_pixel.blue
    blank_img.show()


if __name__ == '__main__':
    main()
