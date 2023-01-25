# menu selector
import datetime 
tStamp1 = datetime.datetime.now()



select = 0
def DisplayMenu() :
    print ("enter your choice")
    print ("1 for a Linear Search")
    print ("2 for a Binary Search")
    print ("3 for a Bubble Sort")
    print ("4 for a Selection Sort")
    print ("5 for a Insertion Sort")



# implementation of a Linear Search
# time complexity ( Order of Magnitude ) : O(n)
def LinearSearch():
    elements = [10, 20, 80, 70, 60, 50]
    x = int(input("please enter the number to search: "))
    # Boolean Flag
    found = False
    for i in range(len(elements)) :
        if elements[i] == x :
            found = True
            print("%d found at %dth position" % (x, i))
            break
        if found == False :
            print("%d is not in list" % x)
            break
def BinarySearch() :

    n = int(input("Enter the size of the list: "))
    sortedlist = []
    # populate the list in sort entry order
    for i in range(n) :
        sortedlist.append(int(input("Enter %dth element: " % i)))
    x = int(input("Enter the number to search: "))

    start = 0
    end = n - 1
    while(start <= end) :
        mid = int((start + end) / 2)
        if (x == sortedlist[mid]) :
            break
        elif (x < sortedlist[mid]) :
            end = mid - 1
        else :
            start = mid + 1
       

    if sortedlist[mid] ==x :
        print("element number %d is present at position: %d" % (x, sortedlist[mid]))
    else :
        print("element number %d is not present in the list" % x)
def BubbleSort():
    arr = [64, 34, 25, 12, 22, 11, 90]
    # program for implementing a Bubble Sort
    n = len(arr)
    # Traverse through all array elements
    for i in range(n - 1) :
    # range(n) also work but outer loop will repeat on time
    # more than necessary
    # Last i elements are already in place
        for j in range(0, n - i - 1) :
    # traverse the array from 0 to n-i-1
    # Swap if the element found is greater
    # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    # driver code to test the above routine
    
    print ("the sorted array is:")
    for i in range(len(arr)) :
        print ("%d" %arr[i]),
def SelectionSort():


    # Routine for a Selection Sort
    A = ['t','e','s','t','d','a','t','a']
    for i in range(len(A)) :
        min_= i
    for j in range(i + 1, len(A)) :
        if A[min_] > A[j] :
            min_ = j
    # swap performed
    A[i], A[min_] = A[min_], A[i]
    # main
    for i in range(len(A)) :
        print (A[i])
def InsertionSort():
    arr = [12, 11, 13, 5, 6]
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
  
        key = arr[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
  
  
# Driver code to test above


    for i in range(len(arr)):
        print ("% d" % arr[i])
def SelectRoutine():
    
    global select
    DisplayMenu()
    select = int(input())
    match select:
        case 1:
            print("calling linerar search")
            LinearSearch()
        case 2:
            print("calling binary search")
            BinarySearch()
        case 3: 
            print("Calling bubble sort")
            BubbleSort()
            
        case 4: 
            print("Calling selection sort")
            SelectionSort()
        case 5: 
            print("Calling insertion sort")
            InsertionSort()
        case other: 
            print("Invalid")

SelectRoutine()
tStamp2 = datetime.datetime.now()
delta = tStamp2 - tStamp1
interval = int(delta.total_seconds() * 1000)
print(interval)


