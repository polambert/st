
import os
import psutil

from .Log import *
from .Info import *

## This is the file that includes all of the commands that can be called by
##  the user in ST.

class Commands:
    commands = {}

    def Run(command, arg):
        #try:
        Commands.commands[command](arg)
        ###except KeyError:
        #    print("  " + command + ": not found")
        #except Exception as e:
        #    print(" ERROR: " + str(e))

    def Init():
        Commands.commands["cpu"] = Commands.CommandList.cpu

        Commands.commands["livetime"] = Commands.CommandList.livetime
        Commands.commands["lt"] = Commands.CommandList.livetime

        Commands.commands["memory"] = Commands.CommandList.memory
        Commands.commands["mem"] = Commands.CommandList.memory

        Commands.commands["disk"] = Commands.CommandList.disk

        Commands.commands["cd"] = Commands.CommandList.cd

        Commands.commands["net"] = Commands.CommandList.network

    class CommandList:
        def cpu(arg):
            ## Remember that <arg> is a string containing all of the rest of
            ##  the command call.
            if arg != "":
                ## They passed arguments
                time = Info.Time.InterpretTime(arg) / 2

                percent = psutil.cpu_percent(interval=time)
                percents = psutil.cpu_percent(interval=time, percpu=2)

                percentsString = ""

                for i in percents:
                    percentsString += str(i) + "%, "

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

        def memory(arg):
            ## Fetch a detailed list of information on current memory
            v = psutil.virtual_memory()
            s = psutil.swap_memory()

            max = 13

            log(Color.LightMagenta + Color.Bold)
            print("  Virtual Memory:")
            log(Color.Reset)
            print("    Percent Used: " + str(v.percent) + "%")
            print("    Total:     " + str(v.total)     + ((13 - len(str(v.total))) * " ")     + " (" + str(v.total / 1048576) + " MiB)")
            print("    Used:      " + str(v.used)      + ((13 - len(str(v.used))) * " ")      + " (" + str(v.used / 1048576) + " MiB)")
            print("    Available: " + str(v.available) + ((13 - len(str(v.available))) * " ") + " (" + str(v.available / 1048576) + " MiB)")
            print("    Free:      " + str(v.free)      + ((13 - len(str(v.free))) * " ")      + " (" + str(v.free / 1048576) + " MiB)")
            print("    Active:    " + str(v.active)    + ((13 - len(str(v.active))) * " ")    + " (" + str(v.active / 1048576) + " MiB)")
            print("    Inactive:  " + str(v.inactive)  + ((13 - len(str(v.inactive))) * " ")  + " (" + str(v.inactive / 1048576) + " MiB)")
            print("    Buffers:   " + str(v.buffers)   + ((13 - len(str(v.buffers))) * " ")   + " (" + str(v.buffers / 1048576) + " MiB)")
            print("    Cached:    " + str(v.cached)    + ((13 - len(str(v.cached))) * " ")    + " (" + str(v.cached / 1048576) + " MiB)")
            print("    Shared:    " + str(v.shared)    + ((13 - len(str(v.shared))) * " ")    + " (" + str(v.shared / 1048576) + " MiB)")

            log(Color.LightCyan + Color.Bold)
            print("  Swap Memory:")
            log(Color.Reset)
            print("    Percent Used: " + str(s.percent) + "%")
            print("    Total:    " + str(s.total) + ((13 - len(str(s.total))) * " ") + " (" + str(s.total / 1048576) + " MiB)")
            print("    Used:     " + str(s.used)  + ((13 - len(str(s.used))) * " ")  + " (" + str(s.used / 1048576)  + " MiB)")
            print("    Free:     " + str(s.free)  + ((13 - len(str(s.free))) * " ")  + " (" + str(s.free / 1048576)  + " MiB)")
            print("    S IN:     " + str(s.sin)   + ((13 - len(str(s.sin))) * " ")   + " (" + str(s.sin / 1048576)   + " MiB)")
            print("    S OUT:    " + str(s.sout)  + ((13 - len(str(s.sout))) * " ")  + " (" + str(s.sout / 1048576)  + " MiB)")

        def disk(arg):
            drive = "/"

            if arg != "":
                ## They passed some information
                if os.path.exists(arg):
                    drive = arg
                elif arg == "ls":
                    ## List all partitions
                    parts = psutil.disk_partitions()
                    for part in parts:
                        log(Color.LightMagenta)
                        log("  Partition: " + part.device)
                        print(Color.Reset)
                        print("    Mounted At %9s" % (part.mountpoint))
                        print("    FS          %9s" % (part.fstype))
                        print("    Options     %9s" % (part.opts))
                        return
                else:
                    log(Color.LightRed)
                    log(" Error: Folder not found. Check your working directory.")
                    print(Color.Reset)
                    return

            log(Color.LightGreen + Color.Bold)
            log("  Disk: " + drive)
            print(Color.Reset)

            d = psutil.disk_usage(drive)

            log(Color.LightGreen)
            print("   Percent Used: " + str(d.percent) + "%")
            log(Color.Reset)
            print("    Total %15i b   (%i GiB)" % (d.total, d.total / 1073741824))
            print("    Used  %15i b   (%i GiB)" % (d.used, d.used / 1073741824))
            print("    Free  %15i b   (%i GiB)" % (d.free, d.free / 1073741824))

        def cd(arg):
            os.chdir(arg)

        def livetime(arg):
            import time

            while True:
                log("  " + Info.Time.GetTime(Settings("time_live")))
                log("\r")
                time.sleep(1)

        def network(arg):
            counters = psutil.net_io_counters(pernic=True)

            for c in counters.keys():
                log(Color.LightMagenta)
                log("  " + c)
                print(Color.Reset)
                print(Color.Magenta + "    Bytes Sent    " + Color.LightMagenta + "%-13i" % (counters[c].bytes_sent))
                print(Color.Magenta + "    Bytes Recv    " + Color.LightMagenta + "%-13i" % (counters[c].bytes_recv))
                print(Color.Magenta + "    Packets Sent  " + Color.LightMagenta + "%-13i" % (counters[c].packets_sent))
                print(Color.Magenta + "    Packets Recv  " + Color.LightMagenta + "%-13i" % (counters[c].packets_recv))
                log(Color.Reset)
