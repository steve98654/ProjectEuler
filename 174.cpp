// Project Euler Problem 174
#include<cmath>
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;


int main()
{

    long cnt = 0;
    long mxsqr = pow(10,6);
    long nmx   = pow(10,6);
    long mxstr = 0;
    vector<long> tvec;

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
                tvec.push_back((2*n)*(2*n)-(2*m)*(2*m));
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
                tvec.push_back((2*n-1)*(2*n-1)-(2*m-1)*(2*m-1));
            }
        }
    }

    sort(tvec.begin(),tvec.end());
    vector<long> cntvec;
    vector<long> numvec;

    cntvec.push_back(1);
    numvec.push_back(tvec[0]);

    for(int i = 1; i!= tvec.size(); i++)
    {
        if(tvec[i] == tvec[i-1])
        {
            cntvec.back()++;
        }
        else
        {
            cntvec.push_back(1);
            numvec.push_back(tvec[i]);
        }
    }

    for(int j = 0; j != 12; j++)
    {
        cout << "Num: " << numvec[j] << " Count: " << cntvec[j] << endl;
    }

    //Find number of counts with values between 1 and 10

    long ncnt=0;

    for(int k = 0; k!=cntvec.size(); ++k)
    {
        if(1 <= cntvec[k] && cntvec[k] <= 10)
            ++ncnt;
    }

    cout << ncnt << endl;
    return 0;
}

