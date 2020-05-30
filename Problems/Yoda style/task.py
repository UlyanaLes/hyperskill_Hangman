from random import seed, shuffle

# your sentence is assigned to the variable
sentence = input().split()

# write your python code below
seed(43)
shuffle(sentence)

# shows the message
print(' '.join(sentence))
