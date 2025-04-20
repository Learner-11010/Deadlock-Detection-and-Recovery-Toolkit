import networkx as nx

def detect_deadlock(graph):
    
    try:
        cycle = nx.find_cycle(graph, orientation="original")  # Detects cycles (deadlock)
        return cycle  # Returns the cycle causing deadlock
    except:
        return None  # No deadlock found
