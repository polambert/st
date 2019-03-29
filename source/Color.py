
# A list of some good printable colors.

class Color:
    Reset   = "\033[0m"

    ## Colors
    Red     = "\033[31m"
    Green   = "\033[32m"
    Yellow  = "\033[33m"
    Blue    = "\033[34m"
    Magenta = "\033[35m"
    Purple  = "\033[35m"
    Cyan    = "\033[36m"
    White   = "\033[37m"

    ## Gray
    LightGray = "\033[37m"
    DarkGray  = "\033[90m"

    ## Light Colors
    LightRed     = "\033[91m"
    LightGreen   = "\033[92m"
    LightYellow  = "\033[93m"
    LightBlue    = "\033[94m"
    LightMagenta = "\033[95m"
    LightPurple  = "\033[95m"
    LightCyan    = "\033[96m"

    ## Style
    Bold          = "\033[1m"
    Italics       = "\033[3m"
    Underline     = "\033[4m"
    Inverse       = "\033[5m" # Reverses Foreground and Background colors
    Strikethrough = "\033[6m"

    ## Style Off
    BoldOff          = "\033[22m"
    ItalicsOff       = "\033[23m"
    UnderlineOff     = "\033[249m"
    InverseOff       = "\033[27m"
    StrikethroughOff = "\033[29m"

    class BG:
        Black   = "\033[40m"
        Red     = "\033[41m"
        Green   = "\033[42m"
        Yellow  = "\033[43m"
        Blue    = "\033[44m"
        Magenta = "\033[45m"
        Purple  = "\033[45m"
        Cyan    = "\033[46m"
        White   = "\033[47m"
