def writer(filename, lines):
    if type(filename) != str:
        raise TypeError
    try: 
        f = open(filename, 'a')
    except FileNotFoundError:
        raise FileNotFoundError("Yes")
    if type(lines) != list:
        raise TypeError

    for i in lines:
        if type(i) != str:
            raise ValueError("Cannot write non-string value to file")
    for i in lines:
        f.write(i+"\n")
        print('')

writer("testfile.txt", ["5", "yes", "good"])
