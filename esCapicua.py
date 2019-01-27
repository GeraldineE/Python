def esPalindromo(valor):
    i=0
    j=len(valor)-1
    while i <j:
        if valor[i]!= valor[j] :
            return False
        i+=1
        j-=1
    return True


def main():
    print (esPalindromo("123454321"))
    print (esPalindromo("111111"))
    print (esPalindromo("12345$4321"))
    print (esPalindromo("1234543281"))
    print (esPalindromo("111"))
    print (esPalindromo("2222"))
    print (esPalindromo("anecdota"))
    
main()