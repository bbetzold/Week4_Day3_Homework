"""
https://www.codewars.com/kata/57fafb6d2b5314c839000195
"""


# Time complexity - at least O(n^2) a for loop with the built-in function count() inside
# Space complexity is lineear O(n) because of the new list

"""

def remove(s):
    copy_list = s.split()
    new_string = ""
    for word in copy_list:
        if word.count('!') != 1:
            new_string += word + " "    
    return new_string.strip()
"""

#count variable to track which word it is on
#split to make a copy of the words as a list
#count variable to track how many exclamation points have been traversed over the current word
#a list to save the indices of words to delete

# Time complexity - Linear
# Space complexity is lineear O(n) because of the new lists and variables

def remove(s):
    copy_list = s.split()
    punct_count = 0
    word_index = 0
    new_list= []

    for char in s:
        if char == "!":
            punct_count += 1
        elif char == " " and punct_count == 1:
            punct_count = 0
            word_index += 1
        elif char == " " and punct_count != 1:
            punct_count = 0
            new_list.append(copy_list[word_index])
            word_index += 1
        else:
            continue
    
    return " ".join(new_list) if new_list != [] else ""

print(remove("Hi! Hi!! Hi!"))