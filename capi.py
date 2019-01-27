def Capi(num):
    i=0
    j=len(num)-1

    while i < j:
        if(num[i]!=num[j]):
            return False
        i+=1
        j-=1
    return True
  


def main():
    print(Capi("hjkeueh"))

  

if __name__=="__main__":
    main()
  



