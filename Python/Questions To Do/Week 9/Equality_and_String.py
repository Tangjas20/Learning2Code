class Item:
    def __init__(self, name, weight):
        pass
    
    def __eq__(self, other):
        # `__eq__` is an instance method, which also accepts
        # one other object as an argument.
        pass
    
    def __str__(self):
        # Note you have to RETURN a string here!
        pass

cat_1 = Item('Cat', 5)
cat_2 = Item('Cat', 5)
cat_1 == cat_2 # what does this evaluate to?

print(cat_1.__eq__(cat_2)) # should evaluate to True
print(cat_1 == cat_2) # should also evaluate to True

print(cat_1.__str__()) # Cat is 5 kg! 
print(str(cat_1)) # Cat is 5 kg! 
print(cat_1) # Cat is 5 kg!
