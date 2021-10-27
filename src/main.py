import enc
import string

from pathlib import Path

def main():
    config = Path(Path.home(), ".frontear", "password.enc")
    if not config.parent.exists():
        config.parent.mkdir()

    with open(config, "wb+") as f:
        password = "test_password"
        f.write(e := enc.encrypt(string.printable, password))
        print(e)
        print()

        f.seek(0)
        print(d := enc.decrypt(f.read(), "test_password"))

        assert string.printable == d

if __name__ == "__main__":
    main()