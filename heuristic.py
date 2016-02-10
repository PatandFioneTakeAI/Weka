# Authors: Patrick Lebold & Fiona Heaney

import csv
import sys


def hasBottomLeft(row):
    if int(row[0]) == 1:
        row.append(1)
    elif int(row[0]) == 2:
        row.append(-1)
    else:
        row.append(0)
        
def middleThreeColumns(row):
    p1 = 0
    p2 = 0
    for piece in range(12,29):
        if int(row[piece]) == 1:
            p1 = p1 + 1
        elif int(row[piece]) == 2:
            p2 = p2 + 1 
    row.append(p1-p2)
    
def hasMiddle(row):
    if int(row[18]) == 1:
        row.append(1)
    elif int(row[18]) == 2:
        row.append(-1)
    else:
        row.append(0)
    
def highestPiece(row):
    for r in range(5, 0, -1):
        p1 = 0
        p2 = 0
        for c in range(r, 36+r, 6):
            if int(row[c]) == 1:
                p1 = p1 + 1
            elif int(row[c]) == 2:
                p2 = p2 + 1
        if p1 == 0 and p2 == 0:
            continue
        row.append(p1-p2)
        break;
        
def openSpaces(row):
    p1 = 0
    p2 = 0
    for index in range(0,41):
        neighbors = []
        if index > 5: #Has left neighboring tile
            neighbors.append(index-6)
        if (index-5)%6 != 0: #Has top neighboring tile
            neighbors.append(index+1)
        if index < 36: #Has right neighboring tile
            neighbors.append(index+6)
        if index%6 != 0: #Has bottom neighboring tile
            neighbors.append(index-1)
        if index > 5 and (index-5)%6 != 0: #Has topleft neighboring tile
            neighbors.append(index-5)
        if (index-5)%6 != 0 and index < 36: #Has topright neighboring tile
            neighbors.append(index+7)
        if index < 36 and index%6 != 0: #Has bottomright neighboring tile
            neighbors.append(index+5)
        if index%6 != 0 and index > 5: #Has bottomleft neighboring tile
            neighbors.append(index-7)
        for slot in neighbors:
            if int(row[slot]) == 0 and int(row[index]) == 1:
                p1 = p1 + 1
            elif int(row[slot]) == 0 and int(row[index]) == 2:
                p2 = p2 + 1
    row.append(p1-p2)
        
def heuristic(row):
    hasBottomLeft(row)
    middleThreeColumns(row)
    hasMiddle(row)
    highestPiece(row)
    openSpaces(row)

def main():    
    argsize = 3#len(sys.argv)
    if argsize == 3:  
        inputFileName = "trainDataSet.csv"#sys.argv[1]
        outputFileName = "newDataSet.csv"#sys.argv[2]
        csvList = []
        
        # Convert csv file to list
        with open(inputFileName, 'r') as file:
            reader = csv.reader(file)
            csvList = list(reader)
        
        
        # Apply heuristic to each row
        skipFirstRow = True
        for row in csvList:
            if skipFirstRow:
                skipFirstRow = False
                row.append("bottomLeft")
                row.append("middleThreeColumns")
                row.append("hasMiddle")
                row.append("highestPiece")
                row.append("openSpaces")
                continue
            heuristic(row)
            
        # Write new csv
        with open(outputFileName, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(csvList)
        
    else:
        print ("Incorrect number of arguments. Proper usage:\n")
        print ("./heuristic <input.csv> <output.csv>")  
        
#----------------------------------------------------------------
    
main()