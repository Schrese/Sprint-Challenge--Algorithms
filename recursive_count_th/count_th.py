'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# RETHINKING 
# what if I instead think about the length of the word and use slices
def count_th(word, counter = 0):
    # initialize the counter at 0
    # counter = 0

    # if the length of the word is less than 2, then we can't have a "th", at most there could only ever be a "t". and if that's the case. we would just return the counter (this covers the case of when the word is at the end and when it doesn't start out with an empty string)
    if len(word) < 2:
        return counter

    # we need to increase the left side of the split each time the function is called, so that it keeps having new letters at the front of the list(string). 
    # if the first two letters don't equal "th", then we just continue recursing while increasing the left side of the slice
    if word[0:2] != "th":
        return count_th(word[1:])
    # if the first two letters equal "th", then we need to increase the counter and continue recursing while increasing the left side of the slice
    else:
        # counter += 1
        return 1 + count_th(word[1:])


    # return counter

# learned... look into things like incrementing counters recursively. 




# def count_th(word):
#     # print(len(word))
    
#     # create a 'counter' and store it
#     # counter = 0
#     print(counter)
#     # condition: if we have an empty string, return 0
#     if word == "":
#         return 0
#     # condition: if the letter is uppercase, don't include it
#     if word == "th" and word.islower():
#         counter += 1
#         return counter
#     # condition: if the letter "t" is followed by an "h", then increase the counter

#     # iterate through the word
#     else:
#         for i in range(len(word) - 1):
#             print(word[i] + word[i+1])
#             # if a "t" is found, then recurse with "word" being the "t" and the next letter
#             # if word[i] == "t":
#                 # print("hello")
#             return count_th(word[i] + word[i+1])
                
#             # otherwise just keep incrementing

#     # return the final count
#     return counter


    # pass
