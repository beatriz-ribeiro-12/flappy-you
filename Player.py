class Icon:
    def __init__(self, url, height, width):
        self.__url = url
        self.__height = height
        self.__width = width

class Player:
    def __init__(self, name, url, height, width):
        self.__name = name
        self.__icon = Icon(url, height, width)
        self.score = 0

    def setScore(self, score):
        self.__score = score

class Pipe:
    def __init__(self, height, width, colour):
        self.__height = height
        self.__width = width
        self.__colour = colour