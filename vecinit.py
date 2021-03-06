from collections import Counter # For counting features

from parser import parse, get_gram

def get_init_vec(train_file, tag_set):
    init_vec = {}
    gram_list = []

    with open(train_file, 'r', encoding = 'UTF-8') as f:
        line = f.readline() # Initial line

        while line != '':
            # Get features in a list
            temp = parse(line)[0]
            for i in range(len(temp)):
                gram_list.extend(get_gram(temp, i))

            line = f.readline()

    ctr = Counter(gram_list)

    # Add features to initial vector
    for elem in ctr:
        if ctr[elem] > 1:   # Only grams whose frequence > 1 can be added
            for tag in tag_set:
                init_vec[elem + '_' + tag] = 0

    return init_vec
