#include <bits/stdc++.h>
using namespace std;
// DFS function to visit nodes
void dfs(int node, vector<int> adj[], int visited[], vector<int> &ls)
{
  // Mark the node as visited
  visited[node] = 1;
  // Add node to the list
  ls.push_back(node);
  // Visit all adjacent nodes
  for (auto it : adj[node])
  {
    if (!visited[it])
    {
      dfs(it, adj, visited, ls); // Recurse for unvisited node
    }
  }
}
// Function to perform DFS starting from node 0
vector<int> visiting_array(vector<int> adj[], int nodes)
{
  // Declare the visited array to mark visited nodes
  int visited[nodes] = {0};
  // List to store the result of DFS
  vector<int> ls;
  // Call DFS starting from node 0
  dfs(0, adj, visited, ls);
  return ls;
}
// Function to add an edge to the undirected graph
void addEdge(vector<int> adj[], int node, int adjacent)
{
  adj[node].push_back(adjacent);
  adj[adjacent].push_back(node);
}
int main()
{
  // Create a graph with 6 nodes (0 to 5)
  vector<int> adj[6];
  // Add edges to the graph
  addEdge(adj, 0, 1);
  addEdge(adj, 1, 2);
  addEdge(adj, 1, 3);
  addEdge(adj, 0, 4);
  // Perform DFS starting from node 0
  vector<int> ans = visiting_array(adj, 6);
  // Print the DFS result
  for (auto it : ans)
  {
    cout << it << " ";
  }
  return 0;
}
