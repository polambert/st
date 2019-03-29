
from .Commands import *

## The Loop that manages input.
class CommandLoop:
    def Start():
        while True:
            cmd = input(":> ")
            if cmd.isspace():
                continue

            split = cmd.split(" ")

            arg = " ".join(split[1:])

            command = split[0]

            Commands.Run(command, arg)
