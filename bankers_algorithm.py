def is_safe_state(available, max_demand, allocation):

    import copy
    
    num_processes = len(max_demand)
    num_resources = len(available)
    
    work = copy.deepcopy(available)
    finish = [False] * num_processes
    safe_sequence = []
    
    while len(safe_sequence) < num_processes:
        found = False
        for i in range(num_processes):
            if not finish[i]:
                need = [max_demand[i][j] - allocation[i][j] for j in range(num_resources)]
                if all(need[j] <= work[j] for j in range(num_resources)):
                    safe_sequence.append(i)
                    work = [work[j] + allocation[i][j] for j in range(num_resources)]
                    finish[i] = True
                    found = True
                    break
        if not found:
            return False, []  
    
    return True, safe_sequence
