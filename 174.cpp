// Project Euler Problem 173
// Goal: Brute force counting with a bound (mxstr) put on the inner removed square
//       to remove lamina with too many squares.
#include<cmath>
#include<iostream>

using namespace std;

int main()
{

    long cnt = 0;
    long mxsqr = pow(10,6);
    long nmx   = pow(10,6);
    long mxstr = 0;

    // Even number of squares in outer square
    for(long n = 2; n <= nmx; n++)
    {
        if((2*n)*(2*n) - mxsqr > 0)
        {
            mxstr = floor(sqrt((2*n)*(2*n)-mxsqr)/2);
        }
        else
        {
            mxstr = 1;
        }
        
        for(long m = mxstr; m <= n-1; m++)
        {
            if((2*n)*(2*n) - (2*m)*(2*m) <= mxsqr)
            {
                cnt++;
            }
        }
    }

    // Odd number of squares in outer square
    for(long n = 2; n <= nmx; n++)
    {
        if((2*n-1)*(2*n-1) - mxsqr > 0)
        {
            mxstr = floor(sqrt((2*n-1)*(2*n-1)-mxsqr+1)/2);
        }
        else
        {
            mxstr = 1;
        }
        
        for(long m = mxstr; m <= n-1; m++)
        {
            if((2*n-1)*(2*n-1) - (2*m-1)*(2*m-1) <= mxsqr)
            {
                cnt++;
            }
        }
    }

    cout << cnt << endl;

    return 0;
}
