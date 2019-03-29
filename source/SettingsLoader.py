
## SettingsLoader
# This class can open a file and return a dictionary with the settings modified
def Settings(setting):
    try:
        return SettingsLoader.settings[setting]
    except:
        return False

class SettingsLoader:
    settings = {}

    def ReadFile(filename):
        file = open(filename, "r")

        ## Iterate through the file
        d = {}

        for line in file.readlines():
            if line[0] == "#":
                continue

            var = ""
            value = ""
            foundEquals = False
            for char in line:
                if char == "=":
                    foundEquals = True
                    var = var.strip()
                    continue

                if not foundEquals:
                    var += char
                else:
                    value += char

            value = value.strip()

            if value == "true":
                value = True
            if value == "false":
                value = False

            if not var.isspace():
                if value != "":
                    d[var] = value

        SettingsLoader.settings = d
        return d
