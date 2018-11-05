import re


def normalize_and_split_text(text):
    text = text.lower()

    list_of_unpretty_things = [',', '.', '(', ')', '?', '!', '"', '*']

    for thing in list_of_unpretty_things:
        text = text.replace(thing, '')

    return text.split()


def count_first_person_pronouns(text):
    # SOURCE: https://stackoverflow.com/questions/14921436/python-finding-word-frequencies-of-list-of-words-in-text-file
    singular_pronouns = ['I', 'Me', 'My']
    return normalize_and_split_text(text).count(singular_pronouns)


def count_words(text):
    dict_of_words = dict()
    text = normalize_and_split_text(text)

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

    text = normalize_and_split_text(text)

    print("\nAverage number of words per sentence in the given text: " + str(len(text) / len(sentences)))


def male_or_female(text):
    # SOURCE: https://www.really-learn-english.com/list-of-pronouns.html

    list_of_pronouns = ['I', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them', 'I', 'you', 'he',
                        'she', 'it', 'we', 'they', 'what', 'who', 'me', 'him', 'her', 'it', 'us', 'you', 'them', 'whom',
                        'mine', 'yours', 'his', 'hers', 'ours', 'theirs', 'this', 'that', 'these', 'those', 'who',
                        'whom', 'which', 'what', 'whose', 'whoever', 'whatever', 'whichever', 'whomever', 'who', 'whom',
                        'whose', 'which', 'that', 'what', 'whatever', 'whoever', 'whomever', 'whichever', 'myself',
                        'yourself', 'himself', 'herself', 'itself', 'ourselves', 'themselves', 'myself', 'yourself',
                        'himself', 'herself', 'itself', 'ourselves', 'themselves', 'anything', 'everybody', 'another',
                        'each', 'few', 'many', 'none', 'some', 'all', 'any', 'anybody', 'anyone', 'everyone',
                        'everything', 'nobody', 'nothing', 'none', 'other', 'others', 'several', 'somebody', 'someone',
                        'something', 'most', 'enough', 'little', 'more', 'both', 'either', 'neither', 'one', 'much',
                        'such'
                        ]

    # this exercise is super relative, as we don't have access to any meaningful data, but let's throw in some numbers
    # first, according to the article in the exercise, females use about 85'000 more first person prounous per year
    # according to this (https://www.quora.com/How-many-words-do-we-use-on-an-average-day), we speak about 16'000 words a day
    # means, an "average" person speaks about 5'840'000 words per year

    # according to this source (https://english.stackexchange.com/questions/55486/what-are-the-percentages-of-the-parts-of-speech-in-english),
    # roughly 38 percent of the english language in a normal conversation are pronouns
    # means, 2'219'200 of those 5mio. yearly worlds are pronouns

    # let's assume that a female person speaks an additional 85'000 pronouns on top of those 2 Mio. pronouns
    # means male use 2'219'200 pronouns per year, female 2'304'200
    # break it down to percent, conversations of male are consisting of 38% pronouns, while female peak at 39.4 percent

    # if you want to test the script the best, grab an ebook over at project gutenberg in the text file format
    # copy the downloaded text file to this folder
    #  and insert the following line at the end of the file
    # male_or_female(open("name_of_your_text_file", "r").read())
    # after this, execute the script with either "py 4.py" or "python3 4.py"
    # you can test btw any other function as well with this input
    # just replace the "male_or_female" with the function you want to test

    number_of_pronouns_in_text = 0
    text = normalize_and_split_text(text)

    for pronoun in list_of_pronouns:
        number_of_pronouns_in_text += text.count(pronoun)

    print(number_of_pronouns_in_text)

    percentage_of_pronouns = number_of_pronouns_in_text / len(text)

    if percentage_of_pronouns < 0.38:
        print("This text could be from a male because less than 38% of this text are pronouns.")
    elif 0.38 < percentage_of_pronouns < 0.394:
        print(
            "This text could be either from a male or a female because the percentage of pronouns is between 38% and 39.4%")
    else:
        print("This text could be from a female because less than 38% of this text are pronouns.")

    print("Amount of pronouns: " + str(number_of_pronouns_in_text))
    print("Amount of words: " + str(len(text)))
    print("Percentage of pronouns: " + str(round(percentage_of_pronouns * 100, 2)))


count_words(open("4_example_text.txt", "r").read())
