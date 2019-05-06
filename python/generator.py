import sys
import random
import string


def main():
    X = 18
    with open("testfile.txt", "w") as f:
        # Just some comment to get a commit
        f.write(''.join(random.choice(string.ascii_letters) for x in range(X)))


if __name__ == "__main__":
    main()