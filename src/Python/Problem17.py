#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


lettertonum = {1:"one",2:"two",3:'three',4:'four',5:'five', 6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',
100:'onehundred',200:'twohundred',300:'threehundred',400:'fourhundred',500:'fivehundred',
600:'sixhundred',700:'sevenhundred',800:'eighthundred',900:'ninehundred',1000:'onethousand'}

totallettersum=0
allletters=""

top = 1000
for i in range(1,top+1):
    num=i
    allletters=""

    if i in lettertonum:
        allletters = lettertonum[i]
        print("number: ",i,"string: ",allletters)
        totallettersum += len(allletters)
        continue

    while(num > 0):
        if (num <= 20): #0 <= num <= 20
            string = lettertonum[num] #get number from mapping
            allletters += string
            totallettersum += len(string) #add to total sum
            break
        
        elif (num < 100): #21 <= num < 100
            firstnum = int(str(num)[0])
            tensplace = lettertonum[firstnum*10]
            totallettersum += len(tensplace)
            allletters += tensplace
            num = num%10 #get the remainder of the number by %10

        elif (num <= 1000): #101 <= num <= 1000
            #say num  is 345, youd take the first number off, thats 3, length of string is 100 so thats 10^(3-1)
            firstnum = int(str(num)[0])
            tenmultiplier = firstnum * 10**(len(str(num))-1)

            string = lettertonum[tenmultiplier] + "and" #would be 'threehundredand'
            totallettersum += len(string)
            allletters += string
            num = num%100 #get remainder of number after %100
    
    print("number: ",i,"string: ",allletters)
    
print("length: ",totallettersum)