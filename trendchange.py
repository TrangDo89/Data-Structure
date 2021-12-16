#Group 31: Trang Do - U26667617, Arianna Loucks - U69700489
#Find the trend change points of the array.
# The following "read" function reads values from a file named "inputHW1.txt" and returns the values in an array.

def read():
    file = open("TestInputHW1.txt", "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values

# read the function for trend change point
def trendchange():
    numbers = read()

    print("The trend change point:")

# using for loop and if to find the point change
    for i in range(len(numbers)-2):
        if (numbers[i] > numbers[i + 1] and numbers[i+2] > numbers[i+1]):
            goal = numbers[i+1]
            print(goal)
            print(numbers[i+2])

        if (numbers[i] < numbers[i + 1] and numbers[i+2] < numbers[i+1]):
            goal = numbers[i+1]
            print(goal)
            print(numbers[i+2])


trendchange()

