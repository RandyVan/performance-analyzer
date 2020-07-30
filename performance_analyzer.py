import random
import time
from demos import quicksort,mergesort,bubblesort

def random_list(size,max_val):
    random_list = []
    for num in range (size):  
        random_list.append(random.randint(1,max_val))
    return random_list

def analyze_func(func_name,arr):
    tic = time.time()
    func_name(arr)
    toc = time.time()
    seconds = toc - tic
    print(f"{func_name.__name__.capitalize()}\t-> Elapsed Time: {seconds:.5f} ")

size = int(input("What is the size of the list you want to create? "))
max = int(input("What is the max value of the range? "))
run_times = int(input("How many times do you want ot run? "))

for num in range(run_times):
    print(f"Run: {num+1}")
    l = random_list(size,max)
    analyze_func(bubblesort,l.copy())
    analyze_func(quicksort,l)
    analyze_func(mergesort,l)
    print("-" * 40)