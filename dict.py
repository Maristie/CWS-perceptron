from parser import parse

def get_gram(line, index):
    i = index
    length = len(line)
    gram_set = set()

    # Get unigrams and bigrams with position information
    # p for previous, m for middle, n for next
    gram_set.add(line[i] + '_m')
    if i == 0 and i + 1 < length:
        gram_set |= {line[i + 1] + '_n', line[i:i + 2] + '_mn'}
    elif i == length - 1:
        gram_set |= {line[i - 1] + '_p', line[i - 1:i + 1] + '_pm'}
    else:
        gram_set |= {line[i + 1] + '_n', line[i:i + 2] + '_mn',
                     line[i - 1] + '_p', line[i - 1:i + 1] + '_pm',
                     line[i - 1] + line[i + 1] + '_pn'}

    return gram_set

# Add feature from a sentence to the dictionary
def add_feat(line, dict, tag_set):
    line_gram_set = set()

    for i in range(len(line)):
        line_gram_set |= get_gram(line, i)

    for elem in line_gram_set:
        for tag in tag_set:
            feat = elem + '_' + tag
            if feat not in dict:
                dict_len = len(dict)
                dict[feat] = dict_len

# Get dictionary
def get_dict(train_file, tag_set):
    dict = {}

    with open(train_file, 'r', encoding = 'UTF-8') as f:
        lines = f.readlines()

    for line in lines:
        add_feat(parse(line)[0], dict, tag_set)

    return dict
