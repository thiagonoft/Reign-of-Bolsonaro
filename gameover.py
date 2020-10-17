GameImage("GameImages\GameOver.png").draw()
if reviver > 0:
    janela.draw_text("Aperte R para voltar no tempo com o Totem Ancestral e tentar novamente.", 0, 0, 30, (255, 255, 255), "Arial", False, False)
    janela.draw_text("Cuidado! So pode ser usado uma unica vez!", 0, 30, 30, (255, 255, 255), "Arial", False, False)
    if teclado.key_pressed("R"):
        vida = 3
        reviver -= 1
        GameState = 1
if teclado.key_pressed("ESC"):
    janela.close()
janela.update()
