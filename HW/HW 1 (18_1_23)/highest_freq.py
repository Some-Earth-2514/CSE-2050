from letters import letter_count
from letters import letter_frequency


def highest_freq(file):
    """Find the letter with the highest frequency and returns the letter & frequency"""

    my_dict = letter_frequency(letter_count(file))  # creating a dictionary holding letters:frequency

    # finding the highest letter:freq pair
    max_letter = ""
    max_freq = 0.0

    # iterates through key and value in the dict and find out which key:value is the highest
    for key, value in my_dict.items():
        if value > max_freq:
            max_freq = value
            max_letter = key

    # create a tuple to store highest frequency letter
    highest_pair = (max_letter, max_freq)

    # return tuple
    return highest_pair


# running assertion test on highest_file(file)
expected_pair = ('e', 0.11794871794871795)
actual_pair = highest_freq('frost.txt')
assert (expected_pair == actual_pair)

highest_freq('frost.txt')
