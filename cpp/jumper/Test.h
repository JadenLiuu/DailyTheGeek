#ifndef TEST_H
#define TEST_H

#ifdef E2E_TEST
#include <Jumper.h>

#include <assert.h>
#include <ctgmath>
#include <algorithm>
#include <vector>

using namespace std;
class Test
{
private:
    void test_01();
    void test_02();
    void test_03();
    void test_04();
    void general_test(vector<float>& res, 
                      vector<float>& prediction, 
                      int test_case);
    
    template <typename T>
    bool approximatelyEqual(const T a, const T b);

    template <typename T>
    void expect_probSum_equals1(const vector<T>& a, bool &exception_caught);

    template <typename T>
    void expect_same(vector<T> a, vector<T> b, bool& exception_caught);

public:
    void run_all(){
        test_01();
        test_02();
        test_03();
        test_04();
    }
};

#endif
#endif
