domCount = input("how many dominos?\n")
this_list = []
for i in range(0, int(domCount)):
    cur = input("numbers seperated by a space\n")
    sample = cur.split()
    this_list.append({int(sample[0]), int(sample[1])})

strt = input("starting domino")
valid_starts = [x for x in this_list if x.0== start or x.1==start]
print(valid_starts)
print(this_list)
