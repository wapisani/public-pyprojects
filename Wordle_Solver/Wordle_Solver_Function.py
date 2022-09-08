#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Dr. Will Pisani
@email: wapisani@mtu.edu

This script is a companion to Wordle_Solver_GUI.py.
"""

def solveWordle(guesses,correct_letters,correct_positions):
    import json, os
    from random import shuffle
    # os.chdir(r'/Users/wapisani/Documents/Programming/public-pyprojects/Wordle_Solver')
    with open(r'words_dictionary_five_letters.json','r') as handle:
        dict_words = json.load(handle)
    letters_in_word = [key for key in correct_letters.keys()]
    letters_left = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for guess in guesses:
        if guess == '':
            continue
        # Eliminate letters from the alphabet if they're not in the word
        for l in guess:
            if l not in correct_positions and l not in correct_letters:
                letters_left.pop(letters_left.index(l))
        
    possible_suggestions = []
    for word in dict_words:
        continue_flag = False
        for l in word:
            if l not in letters_left:
                continue_flag = True
                break
    
        if continue_flag:
            continue
        else:
            possible_suggestions.append(word)
            
    # Eliminate all words that don't have all of the letters
    # that wordle says is in the word
    to_eliminate = []
    for word in possible_suggestions:
        for l in letters_in_word:
            if l not in word:
                to_eliminate.append(word)
                break
            
    for word in to_eliminate:
        possible_suggestions.pop(possible_suggestions.index(word))
                
    # Eliminate all words that don't have letters in the right position
    to_eliminate = []
    for word in possible_suggestions:
        for index, l in enumerate(word):
            i = index + 1
            correct_letter = correct_positions[index]
            # If the letter of the word is definitely in the word
            # Check if the position of the letter has already been tried
            if l in correct_letters:
                for position in correct_letters[l]:
                    if i == position:
                        to_eliminate.append(word)
            if correct_letter == '':
                continue
            else:
                if correct_letter != word[index]:
                    to_eliminate.append(word)
                    break
                
    for word in set(to_eliminate):
        possible_suggestions.pop(possible_suggestions.index(word))
    
    shuffle(possible_suggestions)
    print("Try one of these suggestions:")
    if len(possible_suggestions) < 20:
        for word in possible_suggestions:
            print(word)
    else:
        count = 1
        for word in possible_suggestions:
            num_letters = dict_words[word]
            if num_letters > 4:
                print(word)
                count += 1
                if count >= 20:
                    break
    
    
    
    
