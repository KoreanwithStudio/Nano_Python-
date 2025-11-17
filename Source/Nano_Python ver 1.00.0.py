#THIS is the source code
#Which is python code

import time
import os
import ast
import math

def safe_eval(expr, variables):
    allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
    allowed_names.update(variables)

    node = ast.parse(expr, mode="eval")

    def _eval(n):
        if isinstance(n, ast.Expression):
            return _eval(n.body)
        if isinstance(n, ast.Constant):  # Python 3.8+
            return n.value
        if isinstance(n, ast.Num):  # legacy
            return n.n
        if isinstance(n, ast.BinOp):
            left = _eval(n.left)
            right = _eval(n.right)
            if isinstance(n.op, ast.Add):
                return left + right
            if isinstance(n.op, ast.Sub):
                return left - right
            if isinstance(n.op, ast.Mult):
                return left * right
            if isinstance(n.op, ast.Div):
                return left / right
            if isinstance(n.op, ast.Mod):
                return left % right
            if isinstance(n.op, ast.Pow):
                return left ** right
            if isinstance(n.op, ast.FloorDiv):
                return left // right
            raise ValueError("Unsupported binary operator")
        if isinstance(n, ast.UnaryOp):
            val = _eval(n.operand)
            if isinstance(n.op, ast.UAdd):
                return +val
            if isinstance(n.op, ast.USub):
                return -val
            raise ValueError("Unsupported unary operator")
        if isinstance(n, ast.Call):
            if isinstance(n.func, ast.Name) and n.func.id in allowed_names:
                func = allowed_names[n.func.id]
                args = [_eval(a) for a in n.args]
                return func(*args)
            raise ValueError("Call to disallowed function")
        if isinstance(n, ast.Name):
            if n.id in allowed_names:
                return allowed_names[n.id]
            raise NameError(f"Unknown name: {n.id}")
        raise ValueError("Unsupported expression element: " + str(type(n)))

    return _eval(node)

vars_store = {}

print("NANO_Python — Type --help for a list of commands.")

while True:
    try:
        a = input("NANO_Python/> ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting NANO_Python...")
        break

    if not a:
        continue

    if a == "cls":
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    if a == "--ver":
        print("NANO_Python version 1.1.2 beta 2025-11-17")
        continue

    if a == "--help":
        print("Available commands: --ver, --help, P, math, vars, time, exit, Kor")
        print("vars usage: 'vars set NAME VALUE', 'vars get NAME', 'vars list', 'vars del NAME'")
        continue

    if a == "P":
        b = input("/> ")
        print(b)
        continue

    if a == "math":
        expr = input("/> ").strip()
        try:
            result = safe_eval(expr, vars_store)
            print(result)
        except Exception as e:
            print("Invalid expression:", e)
        continue

    if a.startswith("vars"):
        parts = a.split()
        if len(parts) == 1:
            print("Variable storage - usage: 'vars set NAME VALUE', 'vars get NAME', 'vars list', 'vars del NAME'")
            continue
        cmd = parts[1]
        if cmd == "set" and len(parts) >= 4:
            name = parts[2]
            value_expr = " ".join(parts[3:])
            try:
                value = safe_eval(value_expr, vars_store)
            except Exception:
                # fallback: store as raw string if cannot eval
                value = value_expr
            vars_store[name] = value
            print(f"Set {name} = {value}")
        elif cmd == "get" and len(parts) == 3:
            name = parts[2]
            print(vars_store.get(name, f"{name} not found"))
        elif cmd == "list":
            if vars_store:
                for k, v in vars_store.items():
                    print(f"{k} = {v}")
            else:
                print("No variables stored.")
        elif cmd == "del" and len(parts) == 3:
            name = parts[2]
            if name in vars_store:
                del vars_store[name]
                print(f"Deleted {name}")
            else:
                print(f"{name} not found")
        else:
            print("Invalid vars command. Use --help for usage.")
        continue

    if a == "time":
        print(time.strftime("%Y-%m-%d %H:%M:%S"))
        continue

    if a == "exit":
        print("Exiting NANO_Python...")
        break

    if a == "Kor":
        print("안녕하세요! 현재 NANO_Python은 한국어를 온전하게 지원하지 않습니다. 추후 지원할 예정입니다. 죄송합니다.")
        continue

    print("Unknown command. Type --help for a list of commands.")
import os

print("Nano_Python" \
" Type --help for a list of commands.")

while True:
    a = input("NANO_Python/>")
    if a == "cls":
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    if a == "--ver":
        print("NANO_Python version 1.0.0")
    elif a == "--help":
        print("Available commands: --ver, --help, P, math, vars, time, exit")
    elif a == "P":
        b = input('/>')
        print(b)
    elif a == "math":
        try:
            expr = input('/> ')
            result = eval(expr)
            print(result)
        except:
            print("Invalid expression")
    elif a == "vars":
        print("Variable storage - type 'set' to add, 'get' to retrieve")
    elif a == "time":
        print(time.strftime("%Y-%m-%d %H:%M:%S"))
    elif a == "exit":
        print("Exiting NANO_Python...")
        break
    elif a == "Kor":
        print("안녕하세요! 지금 나노 파이썬 버전은 한국어를 지원하지않습니다. 나중에 지원할 예정입니다.^^" \
        "죄송합니다.")
    else:
        print("Unknown command. Type --help for a list of commands.")

