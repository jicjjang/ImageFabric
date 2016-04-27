import os

from PIL import Image


class Fabric(object):
    filepath = None
    savepath = None
    convertImage = None
    openedFile = None
    convertImagePixel = None
    width = None
    height = None
    min_width = None
    max_width = None
    min_height = None
    max_height = None

    outline = None

    def __init__(self, filepath, min_width=None, max_width=None, min_height=None, max_height=None, savepath=None):
        self.filepath = filepath
        self.savepath = savepath
        self.filename = self.filepath.split(".")[0].split('/')[-1]
        self.make_dir()
        self.set_items(min_width, max_width, min_height, max_height)
        self.image_to_binary()
        self.save_binary()

    def set_items(self, min_width, max_width, min_height, max_height):
        self.convertImage = Image.open(self.filepath).convert('L')
        self.openedFile = open(self.savepath + 'txt/output-' + self.filename + '.txt', 'w')
        self.convertImagePixel = self.convertImage.load()

        self.width = self.convertImage.width
        self.height = self.convertImage.height
        self.min_width = min_width or 0
        self.max_width = max_width or self.width
        self.min_height = min_height or 0
        self.max_height = max_height or self.height

        self.outline = [[1] * self.width for x in range(self.height)]

    def make_dir(self):
        if self.savepath is None:
            self.savepath = ""
        elif self.savepath[-1] is not '/':
            self.savepath += "/"
        if not os.path.exists(self.savepath + 'txt'):
            os.makedirs(self.savepath + 'txt')
        if not os.path.exists(self.savepath + 'img/create/' + self.filename + '/width'):
            os.makedirs(self.savepath + 'img/create/' + self.filename + '/width')
        if not os.path.exists(self.savepath + 'img/create/' + self.filename + '/height'):
            os.makedirs(self.savepath + 'img/create/' + self.filename + '/height')

    def image_to_binary(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.convertImagePixel[(j, i)] is not 255:
                    self.outline[i][j] = 0

    def save_binary(self):
        for i in range(self.height):
            for j in range(self.width):
                self.openedFile.write(str(self.outline[i][j]))
            self.openedFile.write('\n')

    def draw_pixel(self, img_width, img_height, count):
        for i in range(self.min_height, self.max_height):
            for j in range(self.min_width, self.max_width):
                if self.outline[i][j] is 1 and count > j:
                    img_width.putpixel((j, i), 255)
                if self.outline[i][j] is 1 and count > i:
                    img_height.putpixel((j, i), 255)
            if count == self.height:
                break

    def create_saved_binary_to_image(self):
        count = min(self.min_width, self.min_height)
        img_width = Image.new('L', (self.width, self.height), 1)
        img_height = Image.new('L', (self.width, self.height), 1)

        while (True):
            self.draw_pixel(img_width, img_height, count)

            if self.min_width < count < self.max_width:
                img_width.save(self.savepath + 'img/create/' + self.filename + '/width/' + str(count) + '.png', "PNG")
                print '[' + self.filename + '] created width/' + str(count) + '.png file'
            if self.min_height < count < self.max_height:
                img_height.save(self.savepath + 'img/create/' + self.filename + '/height/' + str(count) + '.png', "PNG")
                print '[' + self.filename + '] created height/' + str(count) + '.png file'

            count += 1
            if count >= max(self.max_width, self.max_height):
                break


if __name__ == '__main__':
    pass

else:
    pass
