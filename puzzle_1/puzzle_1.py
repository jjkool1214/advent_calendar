import re


def count(filename):
    with open(filename) as file:
        count = 0
        for line in file:
            nums = re.findall("[0-9]", line)
            coord = int(str(nums[0]) + str(nums[-1]))
            count += coord
    return count

bgrjigbrjieo

def main():
    print(count('day1input.txt'))

main()