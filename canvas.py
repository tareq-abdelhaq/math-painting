import numpy as np
from PIL import Image


class Canvas:
    """
    Object represents canvas area with specific width, height and background color.
    """

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        self.data = np.zeros((height, width, 3), dtype=np.uint8)
        self.data[:] = color  # color: [R, G, B]

    def make_img(self, img_path):
        img = Image.fromarray(self.data, mode="RGB")
        img.save(img_path)
