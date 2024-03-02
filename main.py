# init

import time
import os
from img_converter import greyscale, ascii_converter
import sys


def sort_images() -> str:

    os.makedirs("imgs", exist_ok=True)
    result = {}
    for img in os.listdir("imgs"):
        fname = int(img.replace("frame", "").split(".")[0])
        result[fname] = f"imgs/{img}"

    if not result:
        print("Missing image files on folder imgs")

    for i in range(len(result)):
        if result.get(i):
            yield result[i]


def run(img_path:str=None, size:int=80) -> None:

    frame_rate = 60
    grey = greyscale.GreyScale(size)
    ascii_conv = ascii_converter.AsciiConverter()

    if not img_path:
        for path in sort_images():

            result = ascii_conv.convert(grey.convert(path))
            ascii_converter.AsciiConverter.print_ascii(result)
            time.sleep(1 / frame_rate)
            os.system("clear")

    else:
        result = ascii_conv.convert(grey.convert(img_path))
        ascii_converter.AsciiConverter.print_ascii(result)


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        img_path = sys.argv[1]
        size = 80 if len(args) < 2 else int(args[2])
        run(img_path, size)
    else:
        run()
