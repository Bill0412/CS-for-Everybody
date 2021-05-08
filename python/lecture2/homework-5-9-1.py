total = 0
count = 0
while True:
    num_str = input("Enter a number: ")
    try: 
        num = int(num_str)
        total += num
        count += 1
    except Exception:
        if num_str == 'done':
            break
        else:
            print("Invalid input")
            continue

print(total, count, total / count)