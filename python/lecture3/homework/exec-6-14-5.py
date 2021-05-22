s = 'X-DSPAM-Confidence:0.8475'

index = s.find(':')
num = float(s[index+1:])

print(num)
print(round(1+num, 4))