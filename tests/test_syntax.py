import sys
from tests_lib import validate_args

def run():
    arguments = sys.argv
    validate_args(arguments)

    gh_user = arguments[1]
    lua_file = arguments[2]



if __name__ == "__main__":
    run()
