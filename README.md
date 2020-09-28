# WordSearch
## A Word Search Generator for python.
derived from mast3rsoft's repository [mast3rsoft/WordSearch](https://github.com/mast3rsoft/WordSearch)

## How to use

### 1. import the *the word search Generator*

``` Python
from utils import WordSearch
```
### 2. initialize the *WordSearch* Object
``` Python
# read vocabulary from "voc.txt"
with open("voc.txt") as voc:
    words = voc.readlines()
for i in range(len(words)):
    words[i] = words[i].strip().upper()


# initiate WordSearch 1
w1 = WordSearch(words, 4, 14)
w1.showResult()
w1.gridToCSV("grid1.csv")
```

## What can a Word search object do?
------------------------------------------------------------------------------------------------------------------------------
### Methods
 > ``` WordSearch.letter(row, column) ```                                                                                       
 Discription: it returns a letter (string) in the defined parameters
 
 > ```WordSearch.findWords(words)```                                                                                            
 Discription: it searches the words in Grid. (Note: words is a list and is not seperated by commas.) It returns a dictionary where the key is the word and value is a list of tuples(Note:that the tuples are in that order: (y,x)) of the positions the letters
 
 > ```WordSearch.showResults```
 Description: Prints the Grid and the Word Bank
 
 > ```WordSearch.gridToCSV(name = ""grid.csv)```
 Description: Save the grid to a csv format
 
### Propeties
 > ```WordSearch.Grid```                                                     
 Description: It is the WordSearch Grid where all letters are stored.
 
 > ```WordSearch.maxX```                                                     
 Description: The "x" value you defined at the start of generating the object.
 
 > ```WordSearch.maxY```                                                  
 Description: The "y" value you defined at the start of generating the object.
