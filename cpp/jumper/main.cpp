#include <iostream>
#include <Jumper.h>

using namespace std;

int main(int argc, char* argv[]){

    Jumper rabbit;
    vector<Edge> edges_01 =
    {
        {0,1}, {0,2},
        {1,3}, {1,4},
        {2,6},
        {4,5},{4,6}
    };
    rabbit.jump(edges_01, 7, 0);
    vector<float> end_01 = rabbit.whereYouEnd();
    for(float& res: end_01) cout << res << " ";
}