#ifndef JUMPER_H
#define JUMPER_H

#include <Jumper.h>
#include <Graph.h>
#include <queue>
using namespace std;

class Jumper
{
private:
    vector<Node*> End;
    Graph* graphAgent;
    
public:
    Jumper(){};
    void jump(vector<Edge>& edges, int N, int root){
        graphAgent = new Graph(edges, N);
        queue<Node*> q;
        Node* Root = graphAgent->graph[root];
        Root->prob = 1.0;
        q.push(Root);

        while(q.size()){
            int n_child = q.front()->childs.size();
            if(n_child == 0) End.push_back(q.front());
            float child_prob = (n_child>0)? (1.0/n_child) : 0.0;
            for(Node* child: q.front()->childs){
                child->n_parent -= 1;
                child->prob += (q.front()->prob * child_prob);
                if(child->n_parent == 0) q.push(child);
            }
            q.pop();
        }
    }
    vector<float> whereYouEnd(){
        vector<float> end_prob;
        for(Node* end: End){
            end_prob.push_back(end->prob);
        }
        if(graphAgent) delete graphAgent;
        End.clear();
        return end_prob;
    }
};

#endif