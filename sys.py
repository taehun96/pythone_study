import sys

args = sys.argv[1:]
print(args)

total = 0
for i in args:
    total += int(i)

print(total)