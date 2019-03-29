
import os

## This is the file that includes all of the commands that can be called by
##  the user in ST.

class Commands:
    commands = {}

    def Run(command, arg):
        try:
            commands[command](arg)
        except:
            print("  " + command + ": not found")

    def Init():
        global commands
        commands = {}
        commands["cpu"] = Commands.CommandList.cpu

    class CommandList:
        def cpu(arg):
            ## Remember that <arg> is a string containing all of the rest of
            ##  the command call.
            print("CPU CALL: " + arg)
