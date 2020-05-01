import uinput
from io import open
import time
import re

file_with_songs="songs.txt"
file_with_settings="settings.txt"
default_settings = """\
Speed= 0.05
Prefix= -p"""

def writeKeyboard(to_write:str,writing_speed:float):
    events = (
        uinput.KEY_A,
        uinput.KEY_B,
        uinput.KEY_C,
        uinput.KEY_D,
        uinput.KEY_E,
        uinput.KEY_F,
        uinput.KEY_G,
        uinput.KEY_H,
        uinput.KEY_I,
        uinput.KEY_J,
        uinput.KEY_K,
        uinput.KEY_L,
        uinput.KEY_M,
        uinput.KEY_N,
        uinput.KEY_O,
        uinput.KEY_P,
        uinput.KEY_Q,
        uinput.KEY_R,
        uinput.KEY_S,
        uinput.KEY_T,
        uinput.KEY_U,
        uinput.KEY_V,
        uinput.KEY_W,
        uinput.KEY_X,
        uinput.KEY_Y,
        uinput.KEY_Z,
        uinput.KEY_ENTER,
        uinput.KEY_SPACE,
        uinput.KEY_KPMINUS,
        uinput.KEY_KPEQUAL
        )
    
    with uinput.Device(events) as device:
        translations = {" ":"space","\\":"enter","-":"kpminus","=":"kpequal"}
        for ch in to_write:
            time.sleep(writing_speed)
            if ch in translations.keys():
                ch = translations[ch]
                time.sleep(writing_speed*10)
            
            eval(f"device.emit_click(uinput.KEY_{ch.upper()})")

def filterEverySong(playlist:str):
    only_Alphabet = re.sub("[^a-zA-Z\n\s]+","", playlist)
    return only_Alphabet

def addThePrefix(filtered_songs:str,prefix:str):
    prefix = prefix.upper()
    output = re.sub("[\n]+",f"\n{prefix} ",filtered_songs)
    return str(prefix+" "+output)

def separateInLines(prefixed_songs:str):
    #Causes more process, but gain performance
    #decreasing use of writekeyboard
    final = prefixed_songs.split("\n")
    def __removeFinalSpace(iterable:list):
        return [i[:-1] if i[-1]==" " else i for i in iterable]
    return __removeFinalSpace(final)

def createNewFile(namefile:str,content:str=""):
    try:
        with open(namefile,"w",encoding="utf8") as f:
            f.seek(0)
            f.write(content)
            print("the file was created, you can edit the .txt file")
    except Exception as i:
        print(i)
        print("\ni cant create the file, do i have permissions ?")

def __openfile(namefile:str):
    with open(namefile,"r+",encoding="utf8") as f:
        return f.read()

def __firstConfigurations():
    files = {file_with_settings:str,file_with_songs:str}
    for k in files.keys():
        content = openOrMakeIt(k)
        files[k] = content
    return files

def openOrMakeIt(namefile:str):
    try:
        content = __openfile(namefile)
    except FileNotFoundError as e:
        print(f"i cant find {namefile} file")
        if namefile == file_with_settings:
            content = default_settings
        else:
            content = ""
        createNewFile(namefile,content)
    return content
    
def main():
    files = __firstConfigurations()
    
    settings = files[file_with_settings].split("\n")
    
    writing_speed = float(settings[0].replace("Speed= ",""))
    prefix        = settings[1].replace("Prefix= ","")
    
    song_list  = files[file_with_songs]
    validsongs = filterEverySong(song_list)
    full_text  = addThePrefix(validsongs,prefix)
    
    separated_commands = separateInLines(full_text)
    for i in separated_commands:
        writeKeyboard(i,writing_speed)
        writeKeyboard("\\",writing_speed)
        
if __name__ == "__main__":
    main()
