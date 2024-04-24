import numpy as np
import matplotlib.pyplot as plt
import time

amount = 80

list1 = np.random.randint(0, 150, amount)
x = np.arange(0, amount, 1)

print("WELCOME TO SORTING ALGORITHM VISUALISER!!!")
print("Select speed of sort from 1 to 100")
speed = int(input())
if speed > 100 or speed < 0:
    print("please enter valid speed")
print(" ")
print("Press 1 for bubble sort")
print("Press 2 for selection sort")
print("Press 3 for insertion sort")
print("Press 4 for cocktail shaker sort")
print("Press 5 for radix sort")
print("Press 6 for merge sort")


choice = int(input())

colorblack = [0.0,  # redness
              0.0,  # greenness
              0.0,  # blueness
              1  # transparency
              ]

colorred = [0.9,
            0.0,
            0.0,
            1
            ]

colorgreen = [0.0,
              0.9,
              0.0,
              1
              ]


# best,worst, and average case: n^2

def selectionsort(list):
    start = time.time()
    for i in range(len(list)):
        min_idx = i
        for j in range(i + 1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j

        list[i], list[min_idx] = list[min_idx], list[i]
        ax = plt.axes()
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        plt.bar(x, list, color=colorblack)
        plt.pause(0.7)
        plt.clf()
    end = time.time()
    print("time elapsed = ", end - start, "sec(s)")
    print("best, worst and average case = n^2")



# best-case: n
# worst-case: n^2
def bubblesort(list):
    n = len(list)
    start = time.time()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                plt.bar()
                swapped = True
        if swapped == False:
            break
        ax = plt.axes()
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        plt.bar(x, list, color=colorblack)
        plt.pause(0.7)
        plt.clf()
    end = time.time()
    print("time elapsed = ", end - start, "sec(s)")
    print("best case: n     worst case: n^2")



# called for time elapsed
def cocktailtime(list):
    start = time.time()
    cocktailsort(list)
    end = time.time()
    print("time elapsed = ", end - start, "sec(s)")
    print("best case: n     worst case: n^2")



# best-case: n
# worst-case: n^2
def cocktailsort(list):
    n = len(list)
    swapped = True
    start = 0
    end = n - 1
    while swapped == True:
        swapped = False

        for i in range(start, end):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swapped = True
        if swapped != False:
            swapped = False
            end = end - 1

            for i in range(end - 1, start - 1, -1):
                if list[i] > list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
                    swapped = True
            ax = plt.axes()
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')
            ax.spines['bottom'].set_color('white')
            ax.spines['top'].set_color('white')
            ax.spines['right'].set_color('white')
            ax.spines['left'].set_color('white')
            plt.bar(x, list, color=colorblack)
            plt.pause(0.7)
            plt.clf()
            start = start + 1
            continue

        break


# called for radix sort
def countingsort(list, exp1):
    n = len(list)

    output = [0] * n

    count = [0] * 10

    for i in range(0, n):
        index = list[i] // exp1
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = list[i] // exp1
        output[count[index % 10] - 1] = list[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(list)):
        list[i] = output[i]


# recursive call for time elapsed
def radixsorttime(list):
    start = time.time()
    radixsort(list)
    end = time.time()
    print("time elapsed = ", end - start, "sec(s)")
    print("best, worst, and average case: nd")
    print("where n is length of sorting data and d is no of digits in largest element")


# best, worst and average case: nd
# n = no of elements
# d = no of digits of largest element
def radixsort(list):
    max1 = max(list)
    exp = 1
    while max1 / exp >= 1:
        countingsort(list, exp)
        exp *= 10
        ax = plt.axes()
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        plt.bar(x, list, color=colorblack)
        plt.pause(0.7)
        plt.clf()



# best-case: n
# worst_case: n^2
def insertionsort(list):
    start = time.time()
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
        ax = plt.axes()
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        plt.bar(x, list, color=colorblack)
        plt.pause(0.7)
        plt.clf()
    end = time.time()
    print("time elapsed = ", end - start, " sec(s)")
    print("best case: n     worst case: n^2")




def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)
        plt.bar(x, list, color=colorblack)
        plt.pause(0.7)
        plt.clf()


plt.show()

if choice == 1:
    bubblesort(list1)
if choice == 2:
    selectionsort(list1)
if choice == 4:
    cocktailtime(list1)
if choice == 5:
    radixsorttime(list1)
if choice == 3:
    insertionsort(list1)
if choice == 6:
    quicksort(list1, 0, 99)

