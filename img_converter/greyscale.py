from PIL import Image
import numpy as np


class GreyScale:

    def __init__(self, resize=300):
        self.base_width = resize

    def convert(self, img_path) -> int:
        img = Image.open(img_path)
        convert_img = self._resize(img).convert("L")
        return np.array(convert_img)

    def _resize(self, img: Image):
        wpercent = self.base_width / float(img.size[0])
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((self.base_width , hsize), Image.Resampling.LANCZOS)
        return img
