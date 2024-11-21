def main():
    # Pull Book from path
    book_path = "books/frankenstein.txt"
    # "Read" the book as a string
    text = get_book_text(book_path)
    # Get the counted number of words
    num_words = get_num_words(text)
    # Dictionarty of each character and their count
    chars_dict = get_chars_dict(text)
    # Pulls only alpha characters and sets them to lower case
    letters = get_alpha(text)
    # Gets the report for the final
    report = make_report(letters, chars_dict)

    # Prints the final report
    report_letter = report[0::2]
    report_count = report[1::2]

    for i in range(len(report_letter)):
        print(f"The '{report_letter[i]}' character was found {report_count[i]} times")

# Get the counted number of words 
def get_num_words(text):
    words = text.split()
    return len(words)

# Make dictionarty of each character and their count
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

# "Reads" the book and returns it as a string
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Pulls only alpha characters and sets them to lower case
def get_alpha(text):
    alpha = set()
    for c in text:
        lowered = c.lower()
        if lowered.isalpha() == True:
            alpha.add(lowered)
    alpha_sorted = sorted(alpha)
    return alpha_sorted

# Make a dictionary for the report
def make_report(key, dict):
    counted = []
    for i in range(len(key)):
        count = dict.get(key[i])
        counted.append(key[i])
        counted.append(count)
    return counted

main()
