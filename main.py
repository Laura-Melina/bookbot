
def get_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents
def count_words(file_contents):
    words = file_contents.split()
    wordcount = 0 
    for word in words: 
        wordcount += 1 
    return wordcount

def count_letters():
    text = get_text()
    text = text.lower()
    letter_dic = {}
    for i in text: 
        letter_dic[i] = 0   

    for i in text: 
        letter_dic[i] += 1 
    return letter_dic

def book_report(wordcount,letter_dic):
    print("---Begin report of books/frankenstein.txt---")
    print(f"{wordcount} words found in the document")
    for char in letter_dic: 
        count = letter_dic[char]
        print(f"The {char} character was found {count} times")
    print("--- end report")




