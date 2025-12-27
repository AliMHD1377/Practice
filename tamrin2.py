# به نام خدا

print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

for i in range(1, 11):
    sum = i + previous_num
    print(f"current Number {i} Previous Number {previous_num} sum: {sum}")

    # set it to the current number
    previous_num = i
