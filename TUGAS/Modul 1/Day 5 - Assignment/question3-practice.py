'''
## Question-3

You are given two lists `l1` and `l2` that represent two positive integers each. 
Each digit of the numbers is stored in reverse order, and each item represents one digit. 
Write a `add()` function to add the two numbers and return the sum as an inverted list.

l1 = [2, 4, 3]
l2 = [5, 6, 4]
add(l1, l2)

output:
[7, 0, 8]
'''

'''
342 + 465 = 807
807 dibalik 708
'''

def add(l1,l2):
    '''ini adalah fungsi add

    Args:
        l1 (list) : first number list to calculate
        l2 (list) : second number list to calculate

    Return:
        l3 (list) : number list result from sum of number in l1 and l2
    '''
    l1.reverse()
    l2.reverse()

    numbL1 = 0
    numbL2 = 0

    for i in range(len(l1)):
        val1 = l1[i] * 10**(len(l1)-1-i)
        numbL1 += val1

    for i in range(len(l2)):
        val2 = l2[i] * 10**(len(l2)-1-i)
        numbL2 += val2
    
    addNumb = numbL1 + numbL2
    addNumb = str(addNumb)

    l3 = []
    for i in addNumb:
        l3.append(int(i))

    l3.reverse()
    return l3


if __name__ == "__main__":
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

    output = add(l1,l2)
    print(output)