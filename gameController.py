import Characters

def createPlayer(name, url, height, width):
    return Characters.Player(name, url, height, width)

def createPipe(width, height, colour, x, y):
    return Characters.Pipe(height, width, colour, x, y)

def setScore(score, player):
    player.setScore(score)