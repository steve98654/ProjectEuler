#include <iostream>
#include <cmath>

int main(){

    // Let's assume that a>0 and b>0

    long a,b,p;
    double eps = 1e-8;

    // bmax = 12500000 should be the most that we need

    
    long pmax = 10000;
    long cnt = 0;
    long amx;
    
    for(p=3; p<pmax; ++p)
    {
        for(long b = 1; b < p/2; ++b)
        {
            amx = std::min(b,(1-2*b*p+p*p)/(2*p-2*b)); 
            for(long a = 1; a <= amx ; ++a)
            {
                if( std::abs(-2*a*b+2*p*(a+b)-p*p-1) < eps)
                //if( std::abs(c - int(c)) < eps && c <= cmax)
                {
                    ++cnt;
                }
            }
        }
    }

    std::cout << "Count is: " << cnt << std::endl;

    return 0;
}

