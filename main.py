
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

def book_report():
    text = get_text()
    wordcount = count_words(text)
    letter_dic = count_letters()
    list_of_letters = list(letter_dic.items())
    list_of_letters_sorted = sorted(list_of_letters,key=lambda x: x[1], reverse=True)

    print("---Begin report of books/frankenstein.txt---")
    print(f"{wordcount} words found in the document")
    
    for i in range(len(list_of_letters_sorted)): 
        key,value = list_of_letters_sorted[i]
        if key.isalpha():
            print(f"The {key} character was found {value} times")
            
    print("--- end report")

book_report()



