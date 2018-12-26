import sys
import speech
from microbit import display, Image, sleep, button_a


numbers = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        }


def sayrepr():
    while True:
        display.show(Image.CHESSBOARD)
        while not button_a.was_pressed():
            command()
        display.show(Image.STICKFIGURE)
        while not button_a.was_pressed():
            line = input('? ')
            if line:
                speech.say(line)


def command():
    line = input('>>> ')
    if not line:
        return
    try:
        val = eval(line)
    except Exception as e:
        display.show(Image.CONFUSED)
        sys.print_exception(e)
        speech.say("I don't understand")
    else:
        if val is True:
            display.show(Image.HAPPY)
        elif val is False:
            display.show(Image.NO)
        elif isinstance(val, int):
            display.show(Image.CHESSBOARD)

        if val is not None:
            print(str(val))
            speech.say(line)
        if val is True:
            sleep(100)
            speech.say("is right")
        elif val is False:
            sleep(100)
            speech.say("is false")
        elif isinstance(val, int):
            speech.say("equals")
            speech.say(numbers.get(val, str(val)))


if __name__ == '__main__':
    sayrepr()
