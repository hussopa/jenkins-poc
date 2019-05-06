def check_file(str_len):
    with open("../python/testfile.txt") as f:
        z = f.read()
        if len(z) != int(str_len):
            raise ValueError("{} is not {}".format(len(z), str_len))
