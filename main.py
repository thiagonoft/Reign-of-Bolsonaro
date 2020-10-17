from PPlay.window import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.animation import *
import time
from PPlay.collision import *
import inimigos
import random

# criando a janela e teclado/mouse
janela = Window(1024,700)
janela.set_title("Protect the Amazon!")
janela.set_background_color([0,0,0])
teclado = Window.get_keyboard()
mouse = Mouse()

# lendo o arquivo que contem o design da fase
exec(open("leveldesign1v3.py").read())

# botoes do menu
jogar1 = GameImage("GameImages\jogar1.png")
jogar2 = GameImage("GameImages\jogar2.png")
dificuldade1 = GameImage("GameImages\dificuldade1.png")
dificuldade2 = GameImage("GameImages\dificuldade2.png")
rank1 = GameImage("GameImages\scomojogar2.png")
rank2 = GameImage("GameImages\scomojogar1.png")
sair1 = GameImage("GameImages\sair1.png")
sair2 = GameImage("GameImages\sair2.png")
facil1 = GameImage("GameImages\sfacil1.png")
facil2 = GameImage("GameImages\sfacil2.png")
medio1 = GameImage("GameImages\medio1.png")
medio2 = GameImage("GameImages\medio2.png")
dificil1 = GameImage("GameImages\dificil1.png")
dificil2 = GameImage("GameImages\dificil2.png")

# posicao dos botoes do menu
jogar1.x = janela.width/2 - jogar1.width/2
jogar2.x = janela.width/2 - jogar1.width/2
dificuldade1.x = janela.width/2 - dificuldade1.width/2
dificuldade2.x = janela.width/2 - dificuldade1.width/2
rank1.x = janela.width/2 - rank1.width/2
rank2.x = janela.width/2 - rank1.width/2
sair1.x = janela.width/2 - sair1.width/2
sair2.x = janela.width/2 - sair1.width/2


jogar1.y = (float(janela.height)/1.47164)
jogar2.y = (float(janela.height)/1.47164)
dificuldade1.y = (float(janela.height)/1.31374)
dificuldade2.y = (float(janela.height)/1.31374)
rank1.y = (float(janela.height)/1.18288)
rank2.y = (float(janela.height)/1.18288)
sair1.y = (float(janela.height)/1.08923)
sair2.y = (float(janela.height)/1.08923)


# posicao dos botoes dificuldade
facil1.x = janela.width/2 - facil1.width/2
facil2.x = janela.width/2 - facil2.width/2
medio1.x = janela.width/2 - medio1.width/2
medio2.x = janela.width/2 - medio2.width/2
dificil1.x = janela.width/2 - dificil1.width/2
dificil2.x = janela.width/2 - dificil2.width/2

facil1.y = (float(janela.height)/1.47164)
facil2.y = (float(janela.height)/1.47164)
medio1.y = (float(janela.height)/1.31374)
medio2.y = (float(janela.height)/1.31374)
dificil1.y = (float(janela.height)/1.18288)
dificil2.y = (float(janela.height)/1.18288)

# criando os sprites de movimentacao do personagem
charparado = Sprite("GameImages\spersonagem.png")
charparado.set_position(100,janela.height-57-charparado.height)
chardireita = Sprite("GameImages\walk2.png",9)
chardireita.set_total_duration(1000)
chardireita.set_position(100,janela.height-57-charparado.height)
charesquerda = Sprite("GameImages\walk3.png",9)
charesquerda.set_total_duration(1000)
charesquerda.set_position(100,janela.height-57-charparado.height)
viradopara = 1 #1 direita 2 esquerda

# criando o sprite do arco
arco = Sprite("GameImages\sarco1.png")
# arco.set_position(100+charparado.width/2,janela.height-87-charparado.height/2)
arco.x = charparado.x + charparado.width/2
arco.y = charparado.y + charparado.height/4
flechas1 = []
flechas2 = []
velflecha = 500

# definindo as velocidades do pulo e a gravidade e uma variável de controle
vely = 0
g = 0
huga = True

# criando uma lista com os inimigos atraves da função spawninimigos e seus respectivos projeteis
inimigoss = inimigos.spawninimigos("GameImages\inimigo1.png",20,layer0,janela.width)
tirosinimigos = []
inimigoss2 = inimigos.spawninimigos2(layer3)
granadas = []
velgranadax = 100
velgranaday = 400
explosao = Sprite("GameImages\explosao.png",5)
explosao.set_total_duration(500)
explosao.hide()
explosoes = []


# vida do personagem
vida = 3
reviver = 1

# dificuldade do jogo, por padrao: medio
dificuldade = 2

# contadores de tempo
contador = 0
tempotranscorrido = 0
fps = 0
tempinho = 100
tempotranscorrido2 = 4

# boss fight
win = 0
vilao_life = 5
tempo_tiro_boss = 0
tiroboss = []
vel_vilao = 300
lock = True
vilao = Sprite("GameImages\svilao_game_cortado.png")
vilao.set_position(11900, 380)
death_boss = Sprite("GameImages\death_boss.png", 5)
death_boss.set_total_duration(1000)
death_boss.set_position(vilao.x, vilao.y)
explosion = 1
GameState = 0
Running = True

while Running:
    while GameState == 4:
        exec(open("tutorial.py").read())
    while GameState == 0:
        exec(open("menu.py").read())
    while GameState == 2:
        exec(open("dificuldade.py").read())
    while GameState == 3:
        exec(open("gameover.py").read())
    while GameState == 1:

        # definindo a condição de morte do jogador
        if vida == 0:
            GameState = 3

        # atualizando o contador de FPS
        tempotranscorrido += janela.delta_time()
        contador += 1
        if tempotranscorrido >= 1:
            fps = contador
            contador = 0
            tempotranscorrido = 0

        # movimentação do cenário
        if teclado.key_pressed("RIGHT") and (vilao_life <= 0 or ULTIMOTILE.x > 200) and (PENULTIMOTILE.x > 200 or inimigoss == [] and fogos == []):
            for i in range(len(layer0)):
                layer0[i].x -=5
            for i in range(len(layer1)):
                layer1[i].x -=5
            for i in range(len(layer2)):
                layer2[i].x -=5
            for i in range(len(layer3)):
                layer3[i].x -=5
            for i in range(len(layer4)):
                layer4[i].x -=5
            for i in range(len(inimigoss)):
                inimigoss[i].x -=5
            for i in range(len(inimigoss2)):
                inimigoss2[i].x -= 5
            for i in range(len(tirosinimigos)):
                tirosinimigos[i].x -=5
            for i in range(len(granadas)):
                granadas[i].x -=5
            for i in range(len(flechas1)):
                flechas1[i].x -=2
            for i in range(len(flechas2)):
                flechas2[i].x -= 2
            for i in range(len(fogos)):
                fogos[i].x -= 5
            for i in range(len(tiroboss)):
                tiroboss[i].x -= 2
            explosao.x -= 5
            PRIMEIROTILE.x -=5
            PENULTIMOTILE.x -=5
            ULTIMOTILE.x -= 5
            vilao.x -= 5
            death_boss.x -= 5


        elif teclado.key_pressed("LEFT") and PRIMEIROTILE.x < 0:
            for i in range(len(layer0)):
                layer0[i].x += 5
            for i in range(len(layer1)):
                layer1[i].x +=5
            for i in range(len(layer2)):
                layer2[i].x +=5
            for i in range(len(layer3)):
                layer3[i].x +=5
            for i in range(len(layer4)):
                layer4[i].x +=5
            for i in range(len(inimigoss)):
                inimigoss[i].x +=5
            for i in range(len(inimigoss2)):
                inimigoss2[i].x += 5
            for i in range(len(tirosinimigos)):
                tirosinimigos[i].x += 2
            for i in range(len(granadas)):
                granadas[i].x +=5
            for i in range(len(flechas1)):
                flechas1[i].x += 2
            for i in range(len(flechas2)):
                flechas2[i].x += 2
            for i in range(len(fogos)):
                fogos[i].x += 5
            for i in range(len(tiroboss)):
                tiroboss[i].x += 2
            explosao.x += 5
            PRIMEIROTILE.x += 5
            PENULTIMOTILE.x += 5
            ULTIMOTILE.x += 5
            vilao.x += 5
            death_boss.x += 5

        # desenhando os layers na tela
        fundo.draw()
        PRIMEIROTILE.draw()
        for x in layer0:
            x.draw()
        for x in layer1:
            x.draw()
        for x in layer2:
            x.draw()
        for x in layer3:
            x.draw()
        for x in layer4:
            x.draw()

        # fazendo com que as animaçoes de caminhada ocorram quando em contato com algum layer
        if charparado.y == 450 - 110:
            if g == 1500:
                teste1 = True
        else:
            teste1 = False
        if charparado.y == layer2.y - 110:
            if g == 1500:
                teste2 = True
        else:
            teste2 = False
        if teclado.key_pressed("RIGHT") and chardireita.y >= janela.height-57-charparado.height:
            chardireita.draw()
            chardireita.update()
            charparado = Sprite("GameImages\spersonagem.png")
            charparado.set_position(100,janela.height-57-charparado.height)
            viradopara = 1

        elif teclado.key_pressed("LEFT") and charesquerda.y >= janela.height-57-charparado.height:
            charesquerda.draw()
            charesquerda.update()
            charparado = Sprite("GameImages\personagem2.png")
            charparado.set_position(100,janela.height-57-charparado.height)
            viradopara = 2
        else:
            if teste1 == False:
                if teste2 == False:
                    charparado.draw()
        if teste1:
            if teclado.key_pressed("RIGHT"):
                chardireita.draw()
                chardireita.update()
                charparado = Sprite("GameImages\spersonagem.png")
                charparado.set_position(100, layer1.y - 110)
                viradopara = 1
            elif teclado.key_pressed("LEFT"):
                charesquerda.draw()
                charesquerda.update()
                charparado = Sprite("GameImages\personagem2.png")
                charparado.set_position(100, layer1.y - 110)
                viradopara =2
            else:
                charparado.draw()
        if teste2:
            if teclado.key_pressed("RIGHT"):
                chardireita.draw()
                chardireita.update()
                charparado = Sprite("GameImages\spersonagem.png")
                charparado.set_position(100,layer2.y - 110)
                viradopara = 1
            elif teclado.key_pressed("LEFT"):
                charesquerda.draw()
                charesquerda.update()
                charparado = Sprite("GameImages\personagem2.png")
                charparado.set_position(100, layer2.y - 110)
                viradopara =2
            else:
                charparado.draw()

        # configurando os sprites do arco para que a flecha desapareca quando em cooldown
        tempotranscorrido2 += janela.delta_time()
        if viradopara == 1:
            if tempotranscorrido2 >= 1 * dificuldade:
                arco = Sprite("GameImages\sarco1.png")
                #arco.set_position(100 + charparado.width / 2, janela.height - 87 - charparado.height / 2)
                arco.x = charparado.x + charparado.width / 2
                arco.y = charparado.y + charparado.height/4

            else:
                arco = Sprite("GameImages\sarco12.png")
                #arco.set_position(105 + charparado.width / 2, janela.height - 87 - charparado.height / 2)
                arco.x = charparado.x + charparado.width / 2
                arco.y = charparado.y + charparado.height / 4
        elif viradopara == 2:
            if tempotranscorrido2 >= 1 * dificuldade:
                arco = Sprite("GameImages\sarco2.png")
                #arco.set_position(100, janela.height - 87 - charparado.height / 2)
                arco.x = charparado.x - charparado.width / 8
                arco.y = charparado.y + charparado.height / 4
            else:
                arco = Sprite("GameImages\sarco22.png")
                #arco.set_position(100, janela.height - 87 - charparado.height / 2)
                arco.x = charparado.x - charparado.width / 8
                arco.y = charparado.y + charparado.height / 4

        # criando o tiro do arco
        if teclado.key_pressed("Z") and tempotranscorrido2 >=1 *dificuldade:
            tempotranscorrido2 = 0
            if viradopara == 1:
                flecha = Sprite("GameImages\sflecha1.png")
            elif viradopara == 2:
                flecha = Sprite("GameImages\sflecha2.png")
            flecha.y = arco.y + 40
            flecha.x = arco.x
            if viradopara ==1:
                flechas1 += [flecha]
            if viradopara ==2:
                flechas2 += [flecha]
        for flecha in flechas1:
            flecha.x += velflecha*janela.delta_time()
            if flecha.x >= janela.width:
                flechas1.pop(0)
        for flecha in flechas2:
            flecha.x -= velflecha*janela.delta_time()
            if flecha.x >= janela.width:
                flechas2.pop(0)

        # tiros dos inimigos
        inimigos.tempotranscorrido3 += janela.delta_time()
        inimigos.tirosinimigos(inimigoss,janela.width,tirosinimigos)
        for x in tirosinimigos:
            x.x -= 400*janela.delta_time()
            if x.x <= 0:
                tirosinimigos.remove(x)

        # BOSS FIGHT
        for x in tiroboss:
            if (x.collided(charparado)):
                tiroboss.pop(0)
                vida -= 1
        if vilao.x < 1200 and vilao.x > -1000:

            if win == 0:
                if vilao.y >= 150 and lock:
                    vilao.y -= vel_vilao*janela.delta_time()
                else:
                    vilao.y += vel_vilao*janela.delta_time()
                    lock = False
                    if vilao.y >= 500:
                        lock = True


            for x in flechas1:
                if (x.collided(vilao)) and vilao_life > 0:
                    flechas1.pop(0)
                    vilao_life -= 1

            for x in flechas2:
                if (x.collided(vilao)) and vilao_life > 0:
                    flechas2.pop(0)
                    vilao_life -= 1
            vilao.draw()

            if vilao_life <= 0 and explosion < 250:
                explosion += 1
                win = 1
                death_boss.draw()
                death_boss.update()
                vilao = Sprite("GameImages\sbranco.png")

            tempo_tiro_boss += 1
            if tempo_tiro_boss >= 100:
                tiro_boss = Sprite("GameImages\stiro_boss.png")
                tiro_boss.x = vilao.x
                tiro_boss.y = vilao.y + 100
                tiroboss += [tiro_boss]
                tempo_tiro_boss = 0
                if vilao.collided(charparado):
                    vida -= 1
            if win == 0:
                for y in tiroboss:
                    y.x -= 450*janela.delta_time()
                for x in tiroboss:
                    x.draw()

        if len(tiroboss) >= 1:
            if tiroboss[0].x <= (-1)*tiro_boss.width:
                tiroboss.pop(0)

        if win != 0 and ULTIMOTILE.x < 200:
            GameState = 5

        # pulo do personagem e gravidade
        charparado.y -= vely * janela.delta_time()
        chardireita.y -= vely * janela.delta_time()
        charesquerda.y -= vely * janela.delta_time()
        vely -= g * janela.delta_time()
        if charparado.y >= janela.height - 57 - charparado.height:
            charparado.y = janela.height - 57 - charparado.height
            chardireita.y = janela.height - 57 - charparado.height
            charesquerda.y = janela.height - 57 - charparado.height
            vely = 0
            g = 0
            huga = True
        if charparado.y <= 450 - 110:
            for x in layer1:
                if Collision.collided(charparado, x):
                    charparado.y = 450 - 110
                    chardireita.y = 450 - 110
                    charesquerda.y = 450 - 110
                    vely = 0
                    g = 0
                    huga = True
                if charparado.y == 450 - 110:
                    if not Collision.collided(charparado,x):
                        g = 1500
        if charparado.y <= layer2.y - 110:
            for x in layer2:
                if Collision.collided(charparado, x):
                    charparado.y = layer2.y - 110
                    chardireita.y = layer2.y - 110
                    charesquerda.y = layer2.y - 110
                    vely = 0
                    g = 0
                    huga = True
                if charparado.y == layer2.y - 110:
                    if not Collision.collided(charparado, x):
                        g = 1500

        if teclado.key_pressed("SPACE") and huga:
            huga = False
            vely = 800
            g = 1500

        # granadas dos inimigos
        for x in inimigoss2:
            if x.x <= janela.width:
                granada = Sprite("GameImages\granada.png")
                if x.get_curr_frame() == 2 :
                    granada.x = x.x + x.width - 30
                    granada.y = x.y + x.height - 30
                    granadas += [granada]
                    x.set_curr_frame(3)
        for x in granadas:
            x.x += velgranadax * janela.delta_time()
            x.y += velgranaday * janela.delta_time()


        # colisoes
        for x in tirosinimigos:
            if Collision.collided(x,charparado):
                tirosinimigos.remove(x)
                vida -= 1
        for x in flechas1:
            for y in inimigoss:
                if y.x <= janela.width:
                    if len(flechas1) > 0:
                        if Collision.collided_perfect(x,y):
                            inimigoss.remove(y)
                            flechas1.remove(x)
        for x in flechas2:
            for y in inimigoss:
                if y.x <= janela.width:
                    if len(flechas2) > 0:
                        if Collision.collided_perfect(x,y):
                            inimigoss.remove(y)
                            flechas2.remove(x)

        for x in granadas:
            if Collision.collided(charparado,x):
                explosao.set_position(x.x, x.y - explosao.height)
                explosao.unhide()
                explosao.set_curr_frame(0)
                explosao.play()
                granadas.remove(x)
                vida -= 1

            if x.y  >= 630:
                explosao.set_position(x.x, x.y - explosao.height)
                explosao.unhide()
                explosao.set_curr_frame(0)
                explosao.play()
                granadas.remove(x)

        if explosao.get_curr_frame() == 4:
            explosao.stop()
            explosao.hide()

        for x in fogos:
            if Collision.collided(x,charparado):
                fogos.remove(x)

        # vida
        if vida > 0:
            coracao = Sprite("GameImages\sheart%d.png" %vida)
        coracao.draw()





        arco.draw()
        for flecha in flechas1:
            flecha.draw()
        for flecha in flechas2:
            flecha.draw()
        for x in inimigoss:
            x.draw()
        for x in inimigoss2:
            x.draw()
            x.update()
        for x in tirosinimigos:
            x.draw()
        for x in granadas:
            x.draw()
        for x in fogos:
            x.draw()
            x.update()
        explosao.draw()
        explosao.update()
        if vilao_life > 0 and vilao.x < 1000:
            coracao_boss = Sprite("GameImages\sboss_life%d.png" %vilao_life)
            coracao_boss.set_position(700, 10)
            coracao_boss.draw()
        janela.draw_text("%d" % fps, 0, 0, 30, (255, 255, 255), "Arial", False, False)
        janela.update()

    while GameState == 5:
        GameImage("GameImages\sfinal.png").draw()
        if teclado.key_pressed("ESC"):
            janela.close()
        janela.update()
