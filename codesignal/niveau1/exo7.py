
def croissant(sequence) :
    verify= 0
    verify1= 0
    for v in(range(len(sequence)-1)):
        if sequence[v] >= sequence[v+1]:
            verify +=1
    for v in (range(len(sequence)-2)):
        if sequence[v] >=  sequence[v+2]:
            verify1 +=1
    return(True if verify < 2 and verify1<2 else False)
            



