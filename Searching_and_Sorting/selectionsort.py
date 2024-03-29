# Explaination of the code will be published soon
# in first inner loop the max value will be found
# and even less items will be sorted out
# the question comes but when 
def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
                
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

"""
      OUTPUT
[17, 20, 26, 31, 44, 54, 55, 77, 93]

      EXPLAINATION
fillslot = 9 - 1 = 8

      TIME COMPLEXITY
O(n2)
"""

