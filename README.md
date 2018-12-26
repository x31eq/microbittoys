## Command-line toys for BBC micro:bit

These are command-line Python scripts you can flash to a BBC micro:bit
and amuse a four year old.  They're based on a REPL with sum support
for speech synthesis.

The good one is "saysums.py".  It shows the chessboard pattern and when
you enter a line from the serial prompt, it reads it back, calculates
it as a Python expression, and reads the answer.  It also shows
different icons depending on the result.  If you press button A and
return from the command line, it switches to a simpler mode where it
doesn't try to evaluate Python and simply reads whatever you type in.
There's a stick figure icon for this mode.

There's also "repl.py", which is a bit simpler and I don't remember
much about.

To hear the speech, connect you audio device between pin 0 and GND.
There's a good croc-clip headphone adapter for this.

To set up the software, if you've forgotten how to flash Python to
your micro:bit, get a Python 3 virtualenv or something and

> ``pip install uflash``
> ``pip install microfs``
> ``uflash saysums.py /media/sdb``

It might not work with /media/sdb an you get a message saying

> ``Flashing Python to: /dev/sdb/micropython.hex``
> ``Error flashing saysums.py to ['/dev/sdb']: [Errno 20] Not a directory: '/dev/sdb/micropython.hex'``

In that case, try mounting with your operating system and use the path
it gives you.

I use picocom with this alias for the serial connection:

> ``picocom --baud=115200 /dev/ttyACM0``
