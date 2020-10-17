import random
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.window import *


def spawninimigos (sprite,quantidade,layer,janelawidth):

    # cria uma lista com inimigos
    a = 0
    inimigos = []
    while a < quantidade:
        inimigo = Sprite(sprite)
        inimigo.x = random.randint(janelawidth,10000)
        inimigo.y = layer.y - inimigo.height + 10
        inimigos += [inimigo]
        a+=1
    return inimigos

def spawninimigos2 (layer3):

    # cria uma lista com inimigos que jogam granadas
    inimigos2 = []
    for x in layer3:
        inimigo2 = Sprite("GameImages\sinimigo22.png", 4)
        inimigo2.set_total_duration(5000)
        inimigo2.x = x.x - 20
        inimigo2.y = x.y - 80
        inimigos2 += [inimigo2]
    return inimigos2




tempotranscorrido3 = 0
def tirosinimigos (listadeinimigos,janelawidth,tirosinimigos):

    # configura os tiros inimigos
    global tempotranscorrido3
    atiradores = [x for x in listadeinimigos if x.x <= janelawidth and x.x >= 0]
    if tempotranscorrido3 >= 2:
        for i in range(len(atiradores)):
            tiro = Sprite("GameImages\stiro.png")
            tiro.x = atiradores[i].x
            tiro.y = atiradores[i].y + 31
            tirosinimigos += [tiro]
        tempotranscorrido3 = 0


