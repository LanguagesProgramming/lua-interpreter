import sys
import os
from tests_lib import validate_args
from src.parser import parser

def run():
    arguments = sys.argv
    validate_args(arguments)

    gh_user = arguments[1]
    log_filename = f"sintactico-{gh_user}.txt"
    log_file_path = os.path.join(os.path.dirname(__file__), f"../logs/{log_filename}")

    lua_file = arguments[2]
    lua_file_path = os.path.join(os.path.dirname(__file__), f"../lua/{lua_file}")

    try:
        with open(lua_file_path, "r") as lua_file:
            print(parser)
    except IOError as e:
        print(f"Error when opening lua file {e}")

if __name__ == "__main__":
    run()
