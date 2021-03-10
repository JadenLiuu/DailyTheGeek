#ifdef E2E_TEST
#include <Test.h>
#endif

#include <iostream>
#include <Jumper.h>

using namespace std;
int main(int argc, char* argv[]){

#ifdef E2E_TEST
    cout << "=== TEST ===" << endl;
    Test test_agent;
    test_agent.run_all();
#endif
    return 0;
}