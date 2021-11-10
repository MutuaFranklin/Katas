import itertools
from collections import Counter

sentence =(input("Enter a sentence: "))
list = sentence.split(' ')


result = Counter(itertools.chain(list))
print(list)
print(result)



# method 2

# def occurrence(sentence):
#     list = sentence.split(' ')

#     for(i=1; i <= len(list); i++):
#         print(ehhed)

      






