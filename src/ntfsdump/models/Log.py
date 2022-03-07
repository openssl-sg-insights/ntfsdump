# coding: utf-8
from pathlib import Path
from traceback import format_exc
from datetime import datetime

from ntfsdump import get_program_name, get_version

def get_datetime() -> datetime:
    return datetime.utcnow()

def get_strdatetime() -> str:
    return get_datetime().strftime('%Y%m%d_%H%M%S_%f')


class Log(object):
    def __init__(self, path: Path = Path('.', f"{get_program_name()}_{get_strdatetime()}.log"), is_quiet: bool = False):
        self.path = path
        self.is_quiet = is_quiet
        self.__create_logfile()

    def __create_logfile(self):
        self.path.write_text(f"- {get_program_name()} v{get_version()} - \n")
            
    def __write_to_log(self, message: str):
        try:
            with self.path.open('a') as f:
                f.write(f"{get_datetime().isoformat()}: {message}\n")
        except Exception as e:
            self.print_danger(format_exc())

    def print_info(self, message):
        print(f"\033[36m{message}\033[0m")

    def print_danger(self, message):
        print(f"\033[31m{message}\033[0m")
    
    def log(self, message: str):
        self.__write_to_log(message)
        if not self.is_quiet:
           self.print_info(message) 
