def check_file(str_len):
    with open("../output/src/testfile.txt") as f:
        z = f.read()
        if len(z) < int(str_len):
            raise ValueError("{} is not equal or over {}".format(len(z), str_len))
