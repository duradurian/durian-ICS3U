"""
Author: Darrien Guan
Date: Oct 24
Discription: Calculates the average number of words per sentence in a text file.
"""

def word_count_average_length(sentence):
    '''Returns word count of string'''

    # Split the input sentence into words based on space.
    sentence = sentence.split(" ")
    new_sentence = []

    # Remove all strings that are empty.
    for item1 in range(len(sentence)):
        if sentence[item1] != "":
            new_sentence.append(sentence[item1])

    # Remove all non-alphabetical characters to prevent average character length per word logic errors.
    for i in range(len(new_sentence)):
        new_word = ""

        word = sentence[i]

        for item in range(len(word)):
            if word[item].isalpha():
                new_word += word[item]

        new_sentence[i] = new_word

    word_character_sum = 0

    # Calculate the total character count for all words in the cleaned sentence.
    for i in range(len(new_sentence)):
        word_character_sum += len(new_sentence[i])

    return len(new_sentence), (word_character_sum/len(new_sentence))

# This function reads a file and calculates the average words per sentence and average characters per word.
def average_word_per_sentence(file_name):
    '''calculates the average words per line and average characters per word'''

    word_count_sum = 0
    number_of_sentences = 0
    word_length_sum = 0

    # Open the file name
    with open(file_name, "r") as text:
        for sentence in text:
            number_of_sentences += 1

            # Call the word_count_average_length function to get word count and average word length for each sentence.
            statistics = word_count_average_length(sentence)

            # Update the total word count and total word length.
            word_count_sum += statistics[0]
            word_length_sum += statistics[1]

    # Returns average words per sentence, average characters per word.
    return (word_count_sum/number_of_sentences), word_length_sum/number_of_sentences

def main():
    '''main logic'''

    # Call average_word per sentence function.
    stats = average_word_per_sentence("textfile.txt")

    # Display results
    print("There are an average of %.2f per sentence and %.2f characters per word." % (stats[0], stats[1]))

main()