import re


def count_first_person_pronouns(text):
    # SOURCE: https://stackoverflow.com/questions/14921436/python-finding-word-frequencies-of-list-of-words-in-text-file
    singular_pronouns = ['I', 'Me', 'My']
    text = text.lower().split()
    return text.count(singular_pronouns)


def count_words(text):
    dict_of_words = dict()
    text = text.lower()
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.split()

    for word in text:
        try:
            dict_of_words[word] += 1
        except KeyError:
            dict_of_words.update({word: 1})

    for key, value in dict_of_words.items():
        print("Occasions of word " + key + " in text: " + str(value))


def count_average_words_per_sentence(text):
    # SOURCE: https://stackoverflow.com/a/4998688
    sentences = re.split('[.?!]', text)
    sentences = list(filter(None, sentences))

    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.split()

    print("\nAverage number of words per sentence in the given text: " + str(len(text) / len(sentences)))

# TODO implement the gender detection after reading those websites:
# http://www.yalescientific.org/2012/03/the-secret-life-of-pronouns/
# http://www.hackerfactor.com/GenderGuesser.php
