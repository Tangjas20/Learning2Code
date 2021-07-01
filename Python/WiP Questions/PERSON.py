class Person:
    counter = 0
    current_year = 2020
    is_christmas = False
    def __init__(self, full_name, year):
        Person.counter += 1
        self.id = Person.counter
        self.full_name = full_name
        self.year = year

        if isinstance(full_name, str):
            name_counter = full_name.split(" ")
            if len(name_counter) >= 2:
                self.full_name = full_name
            else:
                self.full_name = "Guy Incognito"
        else: 
            self.full_name = "Guy Incognito"

        if type(year) != int:
            self.year = 2000
        elif year < 1:
            self.year = 2000
        else:
            self.year = year

if __name__ == "__main__":
    p1 = Person('Homer SImpson',1982)
    print(Person.counter)
    print('{}: {}, {}'.format(p1.id, p1.full_name, p1.year))
    
    p2 = Person('Jason', 0)
    print(Person.counter)
    print('{}: {}, {}'.format(p2.id, p2.full_name, p2.year))

