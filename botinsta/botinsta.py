from instabot import Bot, API
from botimage import imageminsta
import PySimpleGUI as sg
bot = Bot()
layout = [[sg.Text("username:")],
[sg.Input()],
[sg.Text("password:")],
[sg.Input()],
[sg.Button("loggin")]]
window = sg.Window("teste", layout)
event , values = window.read()
user = values[0]
passw = values[1]
bot.login(username=user,  password= passw)
instaloop = True
while instaloop:
    layout = [[sg.Text("sair?")],
    [sg.Button("quit")],
    [sg.Text("stories?")],
    [sg.Button("stories!")],
    [sg.Text("post?")],
    [sg.Button("post!")]]
    window = sg.Window("fundionando", layout)
    values = window.read()
    if values[0] == "quit":
        instaloop = False
    else:
        imageminsta()
        if values[0] == "stories!":
            bot.upload_story_photo("D:/projetos/botinsta2.0/output/instimagem.png")
        else:
            bot.upload_photo("D:/projetos/botinsta2.0/output/instimagem.png")
    bot.reset_cache()
bot.logout()