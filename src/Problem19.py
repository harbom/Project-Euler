"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

monthlist = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
monthtoday = {'jan':31,'feb':28,'mar':31,'apr':30,'may':31,'jun':30,'jul':31,'aug':31, 'sep':30,'oct':31,'nov':30,'dec':31}

def main():
    alldays=[[0 for i in range(7)] for j in range(5*12*101)]
    arrayindex=0
    dayindex= 1 #dayindex of 0 will correspond to a sunday

    numSundays = 0

    for year in range(1900,2001): #iterate over all years in the range
        if (isLeapYear(year)):
            monthtoday['feb']=29
        else:
            monthtoday['feb']=28
        
        for monthindex in range(12): #iterate over all months in year
            month = monthlist[monthindex]
            daysinmonth = monthtoday[month]
            
            for day in range(1,daysinmonth+1): #iterate over days in month
                if (dayindex == 7): #go to the next subarray
                    dayindex=0
                    arrayindex+=1
                if (year in range(1901,2001)): #only count data from jan 1 1901 to dec 31 2000, else itll be 0
                    alldays[arrayindex][dayindex] = day
                dayindex+=1  

    #go over huge 2d array and iterate numsundays for every entry with subarray index 0 and value 1
    for i in range(len(alldays)):
        currarray = alldays[i]

        for j in range(7):
            day = currarray[j]
            
            if (day==1 and j==0): #first day of month and its a sunday
                numSundays+=1
    
    print(numSundays)

def isLeapYear(year):
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4==0:
        return True

if __name__ == '__main__':
   main()