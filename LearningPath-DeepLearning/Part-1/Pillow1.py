
from PIL import Image


if __name__ =="__main__":
    rose_Img = Image.open('rose.jpg')
    #rose_Img.show()
    rose_Img = rose_Img.resize( (200, 200))
    rose_Img.save("resized_rose.jpg");
    #rose_Img.crop(x1, y1, x2, y2) All points wrt to top left corner
    rose_Img = rose_Img.rotate(90)
    rose_Img.show()