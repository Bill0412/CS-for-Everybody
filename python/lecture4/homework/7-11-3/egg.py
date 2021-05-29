import os

filename = input('Enter the file name: ')

if filename == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        with open(filename) as f:
            count = 0
            for line in f:
                count += 1
            print('There were {} subject in {}'.format(count, filename))
    except Exception:
        print('File cannot be opened: {}'.format(filename))

