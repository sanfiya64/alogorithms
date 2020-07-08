
def Finding_MaxHeap(alst, size, i):
    largest = i
    l_Child = 2 * i + 1
    r_Child = 2 * i + 2

    if l_Child < size and alst[i] < alst[l_Child]:
        largest = l_Child

    if r_Child < size and alst[largest] < alst[r_Child]:
        largest = r_Child

    if largest != i:
        alst[i], alst[largest] = alst[largest], alst[i]

        Finding_MaxHeap(alst, size, largest)


def Sort_MaxHeap(arr):
    size = len(arr)

    for i in range(size // 2 - 1, -1, -1):
        Finding_MaxHeap(arr, size, i)

    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        Finding_MaxHeap(arr, i, 0)


print("Enter The Size Of The Array : ", end="\n")
size = int(input())
alst = []
print("Enter ", size, "Elements : ")
for i in range(size):
    ele = int(input())
    alst.append(ele)
Sort_MaxHeap(alst)
print("Elements In Array After Sorting Using Heap Sort : ")
for j in alst:
    print(j)