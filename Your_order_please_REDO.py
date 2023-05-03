"""
https://www.codewars.com/kata/55c45be3b2079eccff00010f

"""
# Time complexity - at least O(n^2) a double for loop since it iterates of the list and the over each word in the list
# Space complexity is lineear O(n) because of the new list and dictionary.

"""
def order(sentence):
    if sentence.strip() == "":
        return ""
    else:
        result = []
        new_dict = {}
        for word in sentence.split():
            for char in word:
                if char.isdigit():
                    new_dict[char] = word
        for key, value in sorted(new_dict.items()):
            result.append(value)
        return ' '.join(result)
"""


# Time complexity - better than quadratic, probably linear logarithmic because of the use of
# the sorted() function  on line 42
# Space complexity is linear O(n) because of the new lists and dictionaries.
def order(sentence):
    if sentence.strip() == "":
        return ""
    else:
        ex_order = []
        word_dict = {}
        for char in sentence:
            if char.isnumeric():
                ex_order.append(char)

        word_list= sentence.split()
        for i in range(len(word_list)):
            word_dict[ex_order[i]] = word_list[i]
        
        sorted_dict =  dict(sorted(word_dict.items()))
        new_list = []
        for value in sorted_dict.values():
            new_list.append(value)

        return ' '.join(new_list)

