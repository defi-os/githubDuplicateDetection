import random
def select_unique_pairs(lst,number_pairs,max_iterations):
    pairs = set()
    iterations = 0
    
    while len(pairs) < number_pairs and iterations < max_iterations:
        pair = random.sample(lst, 2)
        if pair[0] != pair[1] and pair not in list(pairs):
            pairs.add(tuple(pair))
            
        iterations += 1
    return list(pairs)