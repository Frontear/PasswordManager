import enc
import json
import pathlib

"""
{
    "YouTube": {
        "username": "Frontear",
        "password": "hunter2"
    }
}
"""
DATA = {}
PASSWORD = None
FILE = pathlib.Path(pathlib.Path.home(), ".frontear", "password.enc")

def add(identifier: str, username: str, password: str) -> bool:
    if identifier in DATA:
        return False

    DATA[identifier] = {
        "username": username,
        "password": password
    }

    return True

def remove(identifier: str) -> bool:
    if identifier not in DATA:
        return False

    del DATA[identifier]

    return True

def save():
    if not (parent := FILE.parent).exists():
        parent.mkdir()

    with open(FILE, "w") as f:
        content = enc.encrypt(json.dumps(DATA), PASSWORD)
        f.write(content)

def load(password: str) -> bool:
    global PASSWORD

    if not FILE.exists():
        PASSWORD = password
        return True

    with open(FILE, "rb") as f:
        try:
            data = enc.decrypt(f.read(), password)
        except InterruptedError:
            return False

        PASSWORD = password
        DATA.update(json.loads(data))