from typing import List, Union
#Words starting with uppercase letters will not be syllabized appropriately.
consonant=['b', 'c', 'ç', 'd', 'f', 'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ş', 't', 'v', 'y', 'z']
word_input = input("Enter a word: ")
word=[]
word.extend(word_input)         #added the letters of the word
wordCp = word[:]                #copied the list to use after filtering
consonantLoc = []               #list for consonant locations
counter = 0                     #for the while loop
counterForLoc = 0               #will be explained...
for i in word:                  #filters the consonants and locates their indexes
	for x in range(len(consonant)):
		if i == consonant[x]:
			consonantLoc.append(word.index(i))
			word.remove(i)
			word.insert(0,"a")      #it is here for not to skip a consonant 
if word_input[consonantLoc[-1]] == word_input[-1]:
	del consonantLoc[-1]
usedLen= len(consonantLoc)-1            #is to make things simple
while counter<=usedLen:                 #this is where the " - "s are added
                #checks if the indexes are sequential or not
        #if there are sequential 3 consonant:
	if counter+2 <= usedLen and consonantLoc[counter]==consonantLoc[counter+1]-1==consonantLoc[counter+2]-2:
		wordCp.insert(consonantLoc[counter]+2+counterForLoc," - ")
		counter+=3
        #if there are sequential 2 consonant:
	elif counter+1 <= usedLen and consonantLoc[counter]==consonantLoc[counter+1]-1:
		wordCp.insert(consonantLoc[counter]+1+counterForLoc," - ")
		counter+=2
        #if there is no sequential:
	elif counter<=usedLen:
		wordCp.insert(consonantLoc[counter]+counterForLoc," - ")
		counter+=1
	counterForLoc+=1#for the " - " we are adding i had to add this for the indexes
for i in range(len(wordCp)):
	print(wordCp[i],end="")
