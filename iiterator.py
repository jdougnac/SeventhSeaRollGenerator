import itertools


target_number = 10
roll_list =[]
roll_list.reverse()
exitos = []

def iterate():
    for tolerance in range(0,10): 
        for i in range(1, len(roll_list)+1):
        
            for seq in itertools.combinations(roll_list, i):
                if sum(seq)==target_number+tolerance or sum(seq) == target_number:
                    exitos.append(list(seq))
                    for element in seq:
                        if element in roll_list:
                            roll_list.remove(element)
                    break                   


def start_iterating():
    while sum(roll_list)>=target_number:
        iterate()
    return [exitos, roll_list]
    




