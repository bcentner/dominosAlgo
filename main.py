from algos import *

def main():
    print("---Welcome to Dominos---\n")
    domCount = input("how many dominos?\n")
    this_list = []
    for i in range(0, int(domCount)):
        cur = input("numbers seperated by a space\n")
        sample = cur.split()
        this_list.append([int(sample[0]), int(sample[1])])

    print(this_list)
    strt = int(input("starting domino: "))
    valid_starts = [x for x in this_list if x[0]== strt or x[1]==strt]
    
    # no way to start
    if len(valid_starts) < 1:
        print("You have no starting options\n")
        return 
    pass

    txt = input("select algo type: ")
    print(txt)
    if int(txt)==1:
        print("branch and bound starting...")
        branchBound()
    elif int(txt)==2:
        print("starting greedy")
        greedy()

if __name__=='__main__':
    main()
