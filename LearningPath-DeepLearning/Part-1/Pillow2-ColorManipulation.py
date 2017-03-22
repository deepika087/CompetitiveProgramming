from PIL import Image, ImageFilter, ImageEnhance


if __name__ =="__main__":
    rose_img = Image.open('rose.jpg')

    grayscale = rose_img.convert('LA')
    #grayscale.show()

    edge_detect = rose_img.filter(ImageFilter.FIND_EDGES)
    #edge_detect.show()

    contrast = ImageEnhance.Contrast(rose_img).enhance(1.5)
    contrast.show();

    sharpness = ImageEnhance.Sharpness(rose_img).enhance(2)
    sharpness.show()