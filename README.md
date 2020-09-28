# WordSearch
## A [Word Search](https://en.wikipedia.org/wiki/Word_search) Puzzle Generator using python.
forked from mast3rsoft's repository [mast3rsoft/WordSearch](https://github.com/mast3rsoft/WordSearch)

## How to use

### 1. import the the word search generator

```python
from WordSearch import WordSearch
```
### 2. initialize the *WordSearch* object
```python
# read vocabulary from "voc.txt"
with open("voc.txt") as voc:
    words = voc.readlines()
for i in range(len(words)):
    words[i] = words[i].strip().upper()


# initiate WordSearch 1
w1 = WordSearch(words, 7, 7)
w1.showResult()
w1.gridToCSV("grid1.csv")
```

### 3. then you should see something like this in your output:
```
GRID
------------------------------
J M L L 8 R N 
C T C A O E F 
R I 2 4 D V T 
8 A G E E R E 
S 1 G O A R 5 
K F 6 E L H A 
Y 4 2 0 V F X 

Word Positions
------------------------------
ART : (4, 4) -> (2, 6)
LOGIC : (5, 4) -> (1, 0)
42 : (2, 3) -> (2, 2)
0618 : (6, 3) -> (3, 0)
RAGE : (2, 0) -> (5, 3)
LOVE : (0, 3) -> (3, 6)
ERA : (3, 4) -> (5, 6)
EDEN : (3, 3) -> (0, 6)
SKY : (4, 0) -> (6, 0)
ACT : (1, 3) -> (1, 1)
```

## What can a Word search object do?
### Methods
```WordSearch.letter(row, column)``` returns a letter (string) in the defined parameters.

```WordSearch.shape()``` returns the width and height (as a tuple) of the grid.

```WordSearch.findWords(words)``` searches the words in Grid. (Note: words is a list and is not seperated by commas.) It returns a dictionary where the key is the word and value is a list of tuples(Note:that the tuples are in that order: (y,x)) of the positions the letters.

```WordSearch.showResults``` prints the grid and the word positions.

```WordSearch.gridToCSV(name = "grid.csv")``` save the grid to a csv format.

### Propeties
```WordSearch.Grid``` is the WordSearch Grid (as a list of lists) where all letters are stored.
