with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    wordcount = 0 
    for word in words: 
        wordcount += 1 
    print(wordcount)