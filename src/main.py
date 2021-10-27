import enc
import json

from pathlib import Path

def main():
    config = Path(Path.home(), ".frontear", "password.enc")
    if not config.parent.exists():
        config.parent.mkdir()

    with open(config, "wb+") as f:
        data = {
            "YouTube": [ # identifier
                "Frontear", # username
                "hunter2" # password
            ]
        }
        password = "test_password"

        f.write(enc.encrypt(json.dumps(data), password))

        f.seek(0)
        data = json.loads(enc.decrypt(f.read(), "test_password"))
        print(data["YouTube"])

if __name__ == "__main__":
    main()