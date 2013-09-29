//Project Euler Problem 127.cpp

#include <boost/math/common_factor.hpp>
#include <algorithm>
#include <iostream>
#include <vector> 
#include <time.h>

std::vector<int> factor(int x)
{
    std::vector<int> factors;
    int i = 2;

    while(x>1)
    {
        if(x%i == 0)
        {
            x = x/i;
            factors.push_back(i);
        }
        else
        {
            i++;
        }
    }

    return factors;
}

long long prod(std::vector<int> vec)
{
    long long prd = 1;
    for(int i=0; i<vec.size(); i++)
    {
        prd *= vec[i];
    }

    return prd;
}

int main()
{

    const int cmx = 120000;
    long long sm = 0;

    std::vector<std::vector<int> > gcdtb;

    //    gcdtb.resize(cmx);
    //for(int i=0; i < cmx; ++i)
    //    gcdtb[i].resize(cmx);

    //for(int i = 0; i < cmx; i++)
    //{
    //    if(i%1000 == 0)
    //        std::cout << i << std::endl;
        
    //    for(int j = 0; j < cmx; j++)
    //    {
    //        gcdtb[i][j] = boost::math::gcd(i,j);
    //    }
    //}
        
    clock_t t1,t2;

    t1 = clock();

    std::vector<std::vector<int> > fcts;
    
    for(int i=0; i < cmx; ++i)
        fcts.push_back(factor(i));    

    for(int a=1; a < cmx-1; ++a)
    {
        if(a%100 == 0)
            std::cout << a << std::endl;

        for(int b=a+1;b<cmx-a;++b)
        {
            int c = a + b;
            if(boost::math::gcd(a,b)==1 && boost::math::gcd(a,c)==1 && boost::math::gcd(b,c)==1)
            {
                std::vector<int> fac1,fac2,fac3,fac;
                //fac1 = factor(a);
                //fac2 = factor(b);
                //fac3 = factor(c);
                fac1 = fcts[a];
                fac2 = fcts[b];
                fac3 = fcts[c];
                fac1.insert(fac1.end(),fac2.begin(),fac2.end());
                fac1.insert(fac1.end(),fac3.begin(),fac3.end());

                sort(fac1.begin(),fac1.end());
                fac1.erase(std::unique(fac1.begin(), fac1.end()), fac1.end());

                if(prod(fac1) < c)
                   sm += c;
                }
            }
    }

    t2 = clock();

    std::cout << sm << std::endl;

    float diff = ((float)t2-(float)t1);
    std::cout << "Time was: " << diff/CLOCKS_PER_SEC << std::endl;

    //int val = boost::math::gcd(6,15); 

    //std::cout << val << std::endl;

    //std::vector<int> tstvec;
    
    //int tstint = 4*4*5*5*6;
    //tstvec = factor(tstint);

    //sort(tstvec.begin(), tstvec.end());
    //tstvec.erase(unique(tstvec.begin(), tstvec.end()), tstvec.end());

    //    for(int i=0; i<tstvec.size();i++)
    //{
    //    std::cout << tstvec[i] << std::endl;
    // }

    //long long mxvl = 120000;
    //long long outvl = mxvl*mxvl*mxvl;

    //std::cout << mxvl*mxvl << std::endl;
    //std::cout << outvl << std::endl;

    return 0;
}

