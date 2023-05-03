"""
https://www.codewars.com/kata/5679aa472b8f57fb8c000047

"""


# Time complexity - at least O(n^2) w/ sum() inside a for loop / Space complexity - O(1) because
# no new variables were instantiated. vvvvvvvvvvvvvvvvvvvvv

#def find_even_index(arr):

"""
    for index, num in enumerate(arr):
        if  sum(arr[index:]) == sum(arr[:index+1]):
            return index
        else:
            continue
    return -1
""" 
# Time complexity -  O(n) for loop and sum outside of for loop / Space complexity - O(n) because
# of the new variables...vvvvvvvvvvvvvvvvvvv

def find_even_index(arr):
    leftsum = sum(arr[:0]) 
    rightsum = sum(arr[0:])
    for index, num in enumerate(arr):
        rightsum -= arr[index]
        if  rightsum == leftsum:
             return index
        leftsum += num
    return -1

print(find_even_index([1,2,3,4,3,2,1]))




