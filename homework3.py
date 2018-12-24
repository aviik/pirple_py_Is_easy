"""Function to compare equality among its input arguments"""

#function to check conditions
def comp(a, b, c):
    if a==b or b==c or c==a:
          return True        
    else:
        # print("not equxls")  #test purpose
        return False

        
#function to accept the arguments
def main():
    print("Enter the three numbers: ")
    x = int(input("First Number: "))
    y = int(input("Second Number: "))
    z = int(input("Third Number: "))
    print(comp(x,y,z))
        
main()  