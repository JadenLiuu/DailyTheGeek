#ifdef E2E_TEST
#include "Test.h"

Jumper rabbit;

template <typename T>
bool Test::approximatelyEqual(const T a, const T b){
    static_assert(std::is_arithmetic<T>::value, "Not an arithmetic type");
    return fabs(a - b) <= 1e-5;
}

template <typename T>
void Test::expect_probSum_equals1(const vector<T>& a, bool &exception_caught){
    if(exception_caught) return;
    try{
        static_assert(std::is_arithmetic<T>::value, "Not an arithmetic type");
        T sum = 0.0;
        for(const T& num: a) sum += num;
        if(!approximatelyEqual(sum, 1.0f)) throw "Invalid Probability!";
    } catch (const char* msg){
        exception_caught = true;
        cerr << "[FAILED]" << msg << endl;
    } catch(std::exception e){
        cerr << "[FAILED]" << e.what() << endl;
        exception_caught = true;
    }
}

template <typename T>
void Test::expect_same(vector<T> a, vector<T> b, bool& exception_caught){
    if(exception_caught) return;
    try{
        if(a.size()!=b.size()) throw "Vector Size Dismatch";
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
        for(int i=0; i<a.size(); i++){
            if(!approximatelyEqual(a[i],b[i])) {
                throw "Meber Dismatch!";
            }
        }
    } catch(char const* msg){
        exception_caught = true;
        cerr << "[FAILED]" << msg << endl;
    } catch(std::exception e){
        exception_caught = true;
        cerr << "[FAILED]" << e.what() << endl;
    }
}

void Test::general_test(vector<float>& res, 
                        vector<float>& prediction, 
                        int test_case){
    bool exception_caught = false;
    expect_probSum_equals1(res, exception_caught);
    expect_probSum_equals1(prediction, exception_caught);
    expect_same(prediction, res, exception_caught);
    if(!exception_caught) cout << "[PASS] " << test_case << endl;
    else cout << "[FAILED] " << test_case << endl;
}

void Test::test_01(){
    vector<Edge> edges =
    {
        {4, 2}, {4, 6}, {4, 5}, {4, 3},
        {5, 1}, {5, 0}
    };
    rabbit.jump(edges, 7, 4);
    vector<float> res = {
        0.25, 0.25, 0.25, 0.125, 0.125 
    };
    vector<float> prediction = rabbit.whereYouEnd();
    general_test(res, prediction, 1);
};

void Test::test_02(){
    vector<Edge> edges =
    {
        {0,1}, {0,2},
        {1,3}, {1,4},
        {2,6},
        {4,5},{4,6}
    };
    rabbit.jump(edges, 7, 0);
    vector<float> res = {
        0.125, 0.625, 0.35
    };
    vector<float> prediction = rabbit.whereYouEnd();
    general_test(res, prediction, 2);
};

void Test::test_03(){    
    vector<Edge> edges =
    {
        {0,1}, {0,2},
        {1,3}, {1,4},
        {2,6},
        {4,5},{4,6}
    };
    rabbit.jump(edges, 7, 0);
    vector<float> res = {
        0.125, 0.625, 0.25
    };
    vector<float> prediction = rabbit.whereYouEnd();
    general_test(res, prediction, 3);
};

void Test::test_04(){
    vector<Edge> edges =
    {
        {4, 2}, {4, 1}, {4, 0},
        {1, 3}, {1, 2}
    };
    rabbit.jump(edges, 5, 4);
    vector<float> res = {
        1.0f/3.0f, (1.0f/3.0f)*0.5, 1.0f/3.0f + (1.0f/3.0f)*0.5
    };
    vector<float> prediction = rabbit.whereYouEnd();
    general_test(res, prediction, 4);
};

#endif