filename = input('Enter the file name: ')

total = 0
count = 0
pattern = 'X-DSPAM-Confidence:'

try:
    with open(filename) as f:
        for line in f:
            if line.startswith(pattern):
                num = float(line[len(pattern):].strip())
                total += num
                count += 1
        if count == 0:
            print('No spam confidence found in this file')
        else:
            print('Average span confidence:', total / count)
except Exception:
    print('The file({}) fails to extract'.format(filename))

