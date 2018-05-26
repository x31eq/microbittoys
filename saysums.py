import sys
import speech
from microbit import display, Image, sleep

def sayrepr():
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
            sys.print_exception(e)
            speech.say("I don't understand")
        else:
            if val is not None:
                print(str(val))
                speech.say(line)
            if val is True:
                display.show(Image.HAPPY)
                sleep(100)
                speech.say("is right")
            elif val is False:
                display.show(Image.SAD)
                sleep(100)
                speech.say("is false")
            elif isinstance(val, int):
                speech.say("equals")
                speech.say(str(val))
                display.clear()
            else:
                display.clear()


if __name__ == '__main__':
    sayrepr()
