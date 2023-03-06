# python3

import sys
import threading
import numpy 


def compute_height(n, parents):
    augstums = 0
    augstumi = []
    s=0
    augstumi = [i for i, e in enumerate(parents) if e == n]

    if len(augstumi) == 0:
        return 1
    for f in augstumi:
        augstums = max(compute_height(f, parents), augstums)
    ##augstumi = numpy.zeros(n)
    ##def augstums(i):
        ##if augstumi[i] != 0:
            ##return augstumi[i]
        ##if parents[i] == -1:
          ##  augstumi[i] = 1
        ##else:
          ##  augstumi[i] = augstums(parents[i]) + 1
       ## return augstumi[i]
    
    ##for i in range(n):
      ##  augstums(i)
    ##return int(max(augstumi))
       

def main():
    check = input()
    if "F" in check:
        file = input()
        if "a" not in file:
            print("Error")
        else:
            izmantot = 'test/' + file
            open_file = open(izmantot, 'r', encoding='UTF-8')
            saturs = open_file.readlines()

            koks = saturs[1]
            daudzums = saturs[0]
    elif "I" in check:
    
        koks = input()
        daudzums = input()

    koks = koks.split(" ")
    koks = [int(i) for i in koks]
    sakums = 0

    p = 0
    for k in koks:
        if k == -1:
            sakums = p
        p = p+1

    augstums = compute_height(sakums, koks)

    print(augstums)
 

          ##  with open ("test/" + file, "r", encoding='UTF-8') as f:
            ##    ne = int(f.readline())
              ##  parent = list(map(int, f.readline().split()))
        ##else:
          ##  print("Error")
    ##
      ##  ne = int(input())
        ##parent = list(map(int, input().split()))
    ##else:
      ##  print("Nav derīgs kods")
    ##print(compute_height(ne, parent))
        

    
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
#main()
# print(numpy.array([1,2,3]))