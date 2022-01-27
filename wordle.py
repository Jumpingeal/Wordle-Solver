def purge(word: list):
    """
    Takes a list of strings and returns a list that only contains elements with
    - a length of 5
    - with only lowercase letters (to avoid nouns)
    """
    new_words = []
    for word in words:
        if len(word) == 5 and word.isalpha() and not any(char.isupper() for char in word):
            new_words += [word]
    return new_words

def exclude(char: str,word_list):
    """
    Takes a string as input and a list of strings (words) and returns a list containing
    - none of the characters in the inputted string
    """
    char = [c for c in char]
    new_words = []
    for word in word_list:
        i = 0
        contain_excluded = False
        while i < len(char) and not contain_excluded:
            if char[i] in word:
                contain_excluded = True
            i += 1
        if not contain_excluded:
            new_words += [word]
    return new_words

def exclude_position(char: str, index: list, word_list):
    """
    Takes a string as input, an index position an da list of strings (words) and returns a list containing
    - words that do not contain the inputted character in the given index position
    """
    new_words = []
    for word in word_list:
        i = 0
        contain_position = False
        while i < len(index) and not contain_position:
            if word[index[i]] == char:
                contain_position = True
            i += 1
        if not contain_position:
            new_words += [word]
    return new_words

def include_position(char: str, index:list, word_list):
    """
    Takes a string as input, an index position an da list of strings (words) and returns a list containing
    - words that do contain the inputted character in the given index position
    """
    new_words = []
    for word in word_list:
        i = 0
        contain_position = False
        while i < len(index) and not contain_position:
            if word[index[i]] != char:
                contain_position = True
            i += 1
        if not contain_position:
            new_words += [word]
    return new_words

def save(file_name: str,lst: list):
    """
    Takes a string and list of words as input and saves the list to a .txt file
    """
    with open(file_name,"w") as f:
        for word in lst:
            f.write(word + "\n")

def letter_distribution(words, print_d = True):
    """
    Takes as input a list of words, and returns the percentage frequency of each character across all words, 
    not counting duplicate characters in a single word
    """
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    frequency = [0 for _ in range(26)]
    total = 0
    for word in words:
        for i in range(len(word)):
            if word[i] not in word[:2]:
                frequency[ord(word[i]) - 97] += 1
                total += 1
    frequency1, letters1 = zip(*sorted(zip(frequency,letters),reverse=True))
    if print_d:
        for i in range(len(frequency)):
            print(f"{letters1[i]}: {round(frequency1[i]/total,4)}")

    return [round(frequency[i]/total,4) for i in range(26)]

def word_score(words,frequency):
    """
    Takes as input a list of words and a list of frequency's of each letter of the alphabet, and returns
    - a list representing the top 5 highest scoring words (not counting duplicate letters)
    """
    score = [0 for _ in range(len(words))]
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j] not in words[i][:j]:
                score[i] += frequency[ord(words[i][j]) - 97]

    score, words = zip(*sorted(zip(score,words),reverse=True))
    for i in range(min(5,len(words))):
        print(f"{words[i]}: {score[i]}")

def openf(file_name):
    """
    Reads a .txt file as to copy words into a list
    """
    with open(file_name) as f:
        words = f.readlines()
        for i in range(len(words)):
            words[i] = words[i][:-1]
    return words
            
if __name__ == "__main__":

    #alternative word lists
    #words = openf("words.txt")
    words = openf("wordlist.10000.txt")

    words = purge(words)
    words += ["mount"]
    frequency = letter_distribution(words,False)
    word_score(words,frequency)
    while True:
        print("Enter picked word: ",end="")
        letters = [c for c in input()]
        green_count = 0
        for i in range(5):
            print(f"What colour did you get for {letters[i]}? ", end ="")
            result = input().lower()
            if result == "b":
                words = exclude([letters[i]],words)
            elif result == "y":
                words = exclude_position(letters[i],[i],words)
            elif result == "g":
                words = include_position(letters[i],[i],words)
                green_count += 1
        if green_count == 5:
            print("YOU WON!!!!")
            break
        frequency = letter_distribution(words,False)
        word_score(words,frequency)
    
    
        
    
