from datetime import datetime
from colorama import Fore, Back, Style

loggingDestination = "textlog.txt"

def writeoutLog(message, status, logFile):
    timenow = datetime.now()
    current_time = timenow.strftime("%m-%d-%Y | %I:%M:%S %p")
    file = open(logFile, 'a')
    match status:
        case "info":
            print(f"{Fore.BLUE}[INFO][{current_time}] - {message}{Style.RESET_ALL}")
            file.write(f"[INFO][{current_time}] - {message}" + '\n')
        case "success":
            print(f"{Fore.GREEN}[SUCCESS][{current_time}] - {message}{Style.RESET_ALL}")
            file.write(f"[SUCCESS][{current_time}] - {message}" + '\n')
        case "error":
            print(f"{Fore.RED}[ERROR][{current_time}] - {message}{Style.RESET_ALL}")
            file.write(f"[ERROR][{current_time}] - {message}" + '\n')
        case "warning":
            print(f"{Fore.YELLOW}[WARNING][{current_time}] - {message}{Style.RESET_ALL}")
            file.write(f"[WARNING][{current_time}] - {message}" + '\n')
        case _:
            print(f"{Fore.WHITE}[UNKNOWN][{current_time}] - {message}{Style.RESET_ALL}")
            file.write(f"[UNKNOWN][{current_time}] - {message}" + '\n')
    file.close