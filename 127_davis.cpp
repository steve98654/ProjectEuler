//Project Euler Problem 127.cpp
//Davis's improvements

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
            // Davis: don't save duplicate factors.  Your code was spending lots of time
            // removing them later and never used the duplicates.  So do it before hand
            // once rather than over and over.
            if (factors.size() == 0 || factors.back() != i)
                factors.push_back(i);
        }
        else
        {
            i++;
        }
    }

    return factors;
}

// Davis, always take arguments by reference to avoid copying them.  The original code made
// a memory allocation and then copies the vector into it every time prod was called.
long long prod(const std::vector<int>& vec)
{
    long long prd = 1;
    for(int i=0; i<vec.size(); i++)
    {
        prd *= vec[i];
    }

    return prd;
}

bool have_common_factor( const std::vector<int>& fac1, const std::vector<int>& fac2)
{
    int i = 0;
    int j = 0;
    while (i < fac1.size() && j < fac2.size())
    {
        if (fac1[i] < fac2[j])
            ++i;
        else if (fac1[i] > fac2[j])
            ++j;
        else
            return true;
    }
    return false;
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

    std::vector<int> fac;
    for(int a=1; a < cmx-1; ++a)
    {
        if(a%100 == 0)
            std::cout << a << std::endl;

        for(int b=a+1;b<cmx-a;++b)
        {
            int c = a + b;
            if(!have_common_factor(fcts[a], fcts[b]) &&
               !have_common_factor(fcts[a], fcts[c]) &&
               !have_common_factor(fcts[b], fcts[c]))
            {
                if(prod(fcts[a])*prod(fcts[b])*prod(fcts[c]) < c)
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
