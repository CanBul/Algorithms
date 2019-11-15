# Finding the rank of the number in the given reversed sorted list

def binary_rank_search(mylist, number):
    length = len(mylist)
    middle = length//2
    left = mylist[0:middle]
    right = mylist[middle:]

    if mylist[middle] == number:
        return middle+1
    elif length==1 and number>mylist[middle]:
        return middle+1
    elif length==1 and number<mylist[middle]:
        return middle+2

    elif mylist[middle]> number:
        return middle+binary_rank_search(right,number)

    else:
        return binary_rank_search(left,number)
