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
        sorted = []
        sorting_list = []
        for key in character_dict:
            if str.isalpha(key) == True:
                mini_dict = {}
                mini_dict[key] = character_dict[key]
                sorting_list.append(mini_dict)
        sorted = sorting_list.sort()
        print(sorted)


#Need to select for only alphabet characters + order them in a list
            
#Use str.isalpha() to deliver boolean check for alphabet chars

#Use dict keys in loop to create list of dicts for each dict unit

#Create print() message using f-strings to present each list value in a text-message
    
    #print(file_contents)

    
    #print(word_count)   
    
    
    #print(character_dict)
    

main()