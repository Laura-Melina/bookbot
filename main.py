
def get_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents
def count_words(file_contents):
    words = file_contents.split()
    wordcount = 0 
    for word in words: 
        wordcount += 1 
    print(wordcount)

def count_letters():
    text = get_text()
    text = text.lower()
    letter_dic = {}
    for i in text: 
        letter_dic[i] = 0   

    for i in text: 
        letter_dic[i] += 1 
    print(letter_dic)
count_letters()