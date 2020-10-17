GameImage("GameImages\menubg.png").draw()
janela.draw_text("Salve a Amazonia dos franceses!", 250, 500, 30, (255, 255, 255), "Arial", False, False)
janela.draw_text("Aperte espaco para pular, Z para atirar e mova-se com as setas direcionais", 30, 525, 30, (255, 255, 255), "Arial", False, False)
if teclado.key_pressed("ESC"):
    GameState = 0
janela.update()