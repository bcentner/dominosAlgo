# TODO: error checking on user input 


def greedy(dominos, start_num : int):
    count = 0
    longest = 0
    longest_li = []
    real_hash = buildHash(dominos)
    real_strts = list(real_hash[start_num])

    while len(real_strts):
        cur = real_strts.pop(0)
        cur_li = []
        cur_li.append(cur)
        
        # copy hash map and git rid of the current starter block
        copy_hash = dict(real_hash)
        copy_hash[start_num].pop(count)

        end = False
        while not end:
            for my_dom in copy_hash[cur]:
                if len(copy_hash[my_dom]) > 0:
                    cur_li.append(my_dom)
                    cur = my_dom
                pass

        if len(cur_li) > longest:
            longest = len(cur_li)
            longest_li = cur_li

        count += 1
        pass
    
    pass

def branchBound(dominos, starts):

    longest = 0
    count = 0
    longest_li = []
    cur = [starts[0]]

    for li_pair in starts:
        cur = [starts[count]]

        # FIXME: need loop here
        
        if li_pair[0] == cur[-1]:
            cur.append(li_pair[0])
        elif li_pair[1] == cur[-1]:
            cur.append(li_pair[-1])

        count += 1
        pass
    pass


# helper functions
def buildHash(dominos):
    dom_hash = {}
    for pair in dominos:
        if pair[0] not in dom_hash:
            dom_hash[pair[0]] = [pair[1]]
        else:
            dom_hash[pair[0]].append(pair[1])

        if pair[1] not in dom_hash:
            dom_hash[pair[1]] = [pair[0]]
        else:
            dom_hash[pair[1]].append(pair[0])

    return dom_hash