minimum = 9999999999999
maximum = -minimum
while True:
    num_str = input("Enter a number: ")
    try: 
        num = int(num_str)
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    except Exception:
        if num_str == 'done':
            break
        else:
            print("Invalid input")
            continue

print(minimum, maximum)