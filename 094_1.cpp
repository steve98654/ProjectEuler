// Project Euler Problem 94 solution 

//We have an error in abs.  Find the proper usage of abs() in the math.h library!!! 

//Compute with: g++ 094.cpp -lgmp

#include <iostream>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <gmp.h>

long double Ara(long a, long b, long c)
{
    mpf_t ss;
    mpf_init2(ss,256);

    long double s = (a+b+c)/2.0;
    ss = (a + b + c)/2.0;

    return sqrt(s*(s-a)*(s-b)*(s-c));
}

int main()
{
    long mxi = 2*1e6;
    long double tol = 1e-8;
    long mxp = 1e9;
    long cnt = 0;
    long prmtot = 0;

    clock_t start = clock();

    long double tp1 = 0;
    long double tp2 = 0;
    long double t1err = 0;
    long double t2err = 0;

    for(long i = 2; i <= mxi; i++)
    {
        tp1 = Ara(i,i,i-1);
        tp2 = Ara(i,i,i+1);
        t1err = fabs(tp1 - round(tp1));
        t2err = fabs(tp2 - round(tp2));

        if((t1err < tol) && (3*i - 1) < mxp)
        {
            cnt++;
            prmtot += 3*i-1;
        }
        if((t2err < tol) && (3*i + 1) < mxp)
        {
            cnt++;
            prmtot += 3*i + 1;
        }
    }

    clock_t end = clock();
    float diff ((float)end - (float)start);

    std::cout << "Total time is: " << diff/CLOCKS_PER_SEC << std::endl;
    std::cout << "Count: " << cnt << " Perm Total: " << prmtot << std::endl;
    std::cout << tp1 << tp2 << t1err << t2err << std::endl;
    return 0;
}   

