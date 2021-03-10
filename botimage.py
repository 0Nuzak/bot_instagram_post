from PIL import Image, ImageDraw, ImageFont
from bttxt import textr
from saves import out_file
import random
def imageminsta():
    w = 720
    img = Image.new("RGBA", [w,w], (255,255,255,255))
    ra = random.randint(0,255)
    ga = random.randint(0,255)
    ba = random.randint(0,255)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    a = random.randint(0,255)
    fnt = ImageFont.truetype("botinsta2.0/input/fragment_core/Fragmentcore.otf",40)
    txt = textr()
    for x in range(w):
        for y in range(w):
            if y<= 160 or y >= 560:
                    img.putpixel((x,y),(ra,ga,ba,200))
    for x in range(w):
        for y in range(w):
            if y<= 20 or y>= 700:
                img.putpixel((x,y),(r,g,b,a))
            elif x<= 20 or x>= 700:
                img.putpixel((x,y),(r,g,b,a))
    d = ImageDraw.Draw(img)
    d.text((300,300), "{}".format(txt), font=fnt, fill=(0,0,0,255),anchor="ms")
    img.save(out_file("instimagem.png"))