# python3

import sys
import threading
import numpy 


def compute_height(n, parents):
    max_height = 0
    augstumi = numpy.zeros(int(n))
    for i in range(int(n)):
        if augstumi[i] > 0:
            continue
        augstums = 0
        k=i
        while k != -1:
            if augstumi[k]>0:
                augstums += augstumi[k]
                break
            else:
                augstums += 1
                k = int(parents[i])
                augstumi[k] = augstums
        if augstums > max_height:
            max_height = augstums
    return max_height


def input_file(file):
    try:
        with open(file, "r",  encoding="utf8") as f:
            saturs = f.readlines()
    except:
        print("Error")
        return None, None
    
    n=saturs[0].strip()
    if n:
        parents = saturs[1].strip().split(" ")
        if parents:
            f.close()
            return n, parents
    return None, None

def ievadisana():
    n = input().strip()
    if n:
        parents =  input().strip().split(" ")
        if parents:
            return n, parents
    return None, None

def main():
    ievadit = input().strip()
    if ievadit == "F":
        file = input().strip()
        if str(file[-1]) != "a":
            n, parents = input_file(file)
            if n and parents:
                augstums = compute_height(n, parents)
                print(int(augstums))
    elif ievadit == "I":
        n, parents = ievadisana()
        if n and parents:
            augstums = compute_height(n, parents)
            print(int(augstums))

    
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))