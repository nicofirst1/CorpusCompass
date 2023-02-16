class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def error(text, *args):
     print( bcolors.FAIL + text + bcolors.ENDC, *args)

def warning(text, *args):
     print(bcolors.WARNING + text + bcolors.ENDC, *args)

def ok(text, *args):
     print( bcolors.OKGREEN + text + bcolors.ENDC   , *args)

def info(text, *args):
     print( bcolors.OKBLUE + text + bcolors.ENDC, *args)

def color_print(text, color):
    if color == "error":
        print(error(text))
    elif color == "warning":
        print(warning(text))
    elif color == "ok":
        print(ok(text))
    elif color == "info":
        print(info(text))

