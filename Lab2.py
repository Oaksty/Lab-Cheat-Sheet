print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")


def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")


def get_user_input():
    arraylist =[]
    print("get_user_input")
    inputstr = input()
    numlist = inputstr.split(",")
    print(numlist)

    for eachnum in numlist:
        arraylist.append(float(eachnum))
    print(arraylist)
    return arraylist


def calc_average(numlist):
    print("calc_average")
    total = sum(numlist)
    average = total / len(numlist)
    print("Average = ", f"{average: .2f}")
    return round(average, 2)


def find_min_max(numlist):
    print("find_min_max")
    templist = sort_temperature(numlist)
    min = templist [0]
    max = templist [-1]
    print("Min = " + str(min) + " and MAX = " + str(max))
    return [min,max]

"""
def calc_min_max_temperature(numlist):
   print("maximum number is ", max(numlist))
   print("minimum number is ", min(numlist))

"""


def sort_temperature(numlist):
    print("sort_temperature")
    templist = numlist.copy()
    templist.sort()
    print("Sorted Numbers = ", templist)
    return templist


def calc_median_temperature(numlist):
    print("calc_median_temperature")
    numlen = len(numlist)
    remainder = numlen % 2


    if remainder == 1:
        median = numlist [numlen//2]
    else :
        median = (numlist[numlen//2] + numlist[numlen//2 - 1])/2


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    numlist = get_user_input()
    calc_average(numlist)
    find_min_max(numlist)
    calc_median_temperature(numlist)


if __name__ == "_main_":
    main()