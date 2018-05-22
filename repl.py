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
        print(e)
    else:
        if val is True:
            display.show(Image.HAPPY)
        elif val is False:
            display.show(Image.SAD)
        else:
            display.clear()
        if val is not None:
            print(repr(val))
