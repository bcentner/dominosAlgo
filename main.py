from algos import *

def main():
    print("---Welcome to Dominos---\n")
    domCount = input("how many dominos?\n")
    all_dom = []
    for i in range(0, int(domCount)):
        cur = input("numbers seperated by a space\n")
        sample = cur.split()
        all_dom.append([int(sample[0]), int(sample[1])])

    print(all_dom)
    strt = int(input("starting domino: "))
    valid_starts = [x for x in all_dom if x[0]== strt or x[1]==strt]
    
    # no way to start
    if len(valid_starts) < 1:
        print("You have no starting options\n")
        return 
    pass

    txt = input("select algo type: ")
    print(txt)
    if int(txt)==1:
        print("branch and bound starting...")
        branchBound(all_dom, valid_starts)
    elif int(txt)==2:
        print("starting greedy...")
        greedy(all_dom, strt)

if __name__=='__main__':
    main()
