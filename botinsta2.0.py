import PySimpleGUI as psg
import mouse
import keyboard
import pygame
import botimage
import random
lay = [[psg.Text("comaçar?")],
[psg.Button("sim")], [psg.Button("não")]]
window = psg.Window(title="botinsta 2.0", layout=lay)
values = window.read()
botloop = True
text = ("se você gosta de frases motivacionais confira a bio ", "espero que seu dia seja incrivel", "se você gostou das frases não esqueça de conferir a bio")
if values[0]== "sim":
    pygame.time.Clock().tick(10)
    while botloop:
        if keyboard.is_pressed("esc"):
            botloop = False
        """xy_pos = mouse.get_position()
        print (xy_pos)"""
        botimage.imageminsta()
        pygame.time.delay(5000)
        mouse.move(663,737)
        pygame.time.delay(5000)
        mouse.click(mouse.LEFT)
        pygame.time.delay(5000)
        mouse.move(540,419)
        pygame.time.delay(5000)
        mouse.click(mouse.LEFT)
        pygame.time.delay(5000)
        mouse.move(501,452)
        pygame.time.delay(5000)
        mouse.click(mouse.LEFT)
        mouse.move(255,137)
        pygame.time.delay(5000)
        mouse.click(mouse.LEFT)
        pygame.time.delay(5000)
        mouse.move(492,443)
        pygame.time.delay(2000)
        mouse.click(mouse.LEFT)
        pygame.time.delay(2000)
        mouse.move(1302,95)
        pygame.time.delay(2000)
        mouse.click(mouse.LEFT)
        pygame.time.delay(2000)
        mouse.move(936,146)
        pygame.time.delay(2000)
        mouse.click(mouse.LEFT)
        pygame.time.delay(2000)
        keyboard.write(text[random.randint(0,2)],delay=0.25)
        pygame.time.delay(5000)
        keyboard.write(" #frasesinspiradoras", delay = 0.5)
        pygame.time.delay(1000)
        mouse.move(99,227)
        pygame.time.delay(1000)
        mouse.click(mouse.LEFT)
        pygame.time.delay(2000)
        keyboard.write(" #frasesparafotos", delay = 0.5)
        pygame.time.delay(2000)
        mouse.click(mouse.LEFT)
        pygame.time.delay(2000)
        keyboard.write(" #frasesreflexivas", delay = 0.5)
        pygame.time.delay(2000)
        mouse.click(mouse.LEFT)
        pygame.time.delay(5000)
        mouse.move(1302,95)
        pygame.time.delay(2000)
        mouse.click(mouse.LEFT)
