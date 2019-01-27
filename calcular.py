import sys

def calcular():
    oper = sys.argv[2]
    opL = float(sys.argv[1])
    opR = float(sys.argv[3])    
    if oper == "+":
       return opL + opR
    if oper == "-":
        return opL - opR
    if oper == "*":
        return opL * opR
    if oper == "/":
        return opL / opR


def argumentosCorrectos():
    return len(sys.argv) == 4     #el primero es el ejecutable, y los otros 3 son de la expresión


def main():
    if argumentosCorrectos():
       resultado = calcular()
       print(resultado)
    else:
        print("error en la expresión")


if __name__ == "__main__":
    main()