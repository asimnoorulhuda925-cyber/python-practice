total=0
digits=input("Enter the number: ")
while len(digits)!=9 or not digits.isdigit():
    digits=input("Incorrect! Pls re-enter the number:")
for i in range(1,9):
    print("i:",i)
    print ("digit:",digits[i-1])
    total=(int(digits[i-1])*i)+total
    print("total:",total)
if (total%10)==int(digits[8]):
    print("valid input")
else:
    print("invalid input")
