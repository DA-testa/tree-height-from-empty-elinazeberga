# python3

import sys
import threading
import numpy 


def compute_height(n, parents):
    augstumi = numpy.zeros(n, dtype=int)
    for i in range(int(n)):
        if augstumi[i] != 0:
            continue
        augstums = 1
        vertibas = parents[i]
        while vertibas != -1:
            if augstumi[vertibas] != 0:
                augstums += augstumi[vertibas]
                break
            augstums += 1 
            vertibas = parents[vertibas]  
        k = i
        while k != -1 and augstumi[k] == 0:
            augstumi[vertibas] = augstums
            augstums -= 1
            k = parents[k]
    return numpy.max(augstumi)


def main():
    check = input()
    if check == "I":
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        file = input()
        if "a" in file:
            print("Error")
            return
        with open ("test/" + file, "r", encoding='UTF-8') as f:
            n = int(f.readlines())    
            parents = numpy.array(list(map(int, f.readline().split)))
    augstums = compute_height(n, parents)
    print(augstums)    
    

    
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