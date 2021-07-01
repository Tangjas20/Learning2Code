def find_consecutive(ls):

    indexer = 1
    while indexer < len(ls):
            if ls[indexer] - 1 == ls[indexer -1] or ls[indexer] -1 == ls[indexer+1]:
                return True
            elif ls[indexer] + 1 == ls[indexer -1] or ls[indexer] + 1 == ls[indexer+1]:
                return True
            else:
                indexer += 1
            return False

print(find_consecutive([1, 4, 7]))
print(find_consecutive([1, 2]))
print(find_consecutive([1, 2, 3, 4, 5]))

