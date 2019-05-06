import sys
import random
import string


def main():
    X = 20
    with open("testfile.txt", "w") as f:
        f.write(''.join(random.choice(string.ascii_letters) for x in range(X)))


if __name__ == "__main__":
    main()