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
    for(int i=3; i < 1000000; i++)
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

    // Display primes 
    //    for(int j=0; j!=primes.size(); ++j)
    //    std::cout << primes[j] << std::endl;

    // Display just the first and last primes
    //    std::cout << primes[0] << std::endl;
    //std::cout << primes.back() << std::endl;
    
    // Generate multiples in increasing order, take last digits 

    std::string val = boost::lexical_cast<std::string>(100);
    int dgts = val.size(); //find number of  digits 

    // std::cout << val.size() << std::endl;
    // get last d digits by modding by 10^dgts

    //    std::cout << primes[2] << std::endl;
    
    std::vector<long> mult; 

    for(int k = 2; k <= 10; k++)
    {
        int p1 = primes[k];
        int p2 = primes[k+1];

        std::string p1str = boost::lexical_cast<std::string>(p1);
        std::string p2str = boost::lexical_cast<std::string>(p2);

        int p1dgts = p1str.size();
        int p2dgts = p2str.size();

        int m = 2; //Multiplier
        int multst = m*p2;
        
        while(multst%int(pow(10,p1dgts))!=p1)
        {
            m++;
            multst = m*p2; 
        }

        mult.push_back(multst);

    }

    for(int k = 0; k < mult.size(); k++)
    {
        std::cout << mult[k] << std::endl;
    }

    return 0;
}
