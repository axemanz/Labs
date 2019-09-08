# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:28:51 2019

@author: amanz
"""
import time

start = time.time()

def read_file_and_make_set():                                                   #while it reads the file, it splits any 
    file_set = set(open('words_alpha.txt').read().split())                      #empty spaces and takes each word into a set 
    return file_set                                                             #returns set

def make_list_of_permutation(remaining_letters,permutated_letters,l):           #takes a word and a list and creates 
    if len(remaining_letters) == 0:                                             #various combinations of that word 
        return l.append(permutated_letters)                                     #then stores it in an list
    else:                                                                       #and returns that list once it's done
        for i in range(len(remaining_letters)):
            p_letters = remaining_letters[i]
            r_letters = remaining_letters[:i] + remaining_letters[i+1:]
            make_list_of_permutation(r_letters,permutated_letters+p_letters,l)

def search_for_anagrams(s1, s2):                                                #using the intersection function, it
    result_set = s2.intersection(s1)                                            #compares both sets and finds the
    return result_set                                                           #anagrams of the inputed word

def get_rid_of_word(w,l):                                                       #removes the inputed word from set
    l.remove(w)
        
word = input('Enter a word or empty string to finish: ')
if word == '':
    print('Bye, thanks for using this program!')
    pass
else:
    list1 = []                                                                  #an empty list
    
    make_list_of_permutation(word,'',list1)                                     #call for method to modify list1
    get_rid_of_word(word,list1)                                                 #call for method to get rid of original word
    
    set1 = set(list1)                                                           #converts list1 into set
    set2 = read_file_and_make_set()                                             #call for method to create set from file
    
    anagram_set = search_for_anagrams(set1, set2)                               #creates a set with method to search anagrams
    sorted_set = sorted(anagram_set)                                            #sorts the anagram_set
    
    print('The word ', word, ' has the following 6 anagrams: ')
    
    for i in range(len(sorted_set)):
        print(sorted_set[i])
        
    end = time.time()
    print('It took', end - start, 'seconds to find the anagrams')

    
    
    