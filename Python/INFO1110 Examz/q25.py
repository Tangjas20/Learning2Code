def find_pair(n):
    newlist = []
    indexer = 0
    indexer2 = 0
    while indexer < len(n):
        if n[indexer] in newlist:
            for i in newlist:
                if i == n[indexer]:
                    j=indexer2
                else:
                    indexer2 += 1
            index1 = indexer2
            index2 = indexer
            newls = [index1,index2]
            tupl = tuple(newls)
            return tupl
        else:
            newlist.append(n[indexer])
            indexer += 1
    return (-1,-1)

print(find_pair([1, 2, 4, 4]))


