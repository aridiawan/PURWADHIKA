'''
## Question-4

You are given a non-overlapping list `l1` where `l1[i] = [start_i, end_i]` 
represents the start and end of the i-th interval and the intervals are sorted in ascending order based on i. 
You are also given an list `l2 = [start, end]` that represents the start and end of another interval. 
Write a `func()` function to insert `l2` into `l1` so that `l1` are still sorted in ascending order 
and do not overlap (merge overlapping intervals if necessary).

l1 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]] 
l2 = [4, 8]
func(l1, l2)

output:
[[1, 2], [3, 10], [12, 16]]
'''

def func(l1,l2):
    '''ini adalah fungsi add

    Args:
        l1 (list) : list of sublist that contains stars and end number to calculate
        l2 (list) : list of start and end number

    Return:
        l3 (list) : new list of l2 in l1
    '''
    l3 = []
    for i in l2:
        if l2.index(i) == 0:
            for j in l1:
                if i >= j[0] and i <= j[1]:
                    l3.append(j[0])
                    break
        else:
            for k in l1:
                if i >= k[0] and i <= k[1]:
                    l3.append(k[1])
                    break
    return l3

if __name__ == "__main__":

    l1 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]] 
    l2 = [4, 8]

    output = func(l1,l2)
    print(output)