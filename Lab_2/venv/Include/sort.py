
import random
def count_sort_time(length: int, step: int=1):
    from random import randint
    from time import process_time_ns

    n_time = dict()
    for j in range(0, length+1, step):
        r = []
        for i in range(0, j):
            new = randint(-100000000001, 100000000001)
            if new not in r:
                r.append(new)
            else:
                i -= 1
        t1 = process_time_ns()
        #select_sort_max(r)
        t2 = process_time_ns()
        n_time.update([(j, round(t2-t1, 10))])
    return n_time


# print(count_sort_time(100000, 100000))

def hoare_sort(nums, fst, lst):
    if fst >= lst: return

    i, j = fst, lst
    pivot = nums[random.randint(fst, lst)]

    while i <= j:
        while nums[i] < pivot: i += 1
        while nums[j] > pivot: j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    hoare_sort(nums, fst, j)
    hoare_sort(nums, i, lst)

array = [random.randint(0,100000) for i in range (10000)]
hoare_sort(array,0,len(array)-1)
print(array)