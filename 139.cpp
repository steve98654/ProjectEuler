#include<cmath>
#include<iostream>
#include<boost/math/common_factor.hpp>

int main(){

    int cnt = 0;
    int lim = 1e8;
    int a=0,b=0,c=0;

    int mxvl = 10000;

    for(int m = 1; m < mxvl; ++m)
    {
        for(int n = 1; n < mxvl; ++n)
        {
            a = m*m-n*n;
            b = 2*m*n;
            c = m*m+n*n;

            if(a+b+c < lim && c%(b-a)==0 && boost::math::gcd(a,b)==1 
                && boost::math::gcd(a,c)==1 && boost::math::gcd(b,c)==1)
            {
                cnt += lim/(a+b+c);
            }
        }
    }

    std::cout << cnt << std::endl;
    return 0;
}

