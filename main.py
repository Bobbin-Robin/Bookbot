def main():
    word_list = []
    word_count = 0
    from collections import defaultdict
    character_dict = defaultdict(int)
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_list = file_contents.split()
        for word in word_list:
            word_count += 1
            word_lower = word.lower()
            for char in word_lower:
                character_dict[char] += 1    
                
    pass
    print(word_count)

    pass
    print(file_contents)   

    
    print(character_dict)



main()