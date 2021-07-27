import typing
from PIL import Image, ImageFilter

class ImageProcessor(object):

    def __init__(self, input_file, output_file, filters) -> None:
        self.input_file = input_file
        self.output_file = output_file
        self.filters  = filters


    def print_image(self) -> None:
        im = Image.open(self.input_file)
        print(im.format, im.size, im.mode)

    def save_image(self, image) -> None:
        if self.input_file != self.output_file:
            try:
                image.save(self.output_file)
            except e as OSError:
                print(e)
                print("cannot convert", self.input_file)


    def gray_scale(self, image) -> Image:
        return image.convert('L')

    def rotate(self, image) -> Image:
        return image.rotate(45)

    def changeImageSize(self, maxWidth, maxHeight, image):
        widthRatio  = maxWidth/image.size[0]
        heightRatio = maxHeight/image.size[1]

        newWidth    = int(widthRatio*image.size[0])
        newHeight   = int(heightRatio*image.size[1])

        newImage    = image.resize((newWidth, newHeight))
        return newImage

    def overlay(self, image) -> Image:
        foreground_img = Image.open("python.png")
        transformed_image = self.changeImageSize(800, 500, image).convert('RGBA')
        transformed_foreground = self.changeImageSize(800, 500, foreground_img).convert('RGBA')
        return Image.alpha_composite(transformed_image, transformed_foreground).convert('RGB')

    def blur(self, image) -> Image:
        return image.filter(ImageFilter.BLUR)

    def sharpen(self, image) -> Image:
        return image.filter(ImageFilter.SHARPEN)

    def apply_filters(self) -> None:
        image = Image.open(self.input_file)
        for filter in self.filters:
            if hasattr(self, filter):
                image_fn = getattr(self, filter)
                image = image_fn(image)
            else:
                print("Filter is not yet implemented")
        self.save_image(image)