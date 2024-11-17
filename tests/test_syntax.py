import io
import sys
import os
from contextlib import redirect_stdout
from lua_interpreter.parser import parser
from .tests_lib import validate_args, get_date_time

def run():
    arguments = sys.argv
    validate_args(arguments)

    gh_user = arguments[1]
    log_filename = f"sintactico-{gh_user}-{get_date_time()}.txt"
    log_file_path = os.path.join(os.path.dirname(__file__), f"../logs/{log_filename}")

    lua_file = arguments[2]
    lua_file_path = os.path.join(os.path.dirname(__file__), f"../lua/{lua_file}")

    try:
        log_file = open(log_file_path, "w")
        lua_file = open(lua_file_path, "r")

        for line in lua_file:
            with io.StringIO() as stream:
                with redirect_stdout(stream):
                    parser.parse(line)

                s = stream.getvalue()
                log_file.write(f"[Lua] {line.strip()} [Parse Result] {s.strip()}\n\n")

        lua_file.close()
        log_file.close()
    except IOError as e:
        print(f"Error when opening lua file {e}")

if __name__ == "__main__":
    run()
