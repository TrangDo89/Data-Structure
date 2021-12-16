# Name: Trang Do U26667617

def read():
    file = open("hw3-ExtraCredit.txt", "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values

def find_duplicate():
    list = read()

    duplicate = []
    for i in range(len(list)):
        count = 1
        if (list[i] != -1):
            j = i+1
            while(j < len(list)):
                if list[i] == list[j]:
                    count +=1
                    list[j] = -1
                j+=1

            if count > 1:
                duplicate.append(list[i])

    print('The duplicate numbers: ', str(duplicate)[1:-1])

find_duplicate()




