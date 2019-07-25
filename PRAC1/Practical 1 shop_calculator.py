number = int(input("Enter your items Number: "))
sum = 0
for i in range(0, number, 1):
    price = float(input("Enter your items price: "))
    sum = sum + price

if sum > 100:
    sum == sum *0.9
else:
    sum == sum
a = price
print("Total price for", number, "is {:.f2}", sum)
