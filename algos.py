# TODO: error checking on user input 


def greedy(dominos, starts):
    count = 0
    
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