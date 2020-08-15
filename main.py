import keyboard as kb
import json
import time
default_settings = """{
    "Speed": "0.05",
    "Prefix": "-p" 
}"""
print(default_settings)


fh = open('songs.txt')

songs = [line.rstrip() for line in fh.readlines()]

fh.close()

try:
    f = open("settings.json", "r")
except FileNotFoundError:
    print("Settings.json no existe!")
    exit()
settings = json.load(f)

if float(settings["Speed"]) < 0.05 or float(settings["Speed"]) > 0.5:
    print("Configuracion invalida, usando parametros por defecto")
    print("Esperando 5 secs para que entres al discord")
    time.sleep(7) # pongo 7 por si acaso :D
    for i in songs:
        kb.write(settings["Prefix"])
        kb.press("space")
        for a in i:
            time.sleep(0.05)
            kb.press(a)
        kb.press("enter")
    
    exit(0)



time_per_key = float(settings["Speed"])
print("Esperando 5 secs para que entres al discord")
time.sleep(7) # pongo 7 por si acaso :D
for i in songs:
    kb.write(settings["Prefix"])
    kb.press("space")
    for a in i:
        time.sleep(time_per_key)
        kb.press(a)
    kb.press("enter")