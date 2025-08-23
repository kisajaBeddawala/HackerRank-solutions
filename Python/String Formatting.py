def print_formatted(number):
    length = len(bin(number)) - 1
    for i in range(1,number+1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]
        
        #when starting number not want any additinal space so remove it
        print(decimal.rjust(length-1) + octal.rjust(length)+hexa.rjust(length) + binary.rjust(length))
    
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)