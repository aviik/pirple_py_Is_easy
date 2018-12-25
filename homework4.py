

myUniqueList = []
myLeftovers = []

#populating the lists
def listAdder(i):
    if i not in myUniqueList:
        myUniqueList.append(i)
        print("Added to unique list!")
        print("Updated unique list",  myUniqueList)
        return True
    else:
        myLeftovers.append(i)
        print("Not an unique input. Added to discard list")
        return False


def main():
    if len(myUniqueList) < 10:
        x = int(input("Input: "))
        listAdder(x)

main()