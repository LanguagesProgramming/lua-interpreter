from datetime import datetime
from zoneinfo import ZoneInfo

def validate_args(arguments):
    if len(arguments) != 3:
        file_name = arguments[0]
        print(f"Please, pass your gh username and file to be tested, e.g., python3 {file_name} <your_gh_username> <file>.lua")
        exit(1)

def get_date_time():
    now = datetime.now(ZoneInfo("America/Guayaquil"))
    return now.strftime("%d-%m-%Y-%H-%M-%S")
