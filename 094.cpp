// Project Euler Problem 94 solution 

//We have an error in abs.  Find the proper usage of abs() in the math.h library!!! 

//Compute with: g++ 094.cpp -lgmp

#include <iostream>
#include <math.h>
#include <time.h>
#include <stdlib.h>

long double Ara(long int a, long int b, long int c)
{

    long double s = (a+b+c)/2.0;
    //    return  sqrt(s*(s-a)*(s-b)*(s-c));
    return sqrt(s*(s-c)); //Note that we only need this to be a perfect square
}

int main()
{
    long int mxi = 34*1e7;
    long double tol = 1e-8;
    long int mxp = 1e9;
    long int cnt = 0;
    long int prmtot = 0;

    clock_t start = clock();

    long double tp1 = 0;
    long double tp2 = 0;
    long double t1err = 0;
    long double t2err = 0;

    for(long int i = 2; i <= mxi; i++)
    {
        tp1 = Ara(i,i,i-1);
        tp2 = Ara(i,i,i+1);
        t1err = fabs(tp1 - round(tp1));
        t2err = fabs(tp2 - round(tp2));

        if((t1err < tol) && (3*i - 1) < mxp)
        {
            cnt++;
            prmtot += 3*i-1;
            std::cout << i << ",";
        }
        if((t2err < tol) && (3*i + 1) < mxp)
        {
            cnt++;
            prmtot += 3*i + 1;
            std::cout << i << ",";
        }
    }

    clock_t end = clock();
    float diff ((float)end - (float)start);

    std::cout << "Total time is: " << diff/CLOCKS_PER_SEC << std::endl;
    std::cout << "Count: " << cnt << " Perm Total: " << prmtot << std::endl;
    std::cout << tp1 << tp2 << t1err << t2err << std::endl;
    return 0;
}   

