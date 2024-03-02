# init

import time
import os
from img_converter import greyscale, ascii_converter

def sort_images():

    result = {}
    for img in os.listdir("imgs"):
        fname = int(img.replace("frame","").split(".")[0])
        result[fname]= f"imgs/{img}"

    for i in range(len(result)):
        if result.get(i):
            yield result[i]


def run():
    frame_rate = 24
    for path in sort_images():

        grey = greyscale.GreyScale(80)
        ascii_conv = ascii_converter.AsciiConverter()
        result = ascii_conv.convert(grey.convert(path))
        ascii_converter.AsciiConverter.print_ascii(result)
        time.sleep(1/frame_rate)
        os.system("clear")


if __name__ == "__main__":
    run()
