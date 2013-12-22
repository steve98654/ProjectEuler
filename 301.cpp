#include <iostream>
#include <cmath>

using namespace std;

// Currently does not work!!

int main(){

    long cnt = 0;
    long long n,n2,n3;

    for(n = 1; n <= pow(2,10); ++n)
    {
        if( n^(2*n2)^(3*n3) == 0)
        {
            ++cnt;
        }
    }

    cout << cnt << endl;

    int xor1 = n^n2;
    int xor2=(n^n2)^n3;

    cout << n << "  " << xor1 << " " << xor2 << endl;

    int val = 45^43; 
    cout << val << endl;

    return 0;
}
