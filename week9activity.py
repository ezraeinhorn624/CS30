import struct
from functools import reduce

'''
You need to implement the five functions defined below.
Each function takes a single argument:
  an image represented as a list of lists of pixels, where
  each pixel is a list of 3 integers.
Each function returns a list in exactly that same form.

The readPPM and writePPM functions defined at the end of the file should NOT be
called by your code.  Rather, they are provided to help you test your code:
readPPM allows you to convert PPM image files into lists of lists of pixels that
can be passed as arguments to your functions, and writePPM allows you to write the
results of your functions to image files so that the images can be viewed.
'''


def negate(pixels): 
    return


def greyscale(pixels):
    return


def upsideDown(pixels):
    return


def mirrorImage(pixels):
    return


def scale(pixels):
    return


# read the PPM image file named fname and convert it to a list of lists of pixels.
# each pixel is an RGB triple, represented as a list of size 3.
# each list of pixels represents one row in the image, ordered from top to bottom.
def readPPM(fname):
    f = open(fname, "rb")
    p6Ignore = f.readline()
    dimensions = f.readline().split()
    width = int(dimensions[0])
    height = int(dimensions[1])
    maxIgnore = f.readline()

    pixels = []
    rgbData = [x for x in f.read()]
    f.close()
    for r in range(height):
        row = []
        for c in range(width):
            i = 3 * (r * width + c)
            row.append(rgbData[i:i+3])
        pixels.append(row)
    return pixels


# pixels should be a list of list of RGB triples, in the same format as returned
# by the readPPM function above.
# this function writes those pixels to the file named fname as a PPM image.
def writePPM(pixels, fname):
    f = open(fname, "wb")
    f.write("P6\n".encode())
    width = len(pixels[0])
    height = len(pixels)
    f.write((str(width) + " " + str(height) + "\n").encode())
    f.write((str(255) + "\n").encode())
    bPixels = [[struct.pack('BBB', p[0], p[1], p[2]) for p in r] for r in pixels]
    flatPixels = reduce(lambda x,y: x+y, bPixels)
    f.writelines(flatPixels)
    f.close()


