storageCapacity = int(input("Enter storage capacity in GB: "))
def howManyFiles(storageCapacity):
    fileSize = 820
    storageCapacityMB = storageCapacity * 1024
    numberOfFiles = storageCapacityMB // fileSize
    return numberOfFiles
print("Number of files that can be stored:", howManyFiles(storageCapacity))


year = int(input("Enter a year: "))
def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
print("Is the year a leap year?", isLeapYear(year)) 


daysinweek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
while True:
    for day in daysinweek:
        print("Day of the week:", day)
        answer = input("Do you want to see the next day?: ")
        if answer != 'yes':
            break
    else:
        continue
    break
    
    
def OddInRange(start, end):
    for i in range(start, end + 1):
        if i % 2 != 0:
            yield i
print("Odd numbers between 1 and 50:")
for oddNumber in OddInRange(1, 50):
    print(oddNumber)
    
numbers = [10, 23, 45, 66, 78, 89, 90, 33, 21]
def filterNumbers(start, end):
    for number in numbers:
        if start <= number <= end:
            yield number
            
print("Numbers between 30 and 70:")
for num in filterNumbers(30, 70):
    print(num)