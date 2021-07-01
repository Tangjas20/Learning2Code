from PERSON import Person
def test_1():
    p1 = Person('Homer Simpson',1982)
    assert p1.full_name == 'Homer Simpson', 'Test 1 failed'
    print('Test 1, Passed!')

if __name__ == "__main__":
    test_1()