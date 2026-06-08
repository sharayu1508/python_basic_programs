# 14.Mobile Recharge System

total_earnings = 0

n = int(input("Enter number of customers : "))

for i in range(1, n + 1):

    print("\nRecharge Plans")
    print("1. ₹199")
    print("2. ₹399")
    print("3. ₹599")

    ch = int(input("Select Plan : "))

    if ch == 1:
        total_earnings += 199

    elif ch == 2:
        total_earnings += 399

    elif ch == 3:
        total_earnings += 599

    else:
        print("Invalid Plan!")

print("\nTotal Earnings =", total_earnings)
