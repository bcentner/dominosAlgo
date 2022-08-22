# TODO: error checking on user input 


def greedy():
    pass

def branchBound():

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