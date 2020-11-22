import Player

def createPlayer(name, url, height, width):
    return Player.Player(name, url, height, width)

def createPipe(width, height, colour):
    return Player.Pipe(height, width, colour)

def setScore(score, player):
    player.setScore(score)