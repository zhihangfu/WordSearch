# WordSearch
## A Word Search Generator for python.
derived from mast3rsoft's repository [mast3rsoft/WordSearch](https://github.com/mast3rsoft/WordSearch)

## How to use

### 1. import the *the word search Generator*

```python
from utils import WordSearch
```
### 2. initialize the *WordSearch* Object
```python
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

### 3. you should see something like this in your output:
```
GRID
------------------------------
R R E V O L 1 
E A L M L 2 T 
W G O I 4 A R 
O E G 0 O R A 
P H I F 6 E T 
T X C 1 K 1 S 
C H T U O Y 8 

Word Bank
------------------------------
ART : (3, 6) -> (1, 6)
INNOVATION : (13, 1) -> (4, 1)
42 : (2, 4) -> (1, 5)
0618 : (3, 3) -> (6, 6)
RAGE : (0, 1) -> (3, 1)
LOVE : (0, 5) -> (0, 2)
ERA : (4, 5) -> (2, 5)
EDEN : (11, 4) -> (11, 1)
NIGHT : (12, 1) -> (12, 5)
SKY : (7, 0) -> (9, 2)
ACT : (9, 8) -> (9, 10)
LOGIC : (1, 2) -> (5, 2)
IMAGINATION : (1, 2) -> (11, 2)
INSPIRATION : (13, 1) -> (13, 11)
LIGHT : (1, 4) -> (5, 0)
YOUTH : (6, 5) -> (6, 1)
HAPPINESS : (8, 9) -> (0, 1)
HUMOR : (0, 4) -> (4, 0)
HONESTY : (4, 10) -> (10, 4)
TIME : (3, 8) -> (0, 5)
POWER : (4, 0) -> (0, 0)
HEALTH : (12, 4) -> (7, 9)
MAGIC : (0, 7) -> (0, 11)
STAR : (5, 6) -> (2, 6)
IDEA : (10, 10) -> (10, 7)
ADAM : (8, 12) -> (5, 12)
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
