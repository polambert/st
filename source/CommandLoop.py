
import os

from .Commands import *

## The Loop that manages input.
class CommandLoop:
    def Start():
        while True:
            cmd = input(":" + os.getcwd().split(os.sep)[-1] + "> ")

            if cmd[0] == ":":
                ## It's a bash command
                cmd = cmd[1:]
                os.system(cmd)
                continue

            if (cmd + " ").isspace():
                continue

            split = cmd.split(" ")

            arg = " ".join(split[1:])

            command = split[0]

            Commands.Run(command, arg)
