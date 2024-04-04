def main():
    word_list = []
    word_count = 0
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_list = file_contents.split()
        for i in word_list:
            word_count += 1
    print(word_count)
     
        

main()