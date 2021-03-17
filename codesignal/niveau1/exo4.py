def adjacentElementsProduct(inputArray):
    product = -1000
    for i in range(len(inputArray)-1):
        if  inputArray[i]*inputArray[i+1] > product:
        product = inputArray[i]*inputArray[i+1] 
    return product
