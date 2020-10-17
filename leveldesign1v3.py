# background estatico
fundo = GameImage("GameImages\sbg12.png")

PRIMEIROTILE = Sprite("GameImages\stile1.png")
PRIMEIROTILE.x = 0
PRIMEIROTILE.y = 629
ULTIMOTILE = Sprite("GameImages\sfim.png")
ULTIMOTILE.x = 12100
ULTIMOTILE.y = 0
PENULTIMOTILE = Sprite("GameImages\sfim.png")
PENULTIMOTILE.x = 10740
PENULTIMOTILE.Y = 0

class Layer(list):
    # cria uma lista para qual é possível criar atributos
    def __new__(self, *args, **kwargs):
        return super(Layer, self).__new__(self, args, kwargs)

    def __init__(self, *args, **kwargs):
        if len(args) == 1 and hasattr(args[0], '__iter__'):
            list.__init__(self, args[0])
        else:
            list.__init__(self, args)
        self.__dict__.update(kwargs)

    def __call__(self, **kwargs):
        self.__dict__.update(kwargs)
        return self

# layers, listas que contem os tiles
layer0 = Layer()
layer0.y = 630
layer1 = Layer()
layer1.y = 450
layer2 = Layer()
layer2.y = 290
layer3 = Layer()
layer3.y = 120
layer4 = Layer()
layer4.y = 70


def addTiles(layer, spritedic, xposition, quantidade):

    # cria uma quantidade de  tiles em um layer
    global layer0,layer1,layer2,layer3,layer4
    a = 0
    while a < quantidade:
        sprite = Sprite(spritedic)
        sprite.x = xposition
        sprite.y = layer.y
        layer += [sprite]
        xposition += sprite.width
        a+=1

addTiles(layer0,"GameImages\stile2.png",0, 500),
addTiles(layer1,"GameImages\stile2.png",700, 4), addTiles(layer1,"GameImages\stile2.png", 2800, 4), addTiles(layer1,"GameImages\stile2.png", 3500, 4),addTiles(layer1,"GameImages\stile2.png", 4500, 1),addTiles(layer1,"GameImages\stile2.png", 4835, 1),addTiles(layer1,"GameImages\stile2.png", 5170, 1), addTiles(layer1, "GameImages\stile2.png", 5570,4), addTiles(layer1, "GameImages\stile2.png", 6000, 2)
addTiles(layer2,"GameImages\stile2.png", 2532, 4), addTiles(layer2,"GameImages\stile2.png", 3200, 2), addTiles(layer2,"GameImages\stile2.png", 3900, 4), addTiles(layer2, "GameImages\stile2.png", 4600, 2), addTiles(layer2, "GameImages\stile2.png", 5970, 2)
addTiles(layer3,"GameImages\stile2.png",2465,1), addTiles(layer3,"GameImages\stile2.png", 3830, 1)
addTiles(layer4,"GameImages\sarvore.png", 12000, 1)
addTiles(layer4,"GameImages\sarvore.png", 10500, 1)
addTiles(layer1,"GameImages\stile2.png", 11350, 1)
addTiles(layer1,"GameImages\stile2.png",5000, 4), addTiles(layer1,"GameImages\stile2.png", 7800, 4), addTiles(layer1,"GameImages\stile2.png", 8500, 4),addTiles(layer1,"GameImages\stile2.png", 9500, 1),addTiles(layer1,"GameImages\stile2.png", 9835, 1),addTiles(layer1,"GameImages\stile2.png", 10170, 1)
addTiles(layer2,"GameImages\stile2.png", 7532, 4), addTiles(layer2,"GameImages\stile2.png", 8200, 2), addTiles(layer2,"GameImages\stile2.png", 8900, 4), addTiles(layer2, "GameImages\stile2.png", 9600, 2), addTiles(layer2, "GameImages\stile2.png", 10000, 2)
addTiles(layer3,"GameImages\stile2.png",7465,1), addTiles(layer3,"GameImages\stile2.png", 8830, 1)
addTiles(layer3,"GameImages\stile2.png",10850,1), addTiles(layer3,"GameImages\stile2.png", 11200, 1),addTiles(layer3,"GameImages\stile2.png",11550,1)


# cria os focos de incendio na fase
p = [x.x for x in layer2]
p2 = []
fogos = []
ii = 0
t = 0
while len(p2) < 20:
    aaa = random.choice(p)
    if aaa not in p2:
        p2 += [aaa]

while t <= 9:
    fogo = Sprite("GameImages\sfogo.png", 5)
    fogo.set_total_duration(1000)
    fogo.y = layer2.y - fogo.height
    fogo.x = p2[ii]
    fogos += [fogo]
    ii += 1
    t += 1








