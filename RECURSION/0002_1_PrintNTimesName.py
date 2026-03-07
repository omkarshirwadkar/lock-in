def printNameNTimes(name, current, times):
    if current == times:
        return
    print(str(current + 1) + ", " + str(name))
    printNameNTimes(name, current + 1, times)

name = input("Enter your name: ")
times = int(input("Enter the number of times you want to print your name: "))

print(printNameNTimes(name, 0, times))