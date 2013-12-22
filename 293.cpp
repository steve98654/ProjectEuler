// generate primes less than 10^9 + 10^5 make it global

// write a function that finds the next prime after n

// find distinct prime factors
// write a function to test if they are consequtive
// take distinct prime factors, sort, take first and last,
// test if it is first and last in primes vector

// comput pF numbers 
// sum


#include <vector>
#include <iostream>
#include <ctime>
#include <cmath>

int main()
{
    // Generate primes up to pmax
    std::vector<int> primes;
    primes.push_back(2);
    long pmax = 1e6+1e5;

    for(int i=3; i < pmax; i++)
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
            //    cout << i << " ";
        }
    }

    std::cout << primes.back() << std::endl;

    return 0;
}

