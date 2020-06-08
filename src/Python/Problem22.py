"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
"""
names=[]

def initNamesArr():
    r = open("Python/Problem22Data.txt")
    allstrings = r.read()
    r.close()

    allstrings = allstrings.split(",")
    for name in allstrings:
        names.append(name[1:-1]) #ignore the "" surrounding the name
    
    #print(names)
def main():
    initNamesArr()
    names.sort()
    #print(names)

    total=0
    top = len(names)
    for i in range(top):
        index=i+1
        currsum = sum([ord(name)-64 for name in names[i]]) #-64 to make A->1, B->2 etc
        total += index*currsum
    
    print(total)

if __name__ == '__main__':
    main()