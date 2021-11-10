products = ['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat',
           'pinkHat', 'blackShirt','yellowShirt', 'greenPants', 'greenPants']

import itertools
from collections import Counter



def featured(products):

    occurrence = Counter(itertools.chain(products))
    print(occurrence)

    most_purchased= max(occurrence, key=occurrence.get)
    return most_purchased
result = featured(products)

print(result)


