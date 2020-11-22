class Icon:
    def __init__(self, url, height, width):
        self.__url = url
        self.__height = height
        self.__width = width

    def getUrl(self):
        return self.__url
    
    def getHeight(self):
        return self.__height

    def getWidth(self):
        return self.__width

class Player:
    def __init__(self, name, url, height, width):
        self.__name = name
        self.__icon = Icon(url, height, width)
        self.score = 0

    def getName(self):
        return self.__name

    def getIcon(self):
        return self.__icon

    def setScore(self, score):
        self.__score = score

class Pipe:
    def __init__(self, height, width, colour, x, y):
        self.__height = height
        self.__width = width
        self.__colour = colour
        self.__x = x
        self.__y = y

    def getHeight(self):
        return self.__height

    def getWidth(self):
        return self.__width

    def getColour(self):
        return self.__colour

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y