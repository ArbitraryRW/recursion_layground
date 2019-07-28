print("Recursion playground running!")

def countdown(num):
    print(num)

    if num <= 0:
        return
    else:
        return countdown(num-1)

def factorial(num):
    print(num)
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

def sum(arr):
    print(arr)

    if arr == []:
        return 0

    return arr[0] + sum(arr[1:])


def list_counter(arr):
    if arr == []:
        return 0

    return 1 + list_counter(arr[1:])

def list_highest(arr):
    if arr == []:
        return 0

    cur_max = list_highest(arr[1:])

    # print("->", arr[1:])
    # print("->", cur_max)

    if arr[0] > cur_max:
        return arr[0]

    else:
        return cur_max

print("\n---Countdown---")
countdown(5)

print("\n---Factorial---")
print(factorial(5))

print("\n---Sum---")

arr = [4,1,2,6,3]

print(sum(arr))

print("\n---List Count---")

print(list_counter(arr))


print("\n---List Highest---")
print (list_highest(arr))