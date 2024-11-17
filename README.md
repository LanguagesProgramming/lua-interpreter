# lua-interpreter
Lua interpreter made with Python using PLY (Python Lex-Yacc)

## Usage

```
python3 main.py
```
## Development

You can install nodemon to watch for changes on files and test new functionality. On a shell you can run
```sh
nodemon --exec python3 main.py
```

You may install nodemon by using `npm install -g nodemon`


## To test your `Lua` file

### Syntax
```sh
python3 -m tests.test_syntax <your_github_username> <your_lua_file>
```
e.g.
```sh
python3 -m tests.test_syntax brauliorivas sort.lua
```

