# TODO: error checking on user input 
def branchBound():
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

    longest = 0
    count = 0
    longest_li = []
    cur = [valid_starts[0]]
    for li_pair in valid_starts:
        cur = [valid_starts[count]]
        # FIXME: need loop here
        if li_pair[0] == cur[-1]:
            cur.append(li_pair[0])
        elif li_pair[1] == cur[-1]:
            cur.append(li_pair[-1])

        count += 1
        pass