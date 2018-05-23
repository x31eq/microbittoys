import music
from microbit import display, Image

while True:
    line = input('>>> ')
    if not line:
        continue
    try:
        val = eval(line)
    except EOFError:
        break
    except Exception as e:
        display.show(Image.CONFUSED)
        music.pitch(55, 1000, wait=False)
        print(e)
    else:
        if val is True:
            display.show(Image.HAPPY)
            music.pitch(528, 300, wait=False)
        elif val is False:
            display.show(Image.SAD)
            music.pitch(66, 1000, wait=False)
        else:
            display.clear()
        if val is not None:
            print(repr(val))
