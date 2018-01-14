# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import re

D1_NAME = "data/d1.txt"
D2_NAME = "data/d2.txt"

def open_file(f_name):
    with open(f_name, 'r') as f:
        return f.read()

D1 = open_file(D1_NAME)
D2 = open_file(D2_NAME)

def dot_product(d1, d2):
    """ Given two vectors d1, d2 (which are dictionaries),
    find the dot product of the two vectors."""
    
    # dot product over words on both list; longer one will
    # have the chance to enumerate all words.
    longer = max(d1, d2)
    shorter = min(d1, d2)

    total = 0
    for word, count in longer.iteritems():
        total += longer[word] * shorter.get(word, 0)
    return total

def arccos(d1, d2):
    """ Calculate the arccos of the two documents vectors. The document
    distance's scale is normalized by finding acrcos. The document
    distance is the angle between the vectors. 0 degree means the two
    documents are identical while 90 degrees mean the docuemnts share
    no common words. To calculate the arccos we need to find the dot 
    products of the two two document vectors. """

    product = dot_product(d1, d2)
    return int(product/(len(d1)*len(d2)))

def naive_approach():
    """
    The naive approach is to split the document into words using regex.
    Then count the occurence for each word in the list and the word
    is the key of the occurence dictionary and the occurence frequency
    is the value. We then calculate the document distance of d1 and d2.
    """

    def wordize(text):
        r = re.compile("\w+")
        return r.findall(text)
    
    def count(d_list):
        count_dict = {}
        for index, word in enumerate(d_list):
            if word in count_dict:
                count_dict[word] += 1
            else:
                count_dict[word] = 1
        return count_dict

    d1_word_list = wordize(D1)
    d2_word_list = wordize(D2)

    d1_counts = count(d1_word_list)
    d2_counts = count(d2_word_list)
    
    distance = arccos(d1_counts, d2_counts)
    return int(distance)

if __name__ == "__main__":
    print("Starting the program.")
    print(naive_approach())
