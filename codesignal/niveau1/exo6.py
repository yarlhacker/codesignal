def makeArrayConsecutive2(statues):
    statues.sort()
    number_of_occurrences = 0
    for v in range(len(statues)-1):
        if statues[v]+1 != statues[v+1]:
            number_of_occurrences += (statues[v+1])-(statues[v]+1)
    return number_of_occurrences
