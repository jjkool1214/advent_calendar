import re


def count(filename):
    with open(filename) as file:
        count = 0
        lines = 0
        for line in file:
            nums = re.findall("[0-9]", line)
            coord = int(str(nums[0]) + str(nums[-1]))
            count += coord
            lines += 1
    return count, lines

def count_2(lst):
    count = 0
    for line in lst:
        nums = re.findall("[0-9]", str(line))
        coord = int(str(nums[0]) + str(nums[-1]))
        count += coord
    return count


def main():
    lst = [["1abc2"], ['pqr3stu8vwx'], ['a1b2c3d4e5f'], ['treb7uchet']]
    print(count_2(lst))

    print(count("C:\\advent_calendar_of_code\\advent_calendar\puzzle_1\\input.txt"))

main()gtrnmeigotre