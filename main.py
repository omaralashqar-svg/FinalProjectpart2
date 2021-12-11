# Omar Alashqar
# 1565085


import copy
import csv
from operator import itemgetter

ManufacturerFile = input()

PriceFile = input()

SdFile = input()

## OPEN MANUFACTURER FILE AND READ ITS CONTENTS
with open(ManufacturerFile) as manfile:
    ListReader = csv.reader(manfile)
    ManufacturerList = []
    isDamagedList = []

    for row in ListReader:
        ManufacturerList += [row]
        manList = ManufacturerList
    i = 0

    ## APPENDS 'damaged' elments to isDamagedList

    while i < len(manList):
        val = manList[i].pop(3)
        isDamagedList.append(val)
        i += 1

    pricesOnlyList = []

with open(PriceFile) as pfile:
    ListReader = csv.reader(pfile)
    PricesList = []

    for row in ListReader:
        PricesList += [row]
    pList = PricesList

    ## APPENDS PRICES TO FULL INVENTORY
    i = 0
    while i < len(manList):
        n = 0
        while n < len(pList):
            if manList[i][0] == pList[n][0]:
                manList[i].append(pList[n][1])
            n += 1
        i += 1

    datesList = []

with open(SdFile) as sdFile:
    ListReader = csv.reader(sdFile)
    SdList = []

    for row in ListReader:
        SdList += [row]
        sList = SdList
    ## APPENDS SERVICE DATES TO FULL INVENTORY
    i = 0
    while i < len(manList):
        n = 0
        while n < len(sList):
            if manList[i][0] == sList[n][0]:
                manList[i].append(sList[n][1])
            n += 1
        i += 1

    ## ADDS THE DAMAGED CONTENT TO THE END OF THE FULL INVENTORY
    n = 0
    while n < len(isDamagedList):
        manList[n].append(isDamagedList[n])
        n += 1

    FullInventoryList = []
    ## SORTS THE FULL INVENTORY LIST BY MANUFACTURER
    FullInventoryList = (sorted(manList, key=(itemgetter(1))))

    ## WRITES INTO THE FULLINVENTORY CSV TO COMPLETE PART A
    with open('FullInventory.csv', 'w', newline='') as fullFile:
        FileWriter = csv.writer(fullFile)

        for row in FullInventoryList:
            FileWriter.writerow(row)

    queryString = str(input())

    qList = queryString.split()
    qResult = []

    FullInventoryList[0][1] = FullInventoryList[0][1].strip()
    FullInventoryList[1][1] = FullInventoryList[1][1].strip()


    print(qList[0])
    print(qList[0])


    j = 0
    s = 0

    while j < len(qList):
        while s < len(FullInventoryList[s]):
            if qList[j] != FullInventoryList[s][1]:
                qResult.append(qList[j])
                break

            j += 1


    if qList[0] == FullInventoryList[0][1]:
        print("match")

    print(qList[0], FullInventoryList[0][1])
   # print(bytes(qList[0].encode()), bytes(FullInventoryList[0][1].encode()))


    i = 0
    while j < len(qList):
        while i < len(FullInventoryList):
            if (qList[j]) == (FullInventoryList[i][1]):
                qResult.append(qList[j])

            i += 1
        j += 1


    #while j < len(qList):

    #while i < len(FullInventoryList[i]):
           # if (qList[j]) == (FullInventoryList[i][1]):
            #    qResult.append(qList[j])
            #i += 1
        #j += 1

