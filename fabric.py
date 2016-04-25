from PIL import Image

# white : (255,255,255) --> 1
# black : (0,0,0) --> 0


class Fabric(object):
    filename = None
    convertImage = None
    openedFile = None
    convertImagePixel = None
    width = None
    height = None

    outline = None

    def __init__(self, filename):
        self.set_items(filename)
        self.outline_checker()
        self.save_binary()

    def set_items(self, filename):
        self.filename = filename
        self.convertImage = Image.open(self.filename).convert('L')
        self.openedFile = open('output.txt', 'w')
        self.convertImagePixel = self.convertImage.load()
        self.width = self.convertImage.width
        self.height = self.convertImage.height
        self.outline = [[1] * self.width for x in range(self.height)]

    def outline_checker(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.convertImagePixel[(j, i)] != 255:
                    self.outline[i][j] = 2

    def save_binary(self):
        for i in range(self.height):
            for j in range(self.width):
                self.openedFile.write(str(self.outline[i][j]))
            self.openedFile.write('\n')

    # def random_binary(self):
    #     for i in range(self.height):
    #         for j in range(self.width):
    #             self.openedFile.write(str(self.outline[i][j]))
    #         self.openedFile.write('\n')

    def save_image(self):
        img = Image.new('L', (self.width, self.height), "white")
        for i in range(self.height):
            for j in range(self.width):
                if self.convertImagePixel[(j, i)] is 2:
                    img.putpixel((j, i), 1)
        img.show()


if __name__ == '__main__':
    pass
else:
    pass
