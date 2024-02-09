import string


def letter_count(file):
    """Counts letters in a text file and returns a dictionary of the letter:count pair"""
    dict_letters = dict()  # creating dictionary to hold letter:count

    f = open(file)  # reading inputted file & counting letters & inputting the counts into dictionary
    for line in f:  # iterate through every line of the file
        for ch in line:  # read through each char
            ch.lower()  # converts all char to lowercase
            if ch in string.ascii_lowercase:  # letters are counted & stored in dictionary
                if ch in dict_letters:  # if char is in dict then increase it by 1
                    dict_letters[ch] += 1
                else:  # else start it at 1
                    dict_letters[ch] = 1
    f.close()  # close the file

    # print(dict_letters)
    return dict_letters  # return the dictionary


def letter_frequency(dict_letters):
    """Finds frequency of each letter in a dictionary and returns a dictionary of letter:frequency pairs"""
    dict_freq = dict_letters  # duplicating inputted dictionary

    total_ch = 0  # counting total characters
    for value in dict_freq.values():  # iterates through the values in the freq dict
        total_ch += value  # sums total value

    for key, value in dict_freq.items():  # calculating frequency of each letter & inputting into dictionary
        dict_freq[key] = (value / total_ch)

    # print(dict_freq)
    return dict_freq  # return the dictionary


# run assertion test on letter_count(file)
expected_count = {'i': 17, 'r': 13, 'e': 23, 'a': 12, 'n': 9, 'd': 10,
                  'c': 6, 'o': 20, 'm': 3, 's': 12, 'y': 3, 't': 19,
                  'h': 12, 'w': 8, 'l': 6, 'f': 9, 'v': 2, 'u': 5, 'p': 1,
                  'k': 2, 'g': 2, 'b': 1}
actual_count = letter_count('frost.txt')
assert (expected_count == actual_count)

# run assertion test on letter_frequency(dict)
expected_freq = {'i': 0.08717948717948718, 'r': 0.06666666666666667,
                 'e': 0.11794871794871795, 'a': 0.06153846153846154,
                 'n': 0.046153846153846156, 'd': 0.05128205128205128,
                 'c': 0.03076923076923077, 'o': 0.10256410256410256,
                 'm': 0.015384615384615385, 's': 0.06153846153846154,
                 'y': 0.015384615384615385, 't': 0.09743589743589744,
                 'h': 0.06153846153846154, 'w': 0.041025641025641026,
                 'l': 0.03076923076923077, 'f': 0.046153846153846156,
                 'v': 0.010256410256410256, 'u': 0.02564102564102564,
                 'p': 0.005128205128205128, 'k': 0.010256410256410256,
                 'g': 0.010256410256410256, 'b': 0.005128205128205128}
actual_freq = letter_frequency(letter_count('frost.txt'))
assert (expected_freq == expected_freq)
