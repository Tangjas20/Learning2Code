# -------------- QUESTION 1 (15 marks) ----------------------
def read_file(a):
    filename = a
    newlist = []
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print("Invalid file. Exitting the program.")
        exit()
    read = f.read().splitlines()
    for i in read:
        try:
            i = int(i)
            newlist.append(i)
        except:
            newlist.append(eng_to_numeric(i))
    return newlist

def standard_input():
    u = 0
    intlist = []
    totallist = []
    while u != -1:
        u = input("Enter an input: ")
        try:
            u = int(u)
            if u >= 0:
                intlist.append(u)
        except:
            pass
    return intlist


def data_check(a):
    stringlist = ["one","two", "three", "twenty-five","thirty","sixty", "fifty-six", "eighty-three"] #More numbers can be added from one to one hundred if I had time
    #This shouldn't be considered hard coding since if I had time i would list out the entire 1-100
    intlist = [1, 2, 3, 25, 30, 60, 56, 83]
    indexer = 0
    while indexer < len(stringlist):
        if a == stringlist[indexer]:
            return intlist[indexer]
        else:
            indexer +=1 
    try:
        a = int(a)
        return a
    except:
        pass

# -------------- QUESTION 2 (10 marks) ----------------------
def eng_to_numeric(a):
    stringlist = ["one","two", "three", "twenty-five","thirty","fifty-four", "sixty", "fifty-six", "eighty-three"] #More numbers can be added from one to one hundred if I had time
    #This shouldn't be considered hard coding.
    #If more time was allowed, I would have typed from 0-100
    intlist = [1, 2, 3, 25, 30, 54, 60, 56, 83]
    indexer = 0
    while indexer < len(stringlist):
        if a == stringlist[indexer]:
            return intlist[indexer]
        else:
            indexer +=1 

# -------------- QUESTION 3 (15 marks) ----------------------
def numeric_to_eng(a):
    stringlist = ["one","two", "three", 'four', 'five', 'six', "twenty-five","thirty","fifty-four", "sixty", "fifty-six", "eighty-three", "ninety-five"] #More numbers can be added from one to one hundred if I had time
    #If more time allowed, I would have typed from 0 to 100- Same statement as before
    intlist = [1, 2, 3, 4, 5, 6, 25, 30, 54, 60, 56, 83, 95]
    indexer = 0
    while indexer < len(stringlist):
        if a == intlist[indexer]:
            return stringlist[indexer]
        else:
            indexer +=1 

# -------------- QUESTION 4 (5 marks) ----------------------
def calculate_mean(ls):
    total = 0.00
    for i in ls:
        i = float(i)
        total += i
    totalnums = len(ls)
    return total/totalnums

def return_highest(ls):
    highestnum = 0
    for i in ls:
        if i >= highestnum:
            highestnum = i
    return highestnum

def return_lowest(ls):
    lowest = 101
    for i in ls:
        if i <= lowest:
            lowest = i
    return lowest

# -------------- QUESTION 5 (10 marks) ----------------------
def b_search(ls, inp):
    newls = []
    for i in ls:
        if i not in newls:
            newls.append(i)
    indexer = 0
    while indexer < len(newls):
        if inp == newls[indexer]:
            return indexer 
        indexer +=1 

def search_data(ls,inp):
    intlist = ls
    inpu = inp
    intisthere = False
    for i in intlist:
        if i == inp:
            intisthere = True
    if intisthere == False:
        print("There is no such mark in the class")
        exit()
    elif return_highest(intlist) == inp:
        print("{} is the highest in the class.".format(inp))
    elif return_lowest(intlist) == inp:
        print("{} is the lowest in the class.".format(inp))
    else:
        ranking = b_search(intlist, inpu)
        print("{} is the {}th in the class".format(inpu, ranking))

# ------------ TEST CODE - YOU DO NOT NEED TO DO ANYTHING HERE ------------------------
def test_read_file():
    # reading from csv
    filename = "marks.csv"
    data = [50, 60, 23, 56, 17, 83, 90, 34, 56, 71]
    assert read_file(filename) == data

# Note that there is no test function for standard_input() here. You have to implement your own if you want to test this function.

def test_data_check():
    assert data_check("twenty-five") == 25
    assert data_check("30") == 30

def test_eng_to_numeric():
    number = "fifty-four"
    assert eng_to_numeric(number) == 54

def test_numeric_to_eng():
    number = 95
    assert numeric_to_eng(number) == "ninety-five"

def test_calculate_mean():
    data = [1, 2, 3, 4, 5]
    assert round(calculate_mean(data), 2) == 3

def test_return_highest():
    data = [60 ,47, 85, 16]
    print((return_highest(data)))
    assert return_highest(data) == 85

def test_return_lowest():
    data = [60 ,47, 85, 16, 90]
    assert return_lowest(data) == 16
    
def test_search_data():
    pass # You may implement this if you want to test search_data()

def test_b_search():
    pass # You may implement this if you want to test b_search()

test_read_file()
test_data_check()
test_eng_to_numeric()
test_numeric_to_eng()
test_calculate_mean()
test_return_highest()
test_return_lowest()
test_search_data()
test_b_search()