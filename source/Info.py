
import time
import datetime

import psutil

from .Color import *
from .Log import log
from .SettingsLoader import *

class Info:
    class Battery:
        def PrintInfo():
            ## First, make sure a battery is installed.
            battery = psutil.sensors_battery()

            if battery == None:
                return None

            percent = round(battery.percent, 2)
            timeLeft = battery.secsleft / 60 # Convert to minutes left
            charging = battery.power_plugged

            ## Determine the color to use based on battery percentage.
            color = Color.LightGreen
            if percent < 50:
                color = Color.LightYellow
            if percent < 25:
                color = Color.LightRed

            if charging and Settings("battery_greenIfCharging"):
                color = LightGreen

            ## Calculate simplified time left
            hours = timeLeft // 60
            minutes = round(timeLeft % 60)

            log(color)
            log("  Battery: ")
            log(str(percent) + "% ")
            if not charging:
                log("(" + (str(hours) + "h ") * (hours != 0) + str(minutes) + "m)")
            else:
                log("(Charging)")
            print(Color.Reset)

    class Memory:
        def PrintInfo():
            memory = psutil.virtual_memory()

            total = memory.total
            percent = memory.percent
            used = memory.used

            # Divide by 1 billion, since it's in bytes.
            totalGigs = total / 1000000000
            usedGigs = used / 1000000000

            ## Determine the color to use based on memory percentage.
            color = Color.LightGreen
            if percent > 65:
                color = Color.LightYellow
            if percent > 90:
                color = Color.LightRed

            usedString = str(round(usedGigs, 2)) + "G / " + str(round(totalGigs, 2)) + "G"

            log(color)
            log("  Memory: ")
            log(str(percent) + "% ")
            log("(" + usedString + ")")
            print(Color.Reset)

    class Disk:
        def PrintInfo(drive="/"):
            disk = psutil.disk_usage(drive)

            total = disk.total
            used = disk.used
            free = disk.free
            percent = disk.percent

            ## Determine the color to use based on disk percentage.
            color = Color.LightGreen
            if percent > 75:
                color = Color.LightYellow
            if percent > 95:
                color = Color.LightRed

            totalGigs = total / 1000000000
            usedGigs = used / 1000000000

            usedString = str(round(usedGigs, 2)) + "G / " + str(round(totalGigs, 2)) + "G"

            log(color)
            log("  Disk: ")
            log(str(percent) + "% ")
            log("(" + usedString + ")")
            print(Color.Reset)

    class Process:
        def PrintInfo():
            pidcount = Info.Process.GetProcessCount()

            log("  Processes: ")
            log(pidcount)
            print()

        def GetProcessCount():
            return len(psutil.pids())
        
        def ListPIDs():
            pids = psutil.pids()

            for pid in pids:
                log("%-7s" % pid)
                try:
                    log(" %20s" % (psutil.Process(pid).exe()))
                except:
                    log(" %20s" % " PD1")
                try:
                    log("   %s" % (psutil.Process(pid).name()))
                except:
                    log("   PD2")
                print()

        def ListPIDInfo(pid):
            # <pid> must be an int.
            p = psutil.Process(pid)
            print("  " + str(pid))
            print("    " + p.exe() + p.name())
            print("    " + " ".join(p.cmdline()))
            print("    Children:")

            children = p.children(recursive=True)
            for child in children:
                print("      %7i %-10s %8s" % (child.pid, child.name, child.started))



    class Time:
        def PrintInfo():
            time = Info.Time.GetTime(Settings("time_boot"))

            log(Color.LightBlue)
            log("  Time: ")
            log(Color.Bold)
            log(time)
            log(Color.BoldOff)
            print(Color.Reset)

        def GetTime(strf=""):
            if strf == "":
                return datetime.datetime.now()
            return datetime.datetime.now().strftime(strf)

        ## UTS - Unix TimeStamp
        def GetUTS():
            return round(time.time())

        def GetAccurateUTS():
            return time.time()

        ## A TimeText is a simple format for durations.
        # Example: 10d 2h 3m 45s
        # Value returned is in seconds.
        def InterpretTime(text):
            total = 0

            cap = ""

            for i in text:
                if i in "0123456789":
                    cap += i
                elif i.isspace():
                    pass
                elif i == "d":
                    total += int(cap) * 24 * 60 * 60
                elif i == "h":
                    total += int(cap) * 60 * 60
                elif i == "m":
                    total += int(cap) * 60

            total += int(cap)

            return total

    class Processor:
        def PrintInfo():
            # Divide by 2 because we're testing twice
            time = Info.Time.InterpretTime(Settings("cpu_defaultTestTime")) / 2

            percent = psutil.cpu_percent(interval=time)

            percents = psutil.cpu_percent(interval=time, percpu=True)

            percentsString = ""

            for i in percents:
                percentsString += str(i) + ", "

            percentsString = percentsString[:-2]

            ## Determine color based on CPU usage.
            color = Color.LightGreen
            if percent > 60:
                color = Color.Yellow
            if percent > 90:
                color = Color.Red

            log(color)
            log("  CPU: ")
            log(str(percent) + "% ")
            log("[" + percentsString + "]")
            print(Color.Reset)
