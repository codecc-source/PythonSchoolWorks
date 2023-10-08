print("1.________________________________")
print("Find the first 5 natural numbers: ")
print("----------------------------------")
print("The natural numbers are: ")
natNumbers = [1, 2, 3, 4, 5]
print(natNumbers)

natNumbers.sort()
print("Ascending sort: ", natNumbers)

natNumbers.sort(reverse=True)
print("Descending sort: ", natNumbers)

Sum = sum(natNumbers)
print("The sum of first 5 natural numbers: ", Sum)

print("")
print("2.________________________________")
val1 = int(input("Enter low range value: "))
val2 = int(input("Enter upper range value: "))

print("Prime numbers: ")
for num in range(int (val1), int(val2) + 1):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                break
            else:
                print(num)

print("")
print("3.________________________________")
num = 5
for i in range(num,0,-1):
    for s in range(0,num-i):
        print(" ", end="")
    for j in range(0,i):
        print(i, " ", end="")
    print()
