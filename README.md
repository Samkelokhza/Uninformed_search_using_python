# Uninformed Search Using Python 

## Overview
This project demonstrates the implementation of **uninformed search algorithms** on a tree graph using Python.  
The algorithms explored include:
- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **Iterative Deepening Depth-First Search (IDDFS)**

The graph is modeled as an **adjacency list**, and each algorithm is executed from the root node.  
Outputs highlight the unique traversal strategies of each method, with IDDFS incorporating a depth limit.

---

## Objectives
- Implement BFS, DFS, and IDDFS in Python.
- Represent a tree graph using adjacency lists.
- Execute searches from the root node.
- Compare traversal strategies and outputs.
- Demonstrate the role of depth limits in IDDFS.

---

## Project Structure
- `bfs.py` – Implementation of Breadth-First Search.
- `dfs.py` – Implementation of Depth-First Search.
- `iddfs.py` – Implementation of Iterative Deepening DFS.
- `graph.py` – Adjacency list representation of the tree graph.
- `README.md` – Documentation for the project.

---

## ⚙️ How It Works
1. **Graph Representation**  
   The tree is represented as an adjacency list (dictionary of nodes and their children).

2. **Breadth-First Search (BFS)**  
   - Explores nodes level by level.
   - Uses a queue to manage traversal order.

3. **Depth-First Search (DFS)**  
   - Explores nodes along each branch before backtracking.
   - Uses recursion or a stack.

4. **Iterative Deepening DFS (IDDFS)**  
   - Combines DFS with a depth limit.
   - Repeatedly applies DFS with increasing depth until the target is found.

python iddfs.py
