#include <bits/stdc++.h>
using namespace std;
// BFS function
vector<int> bfs(vector<int> adj[], int nodes)
{
  // initialize visited array
  int visited[nodes] = {0};
  visited[0] = 1;
  // declare queue
  queue<int> qu;
  qu.push(0);
  // initialize bfs result vector
  vector<int> bfs;
  while (!qu.empty())
  {
    int node = qu.front();
    qu.pop();
    bfs.push_back(node);
    // point to the node and check for all adjacent nodes
    for (auto it : adj[node])
    {
      if (!visited[it])
      {
        // if the node in adjacency list is not visited, mark it and push into queue
        visited[it] = 1;
        qu.push(it);
      }
    }
  }
  return bfs;
}
// Function to add edge to the graph
void addEdge(vector<int> adj[], int node, int adjacent)
{
  adj[node].push_back(adjacent);
  adj[adjacent].push_back(node);
}
int main()
{
  // creating a graph with 6 nodes (0 to 5)
  vector<int> adj[6];
  // adding edges to the graph
  addEdge(adj, 0, 1);
  addEdge(adj, 1, 2);
  addEdge(adj, 1, 3);
  addEdge(adj, 0, 4);

  // Perform BFS starting from node 0
  vector<int> ans = bfs(adj, 5);
  // Print BFS result
  for (auto it : ans)
  {
    cout << it << " ";
  }
  return 0;
}
