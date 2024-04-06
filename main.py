def main():
    word_list = []
    word_count = 0
    from collections import defaultdict
    character_dict = defaultdict(int)
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
#Creates the string (whole book)^
        word_list = file_contents.split()
        for word in word_list:
            word_count += 1
#Counts words^
            word_lower = word.lower()
            for char in word_lower:
                character_dict[char] += 1    
#Creates dict for character frequnecy (unsorted)^
        t_list = []
        for key, value  in character_dict.items():
            if str.isalpha(key) == True:
                tuple = (key, value)
                t_list.append(tuple)
            def sort_on(t_list):
                return t_list[1]
            
        t_list.sort(reverse=True, key=sort_on)
        print(f"--begin report of ./books/frankenstein.txt--")
        print(f"--{word_count} words found in document--")
        for t in t_list:
            print(f"The {t[0]} character appeared {t[1]} times.")
        print("--End report--")    

main()