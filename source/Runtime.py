
# Runtime
# The main entry program

from .Info import *
from .SettingsLoader import *
from .CommandLoop import *

class Runtime:
    def Run(settings):
        # <settings> is a dictionary with some useful program settings.
        print()
        print(" --- ST --- ")

        if Settings("printBattery"):
            Info.Battery.PrintInfo()
        if Settings("printCPU"):
            Info.Processor.PrintInfo()
        if Settings("printMemory"):
            Info.Memory.PrintInfo()
        if Settings("printDisk"):
            Info.Disk.PrintInfo()
        if Settings("printTime"):
            Info.Time.PrintInfo()
        if Settings("printProcessCount"):
            Info.Process.PrintInfo()

        print()

        CommandLoop.Start()
