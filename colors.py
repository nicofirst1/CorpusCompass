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


def error(text):
     return bcolors.FAIL + text + bcolors.ENDC

def warning(text):
     return bcolors.WARNING + text + bcolors.ENDC

def ok(text):
     return bcolors.OKGREEN + text + bcolors.ENDC

def info(text):
     return bcolors.OKBLUE + text + bcolors.ENDC

def color_print(text, color):
    if color == "error":
        print(error(text))
    elif color == "warning":
        print(warning(text))
    elif color == "ok":
        print(ok(text))
    elif color == "info":
        print(info(text))

