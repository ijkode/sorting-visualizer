import random
from tkinter import *
from tkinter import font
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

window = Tk()
window.iconbitmap(r'sort.ico')
window.title("Sorting Visualizer")
window.minsize(width=800, height=50)
window.maxsize(width=1600, height=50)
window.geometry('800x50')
myFont = font.Font(family='FF DIN', weight="bold", size=10)
sizeValue = Scale(window, from_=0, to=100, resolution=1, orient=HORIZONTAL, relief=GROOVE, highlightthickness=0, bd=2,
                  bg="black", fg="white",
                  width=24)
sizeValue.grid(column=6, row=0, sticky="nsew")


def bubble():
    amount = int(sizeValue.get())
    arr = np.random.randint(0, 100, amount)
    x = np.arange(0, amount, 1)

    for n in range(len(arr) - 1, 0, -1):
        plt.bar(x, arr)
        charts(arr)
        plt.title("Bubble Sort, Complexity - O(n^2)", size=10)
        plt.pause(0.01)
        plt.clf()
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    plt.bar(list(range(amount)), arr)
    charts(arr)
    plt.title("Bubble Sort, Complexity - O(n^2)", size=10)
    plt.show()


def merge():
    random.seed("ABC")
    amount = int(sizeValue.get())
    numbers = [random.randint(0, 100) for _ in range(amount)]

    def mergeSort(arr, left, right):
        if left >= right:
            return

        mid = (left + right) // 2

        plt.bar(list(range(amount)), arr)
        charts(arr)
        plt.title("Merge Sort, Complexity - O(nlogn)", size=10)
        plt.pause(0.01)
        plt.clf()

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge1(arr, left, right, mid)

        plt.bar(list(range(amount)), arr)
        charts(arr)
        plt.title("Merge Sort, Complexity - O(nlogn)", size=10)
        plt.pause(0.01)
        plt.clf()

    def merge1(arr, left, right, mid):
        left_cpy = arr[left:mid + 1]
        right_cpy = arr[mid + 1:right + 1]

        l_counter, r_counter = 0, 0
        sorted_counter = left

        while l_counter < len(left_cpy) and r_counter < len(right_cpy):
            plt.bar(list(range(amount)), arr)
            charts(arr)
            plt.title("Merge Sort, Complexity - O(nlogn)", size=10)
            plt.pause(0.01)
            plt.clf()
            if left_cpy[l_counter] <= right_cpy[r_counter]:
                arr[sorted_counter] = left_cpy[l_counter]
                l_counter += 1
            else:
                arr[sorted_counter] = right_cpy[r_counter]
                r_counter += 1

            sorted_counter += 1

        while l_counter < len(left_cpy):
            plt.bar(list(range(amount)), arr)
            charts(arr)
            plt.title("Merge Sort, Complexity - O(nlogn)", size=10)
            plt.pause(0.01)
            plt.clf()
            arr[sorted_counter] = left_cpy[l_counter]
            l_counter += 1
            sorted_counter += 1

        while r_counter < len(right_cpy):
            plt.bar(list(range(amount)), arr)
            charts(arr)
            plt.title("Merge Sort, Complexity - O(nlogn)", size=10)
            plt.pause(0.01)
            plt.clf()
            arr[sorted_counter] = right_cpy[r_counter]
            r_counter += 1
            sorted_counter += 1

    mergeSort(numbers, 0, len(numbers) - 1)
    plt.bar(list(range(amount)), numbers)
    charts(numbers)
    plt.title("Merge Sort, Complexity - O(nlogn)", size=10)
    plt.show()


def insertionSort():
    amount = int(sizeValue.get())
    arr = np.random.randint(0, 100, amount)
    x = np.arange(0, amount, 1)
    for i in range(1, len(arr)):
        plt.bar(x, arr)
        charts(arr)
        plt.title("Insertion Sort, Complexity - O(n^2)", size=10)
        plt.pause(0.01)
        plt.clf()
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    plt.bar(list(range(amount)), arr)
    charts(arr)
    plt.title("Insertion Sort, Complexity - O(n^2)", size=10)
    plt.show()


def quick():
    amount = int(sizeValue.get())
    arr = np.random.randint(0, 100, amount)
    x = np.arange(0, amount, 1)
    n = len(arr)

    def partition(arr, low, high):
        i = (low - 1)
        pivot = arr[high]

        for j in range(low, high):

            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    def quickSort(arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = partition(arr, low, high)
            plt.bar(x, arr)
            charts(arr)
            plt.title("Quick Sort, Complexity - O(nlogn)", size=10)
            plt.pause(0.05)
            plt.clf()
            quickSort(arr, low, pi - 1)
            quickSort(arr, pi + 1, high)

    quickSort(arr, 0, n - 1)
    plt.bar(x, arr)
    plt.title("Quick Sort, Complexity - O(nlogn)", size=10)
    plt.pause(0.05)
    plt.clf()
    plt.bar(list(range(amount)), arr)
    charts(arr)
    plt.title("Quick Sort, Complexity - O(nlogn)", size=10)
    plt.show()


def selectionSort():
    amount = int(sizeValue.get())
    arr = np.random.randint(0, 100, amount)
    x = np.arange(0, amount, 1)
    for i in range(len(arr)):
        plt.bar(x, arr)
        charts(arr)
        plt.title("Selection Sort, Complexity - O(n^2)", size=10)
        plt.pause(0.001)
        plt.clf()
        min_idx = i
        for j in range(i + 1, len(arr)):
            plt.bar(x, arr)
            charts(arr)
            plt.title("Selection Sort, Complexity - O(n^2)", size=10)
            plt.pause(0.0001)
            plt.clf()
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    plt.bar(list(range(amount)), arr)
    charts(arr)
    plt.title("Selection Sort, Complexity - O(n^2)", size=10)
    plt.show()


def charts(arr):
    for j in range(len(arr)):
        plt.text(j, arr[j], arr[j], ha="center", va="bottom")


Grid.rowconfigure(window, 0, weight=1)
Grid.columnconfigure(window, 0, weight=1)
Grid.columnconfigure(window, 1, weight=1)
Grid.columnconfigure(window, 2, weight=1)
Grid.columnconfigure(window, 3, weight=1)
Grid.columnconfigure(window, 4, weight=1)
Grid.columnconfigure(window, 5, weight=1)
Grid.columnconfigure(window, 6, weight=1)
btn1 = Button(window, text="Bubble Sort", bg="black", fg="grey", font=myFont, command=bubble)
btn1.grid(column=0, row=0, sticky="nsew")
btn2 = Button(window, text="Merge Sort", bg="black", fg="grey", font=myFont, command=merge)
btn2.grid(column=1, row=0, sticky="nsew")
btn3 = Button(window, text="Insertion Sort", bg="black", fg="grey", font=myFont, command=insertionSort)
btn3.grid(column=2, row=0, sticky="nsew")
btn4 = Button(window, text="Quick Sort", bg="black", fg="grey", font=myFont, command=quick)
btn4.grid(column=3, row=0, sticky="nsew")
btn5 = Button(window, text="Selection Sort", bg="black", fg="grey", font=myFont, command=selectionSort)
btn5.grid(column=4, row=0, sticky="nsew")
sizeLable = Label(window, text="Array Size:", bd=2, bg="grey", fg="black", font=myFont, width=10, height=3)
sizeLable.grid(column=5, row=0, sticky="nsew")

window.mainloop()
