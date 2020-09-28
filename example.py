from WordSearch import WordSearch


# read vocabulary from "voc.txt"
with open("voc.txt") as voc:
    words = voc.readlines()
for i in range(len(words)):
    words[i] = words[i].strip().upper()


# initiate WordSearch 1
w1 = WordSearch(words, 7, 7)
w1.showResult()
w1.gridToCSV("grid1.csv")

# initiate WordSearch 2
w2 = WordSearch(words, 13, 14)
w2.showResult()
w2.gridToCSV("grid2.csv")

# initiate WordSearch 3
w3 = WordSearch(words, 3, 14)
w3.showResult()
w3.gridToCSV("grid3.csv")

# initiate WordSearch 4
w4 = WordSearch(words, 9, 6)
w4.showResult()
w4.gridToCSV("grid4.csv")
