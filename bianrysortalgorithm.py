def bs(array, element):
    element1 = 0
    element2 = len(array) - 1
    while element1 <= element2:

        element3 = (element1 + element2) // 2
        if (array[element3] == element):
            return element3
        elif (array[element3] > element):
            element2 = element3 - 1
        else:
            element1 = element3 + 1

    return -1


array = input('Enter the elements: ')
array = array.split()
array = [int(x) for x in array]
element = int(input(' Enter The number to be  searched: '))

result = bs(array,element)
if result < 0:
    print(format(element),' is not present in the given array.')
else:
    print('{} is present in the given array {}.'.format(element, result))