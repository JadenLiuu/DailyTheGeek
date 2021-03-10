#ifndef GRAPH_H
#define GRAPH_H
#include <iostream>
#include <vector>
using namespace std;

// Data structure to store a graph edge
struct Edge {
    int src, dest;
};

struct Node
{
    int n_parent;
    float prob;
    vector<Node*> childs;
    Node(): n_parent(0), prob(0.0) {};
};
 
class Graph
{
    int N; // total number of nodes in the graph
    void construct_edge_info(vector<Edge>& edges){
        vector<int> parentList(N, 0);
        for (unsigned i = 0; i < edges.size(); i++){
            parentList[edges[i].dest]++;
            adjList[edges[i].src].push_back(edges[i].dest);
        }
        for(unsigned i = 0; i < N; i++){
            Node* n = new Node();
            n->n_parent = parentList[i];
            graph[i] = n;
        }
    }
    void connect_graph(){
        for(unsigned i = 0; i < N; i++){
            for(int& child_idx: adjList[i]){
                graph[i]->childs.push_back(graph[child_idx]);
            }
        }
    }

public:
    vector<vector<int>> adjList;
    vector<Node*> graph;
    Graph(vector<Edge> edges, int N)
    {
        this->N = N;
        graph.resize(N);
        adjList.resize(N);
        construct_edge_info(edges);
        connect_graph();        
    }
    ~Graph(){
        for(Node* n: graph) {
            if(n) delete n;
        }
    }
};
#endif
