//Project Euler Problem 134
#include <iostream>
#include <vector>
#include <boost/lexical_cast.hpp>
#include <string>
#include <cmath>

int main()
{
    // Generate primes less than 1000000
    std::vector<int> primes;
    primes.push_back(2);
    for(int i=3; i < 1000004; i++)
    {
        bool prime=true;
        for(int j=0;j<primes.size() && primes[j]*primes[j] <= i;j++)
        {
            if(i % primes[j] == 0)
            {
                prime=false;
                break;
            }
        }
        if(prime) 
        {
            primes.push_back(i);
        }
    }

    std::vector<unsigned long long> mult; 

    for(int k = 2; k<primes.size()-1; k++)
    {
        if(k%1000 == 0)
            std::cout << k << std::endl;
        
        int p1 = primes[k];
        int p2 = primes[k+1];

        std::string p1str = boost::lexical_cast<std::string>(p1);
        int p1dgts = p1str.size();

        unsigned long long multst = 2*p2;
        
        int pdgt = int(pow(10,p1dgts));

        while(multst%pdgt!=p1)
        {
            multst += p2; 
        }

        mult.push_back(multst);

    }

    long sum = 0;
    for(int k = 0; k < mult.size(); k++)
    {
        sum += mult[k];
    }

    std::cout << "Sum is: " << sum << std::endl;
    return 0;
}

