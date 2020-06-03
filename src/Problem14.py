mapping={}
def collatzChainLen(i):
    len=1
    temp=i

    while(temp != 1):
        if temp in mapping:
            len = len + mapping[temp]
            break;
        
        if temp%2==0:
            temp/=2
        else:
            temp = 3*temp + 1
        len+=1
    
    mapping[i] = len
    return len

def main():
    maxlen=0
    maxnum=0
    for i in range(1,1000000,2):
        currlen = collatzChainLen(i)
        if currlen>maxlen:
            maxlen=currlen
            maxnum=i
    
    print(maxnum)

if __name__=='__main__':
    main()