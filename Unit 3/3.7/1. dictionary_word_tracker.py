"""
Author: Darrien Guan
Date: October 26, 2023
Discription: Program keeps a count of the occurance of each word using dictionary in a textfile.
"""

def clean_sentence(sentence):
    '''removes all punctuation in sentence and returns as list'''

    # remove all /n
    sentence = (sentence.replace('\n', "")).lower()

    new_sentence_string = ""
    new_sentence_list = []

    # only let alphabetical characters 
    for i in range(len(sentence)):
        if sentence[i].isalpha() or sentence[i] == " ":
            new_sentence_string += sentence[i]

    # make new list using new senentence 
    new_sentence_string = new_sentence_string.split(" ")

    # Remove all blank spaces in new list.
    for i in range(len(new_sentence_string)):
        if new_sentence_string[i] != "":
            new_sentence_list.append(new_sentence_string[i])

    return new_sentence_list

def main():
    '''main logic'''

    # Word dictionary for words in text file
    word_dict = {}

    # Open text file
    with open("textfile.txt", "r") as file:
        for sentence in file:

            # Call clean_sentence to convert sentence into clean list.
            sentence_list = clean_sentence(sentence)

            # Ignore all blank lines.
            if sentence_list != []:

                # Checks every word in list
                for i in range(len(sentence_list)):

                    # If word already in dict, +1 to count, else, new word is added with a count of 1
                    if sentence_list[i] not in word_dict:
                        word_dict[sentence_list[i]] = 1
                    
                    else:
                        new_total = word_dict[sentence_list[i]] + 1
                        word_dict[sentence_list[i]] = new_total

    # dictionary to list
    word_dict_list = list(word_dict)

    # Write textfile in format word: count
    with open("report.txt", "w") as report:
        for i in range(len(word_dict_list)):
            report.write(f"{word_dict_list[i]}: {word_dict[word_dict_list[i]]}\n")

main()