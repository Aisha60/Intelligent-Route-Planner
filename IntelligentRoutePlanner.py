
from queue import deque
from queue import PriorityQueue
import pandas as  pd

# Read the Excel file
df = pd.read_excel('RoutesDataset.xlsx')

# Initialize an empty network graph
network_graph = {}

# Iterate over the rows in the DataFrame and populate the network graph
for index, row in df.iterrows():
    source_node = row['Source Node']
    destination_node = row['Destination Node']
    distance = row['Distance (km)']
    latency = row['Latency (ms)']
    bandwidth = row['Bandwidth (Mbps)']
    reliability = row['Reliability (%)']
    
    # Add the edge from source to destination node
    if source_node not in network_graph:
        network_graph[source_node] = {}
    network_graph[source_node][destination_node] = {'distance': distance, 'latency': latency, 'bandwidth': bandwidth, 'reliability': reliability}
    
    # Add the edge from destination to source node
    if destination_node not in network_graph:
        network_graph[destination_node] = {}
    network_graph[destination_node][source_node] = {'distance': distance, 'latency': latency, 'bandwidth': bandwidth, 'reliability': reliability}
print (network_graph)


# Uniform cost search algorithm for finding the most optimal route based on actual distance
def uniformCost_search(graph, source, destination):
    priority_queue = PriorityQueue()
    priority_queue.put((0, source, []))  # (cost, node, path)
    visited = set()
    
    while not priority_queue.empty():
        cost, node, path = priority_queue.get()
        print("Exploring node:", node, "with path:", path)
        if node == destination:
            return path + [node]
        if node in visited:
            continue
        visited.add(node)
        for neighbor, attributes in graph.get(node, {}).items():
            new_cost = cost + attributes['distance']
            priority_queue.put((new_cost, neighbor, path + [node]))
    return None

def find_route_with_minbandwidth(network_graph, source, destination, min_bandwidth):
    visited = set()  # Track visited nodes to avoid cycles
    queue = deque([(source, [source])])  # Queue for BFS traversal with paths

    while queue:
        node, path = queue.popleft()
        if node == destination:
            return path  # Found the destination!
        if node in visited:
            continue
        visited.add(node)

        for neighbor, edge_info in network_graph[node].items():
            if neighbor not in visited and edge_info['bandwidth'] >= min_bandwidth:
        # Check bandwidth before adding to the queue
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return None  # No path found that meets the requirement

def find_route_with_minLatency(network_graph, source, destination, min_latency):
    visited = set()  # Track visited nodes to avoid cycles
    queue = deque([(source, [source])])  # Queue for BFS traversal (node,path)

    while queue:
        node, path = queue.popleft()
        if node == destination:
                return path  # Found the destination!
        if node in visited:
                continue
        visited.add(node)

        for neighbor, edge_info in network_graph[node].items():
                if neighbor not in visited and edge_info['latency'] <= min_latency:
                        new_path = path + [neighbor]
                        queue.append((neighbor, new_path))

    return None  # No path found

def find_route_with_mostReliability(network_graph, source, destination, min_reliability):
    visited = set()  # Track visited nodes to avoid cycles
    queue = deque([(source, [source])])  # Queue for BFS traversal (node,path)

    while queue:
        node, path = queue.popleft()
        if node == destination:
                return path  # Found the destination!
        if node in visited:
                continue
        visited.add(node)

        for neighbor, edge_info in network_graph[node].items():
                if neighbor not in visited and edge_info['reliability'] >= min_reliability:
                        new_path = path + [neighbor]
                        queue.append((neighbor, new_path))

    return None  # No path found

# User interface to select the type of solution
def select_solution_type():
    print ("------------------------------------MENU---------------------------------------")
    print("Select the type of solution:")
    print("1. Most optimal route based on actual distance (Uniform Cost search)")
    print("2. Route that satisfies minimum bandwidth constraint")
    print("3. Route that satisfies minimum latency constraint(Timely delivery)")
    print("4. Route that is most fault-tolerant")
    print("--------------------------------------------------------------------------------")
    choice = input("\nEnter your choice (1, 2, 3, or 4): ")
    return int(choice)

def main():
    
    while True:
        
        while True:
                source = 'Node'+ input("Enter the source node e.g 1: ")
                destination = 'Node'+ input("Enter the destination node e.g 4: ")
                if source in network_graph and destination in network_graph:
                        print("Source and destination nodes are valid.")
                        break
                else:
                        print("Invalid source or destination node.")
                        
        solution_type = select_solution_type()
    
        if solution_type == 1:
        # Uniform cost search for finding the most optimal route based on distance
            route = uniformCost_search(network_graph, source, destination)
            if route:
                print("Most optimal route based on distance:", route)
            else:
                print("No route found.")
        
        # Constraints satisfaction route finding using BFS with CSP
        elif solution_type in [2, 3, 4]:

            if solution_type == 2:
                minimum_bandwidth = int(input("Enter your minimum bandwidth requirement(50, 200, 150 , etc): "))
                route = find_route_with_minbandwidth(network_graph,source,destination, minimum_bandwidth)
                
            elif solution_type == 3:
                minimum_latency = int(input("Enter your minimum latency requirement(5, 2, 10 etc): "))
                route = find_route_with_minLatency(network_graph,source,destination, minimum_latency)
                
            elif solution_type == 4:
                min_reliability = int(input("Enter your minimum reliability requirement for route (99, 90, 94, etc): "))
                route = find_route_with_mostReliability(network_graph,source,destination, min_reliability)
            
            if route:
                print("Route satisfying the constraint is:", route)
            else:
                print("No route satisfying the constraint found.")
        
        else:
            print("Invalid choice.")
            
        choice = input("\nDo you want to find another route (y/n)? ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()



