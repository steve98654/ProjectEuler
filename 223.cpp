#include <iostream>
#include <cmath>

int main(){

    // Let's assume that a>0 and b>0

    long a,b;
    double c;
    double eps = 1e-8;

    // bmax = 12500000 should be the most that we need

    
    long pmax = 250000;
    long bmax = pmax/2;
    
    long cmax = 1300;
    long cnt = 0;

    for(long b = 1; b < bmax; ++b)
    {
        for(long a = 1; a <= b; ++a)
        {
            c = std::sqrt(a*a+b*b - 1);
            if( std::abs(c - int(c)) < eps && a+b+c <= pmax)
            //if( std::abs(c - int(c)) < eps && c <= cmax)
            {
                ++cnt;
            }
        }
    }

    std::cout << "Count is: " << cnt << std::endl;

    return 0;
}

