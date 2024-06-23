
The proposed system aims to provide a solution to the problem by implementing a
routing system capable of finding routes based on different criteria such as actual
distance, minimum bandwidth, minimum latency, and maximum reliability.
This desktop based command line inteface system is developed using python and utilization of AI path search optimization algorithms.

The system is focused on pathfinding within a pre-defined, static network structure. 

**Network Representation:** 
The system represents the network as a graph, where
nodes signify locations and connections (edges) represent pathways between them. Each connection can be assigned attributes like distance, bandwidth, latency, and
reliability. 

**Pathfinding Algorithms**: 
The system implements algorithms like Uniform Cost
Search (UCS) and Breadth-First Search (BFS) to explore the network and identify
paths. UCS allows for flexible cost definitions, considering various network
characteristics. BFS is used for constraint-based searches where paths must meet
minimum requirements for bandwidth, latency, or reliability.

**Tools and Technologies**:

**Graph Representation**                 Python dictionaries (for initial representation), Excel (for data storage),
**Data Analysis and Manipulation**       pandas,
**Search Algorithms Implementation**     Python,
**User Interface and Input Handling**    Python (user input/output functions, cmd),
**IDE**                                  Visual Studio Code
