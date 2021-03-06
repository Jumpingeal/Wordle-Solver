from wordle import *
import random

if __name__ == "__main__":
    all_words = purge(openf("wordlist-wordle.txt"))
    
    
    
    highest_guess = 0
    total_guesses = 0

    for j in range(len(all_words)):
        words = all_words.copy()
        frequency = letter_distribution(words,False)
        guessed_word = word_score(words,frequency,False)[0]
        guess_count = 1
        #get random 5 letter word
        # correct_word = words[random.randint(0,len(words) - 1)]
        correct_word = words[j]
        #print("Word to guess: " + correct_word)
        
        #while word hasn't been guess
        while guessed_word != correct_word:
            #print(f"Guess {guess_count}: " + guessed_word)
            #for every character in guessed_word
            for i in range(len(guessed_word)):
                #if character is in correct and in position
                if guessed_word[i] == correct_word[i]:
                    words = include_position(guessed_word[i],[i],words)
                #if character is in correct word
                elif guessed_word[i] in correct_word:
                    words = exclude_position(guessed_word[i],[i],words)
                    words = include(guessed_word[i],words)
                #otherwise exclude
                else:
                    words = exclude([guessed_word[i]],words)
            frequency = letter_distribution(words,False)
            guessed_word = word_score(words,frequency,False)[0]
            guess_count += 1

        total_guesses += guess_count

        if guess_count > highest_guess:
            highest_guess = guess_count
        print(f'#{j}')
    #print(f"Guess {guess_count}: " + guessed_word)
    print(f'Highest number of guesses was: {highest_guess}')
    print(f'Average number of guesses was: {total_guesses/len(all_words)}')
    #print(f"Average number of guesses for a trial of {try_count} words: {round(total_guesses/try_count,5)}\nMax number of guesses: {maxx}")
