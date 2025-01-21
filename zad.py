def zad1():
    answer = []
    with open("trojki.txt","r") as file:
        for line in file:
            arr = line.split(" ")
            if sum(map(int,list(arr[0]+arr[1]))) == int(arr[2]):
                answer.append(line)
    file.close()
    return " ".join(answer)

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def zad2():
    answer = []
    with open("trojki.txt","r") as file:
        for line in file:
            arr = line.split(" ")
            a, b = int(arr[0]), int(arr[1])
            if isPrime(a) and isPrime(b) and a*b == int(arr[2]):
                answer.append(line)
    file.close()
    return " ".join(answer)

def isRightTriangleWorthy(line):
    arr = list(map(int,line.split(" ")))
    arr.sort()
    if pow(arr[0],2) + pow(arr[1],2) == pow(arr[2],2):
        return True
    return False

def zad3():
    answer = []
    with open("trojki.txt") as file:
        while line := file.readline():
            if isRightTriangleWorthy(line):
                line2 = file.readline()
                if isRightTriangleWorthy(line2):
                    answer.append(" ".join([line,line2]) + "\n")
    file.close()
    return " ".join(map(str,answer))

def isTriangleWorthy(line):
    arr = list(map(int,line.split(" ")))
    arr.sort()
    if arr[0] + arr[1] > arr[2]:
        return True
    return False    
                
def zad4():
    combo = 0
    longestCombo = 0
    answer = 0
    with open("trojki.txt") as file:
        for line in file:
            if isTriangleWorthy(line):
                combo += 1
                answer += 1
                longestCombo = max(longestCombo,combo)
            else:
                combo = 0
    file.close()
    return answer, longestCombo

print(zad1())
print(zad2())
print(zad3())
print(zad4())



    