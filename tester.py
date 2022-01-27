from wordle import *
import random

if __name__ == "__main__":
    all_words = purge(openf("wordlist.10000.txt"))
    
    words = all_words.copy()

    frequency = letter_distribution(words,False)
    guessed_word = word_score(words,frequency,False)[0]
    
    guess_count = 1
    #get random 5 letter word
    correct_word = words[random.randint(0,len(words) - 1)]
    print("Word to guess: " + correct_word)
    
    #while word hasn't been guess
    while guessed_word != correct_word:
        print(f"Guess {guess_count}: " + guessed_word)
        #for every character in guessed_word
        for i in range(len(guessed_word)):
            #if character is in correct and in position
            if guessed_word[i] == correct_word[i]:
                words = include_position(guessed_word[i],[i],words)
            #if character is in correct word
            elif guessed_word[i] in correct_word:
                words = exclude_position(guessed_word[i],[i],words)
            #otherwise exclude
            else:
                words = exclude([guessed_word[i]],words)
        frequency = letter_distribution(words,False)
        guessed_word = word_score(words,frequency,False)[0]
        guess_count += 1
    print(f"Guess {guess_count}: " + guessed_word)
    
    #print(f"Average number of guesses for a trial of {try_count} words: {round(total_guesses/try_count,5)}\nMax number of guesses: {maxx}")
