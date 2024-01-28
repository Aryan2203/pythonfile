def countingWordsFromFile():
     fileName=input("enter the file name : ")
     file=(fileName,'r')
     for line in file:
             words=line.split()
