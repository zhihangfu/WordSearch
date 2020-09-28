"""
dirived from maste3rsft's GitHub project: https://github.com/mast3rsoft/WordSearch
defines a class "WordSearch" as generator of word search puzzles
"""

import random
import csv


class WordSearch():
    HORIZONTAL = 0
    VERTICAL = 1
    DIAGONAL = 2
    REVHORIZONTAL = 3
    REVVERTICAL = 4
    REVDIAGONAL = 5
    REVFLIPDIAGONA = 6
    FLIPDIAGONAL = 7
    DONTCARE = -100
    wordPosition = {}

    def __init__(self, searchWords, width = 20, height = 20):
        self.width = width
        self.height = height
        self.grid = [] # grid is a list of list of strings (characters)
        testWords = ['superhero', 'gugu','gaga','blah','vodka']
        if searchWords == []: searchWords = testWords
        self.searchWords = []
        for word in searchWords:
            if len(word) <= max(width, height):
                self.searchWords.append(word)
        # self.searchWords = searchWords
        for row in range(0, self.height):
            self.grid.append(['*'] * width)
            # for column in range(0, self.width):
            #     self.grid[row].append('*')
        for word in searchWords:
            DIR = random.randint(0, 7)
            iteration = 0
            while (not self.engrave(word, self.DONTCARE , self.DONTCARE , DIR)) and iteration < 5000:
                iteration += 1
        self.obfusticate()

    def engrave(self, word, x, y, direction):
        if len(word) == 0:
            return True
        # word has length > 0
        # check if we need to choose random pos
        if x == self.DONTCARE or y == self.DONTCARE: # cannot have one random, one fixed
            iteration = 0
            while True:
                iteration += 1
                y = random.randint(0, self.height - 1)
                x = random.randint(0, self.width - 1)
                if self.grid[y][x] == '*' or iteration > 100:
                    break
        # check if x & y are valid
        if x == self.width or x < 0:
            return False
        if y == self.height or y < 0:
            return False
        if not (self.grid[y][x] == "*" or self.grid[y][x] == word[0]):
            return False
        undovalue = self.grid[y][x]
        undox = x
        undoy = y
        self.grid[y][x] = word[0]
        # now need to write rest of the word
        if direction == self.HORIZONTAL:
            x += 1
        elif direction == self.VERTICAL:
            y += 1
        elif direction == self.DIAGONAL:
            y += 1
            x += 1
        elif direction == self.REVHORIZONTAL:
            x -= 1
        elif direction == self.REVVERTICAL:
            y -= 1
        elif direction == self.REVDIAGONAL:
            y -= 1
            x -= 1
        elif direction == self.FLIPDIAGONAL:
            x += 1
            y -= 1
        elif direction == self.REVFLIPDIAGONA:
            x -= 1
            y += 1
        else:
            print("This direction not implemented yet")
        if self.engrave(word[1:], x, y, direction):
            # we could do the rest, we are happy and done
            return True
        else:
            # grrh: something didn’t work, we need to undo now
            y = undoy
            x = undox
            self.grid[y][x] = undovalue
            return False

    def obfusticate(self):
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        for j in range(self.height):
            for i in range(self.width):
                if self.grid[j][i] == '*':
                    self.grid[j][i] = alpha[random.randint(0,35)]

    def letter(self,x,y):
        return self.grid[x][y]

    def printPos(self):
        for key in self.wordPosition:
            print( key, ":", self.wordPosition[key][0], "->", self.wordPosition[key][-1] )

    def findWords(self, words):
        for word in words:
            firstLetter = word[0]
            positions = None
            y = 0; found = False
            while y < self.height and not found:
                x = 0
                while x < self.width and not found:
                    if firstLetter == self.grid[y][x]:
                        positions = self.wordIsHere(word, x, y)
                        if positions:
                            found = True
                            break
                    x += 1
                if not found:
                    y += 1
            if found:
                self.wordPosition[word] = positions
        self.printPos()

    def wordIsHere(self, word, firstX, firstY):
         """
         traverse all 8 directions
         """

         # horizontal
         found = True; x = firstX; y = firstY; positions = []
         for letter in word:
             if x >= self.width or letter != self.grid[y][x]:
                 found = False
                 break
             else:
                 positions.append((y, x))
                 x += 1
         if found:
             return positions

         # vertical
         found = True; x = firstX; y = firstY; positions = []
         for letter in word:
             if y >= self.height or letter != self.grid[y][x]:
                 found = False
                 break
             else:
                 positions.append((y, x))
                 y += 1
         if found:
             return positions

         # reverse horizontal
         found = True; x = firstX; y = firstY; positions = []
         for letter in word:
             if x < 0 or letter != self.grid[y][x]:
                 found = False
                 break
             else:
                 positions.append((y, x))
                 x -= 1
         if found:
             return positions

         # reverse vertical
         found = True; x = firstX; y = firstY; positions = []
         for letter in word:
             if y < 0 or letter != self.grid[y][x]:
                 found = False
                 break
             else:
                 positions.append((y, x))
                 y -= 1
         if found:
             return positions

         # diagonal
         found = True; x = firstX; y = firstY; positions = []
         for letter in word:
             if y >= self.height or x >= self.width or letter != self.grid[y][x]:
                 found = False
                 break
             else:
                 positions.append((y, x))
                 x += 1
                 y += 1
         if found:
             return positions

         # reverse diagonal
         found = True; x = firstX; y = firstY; positions = []
         for letter in word:
             if y < 0 or x < 0 or letter != self.grid[y][x]:
                 found = False
                 break
             else:
                 positions.append((y, x))
                 x -= 1
                 y -= 1
         if found:
             return positions

         # flip diagonal
         found = True; x = firstX; y = firstY; positions = []
         for letter in word:
             if y < 0 or x >= self.width or letter != self.grid[y][x]:
                 found = False
                 break
             else:
                 positions.append((y, x))
                 x += 1
                 y -= 1
         if found:
             return positions

         # reverse flip diagonal
         found = True; x = firstX; y = firstY; positions = []
         for letter in word:
             if y >= self.height or x < 0 or letter != self.grid[y][x]:
                 found = False
                 break
             else:
                 positions.append((y, x))
                 x -= 1
                 y += 1
         if found:
             return positions

         return None

    def printGrid(self):
        for row in self.grid:
            for letter in row:
                print("%s " % letter, end='')
            print()

    def showResult(self):
        print("\n\nGRID\n------------------------------")
        self.printGrid()
        print("\nWord Positions\n------------------------------")
        self.findWords(self.searchWords)

    def gridToCSV(self, name = "grid.csv"):
        with open(name, "w", newline="") as g:
            writer = csv.writer(g)
            writer.writerows(self.grid)

    def shape(self):
        return self.width, self.height
