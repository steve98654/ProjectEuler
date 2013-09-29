#include<iostream>
#include<vector>

using namespace std;


/////// Find a way to call Python's pow function in this program

long long modExp(long long b, long long e, long long m)
{
    long long remainder;
    long long x = 1;

    while (e != 0)
    {
        remainder = e % 2;
        e = e/2;

        if (remainder == 1)
            x = (x * b) % m;
            b = (b * b) % m; // New base equal b^2 % m
    }

    return x;
}

long long PowMod(long long b, long long e, long long m)
{
    long long c = 1;
    for(long long e_prime = 1; e_prime <= e; ++e_prime)
        c = (c * b) % m;

    return c;
}

long long PowMod2(long long b, long long e, long long m)
{
    long long tpe = e;
    long long res = 1;
    while (e > 0)
    {
        if (e%2 == 1)
        {
            res = (res*b)%m;
        }

        //        if(tpe == 34535)
        //  cout << res << "  " << e << "  " << b << endl;

        e = e >> 1;
        //        b = (b*b)%m;
        b = PowMod(b,e,m);

        //    cout << b << endl;
    }

    return res;
}

/* This function calculates (a^b)%c */
long long pwmodulo(long long a,long long b, long long c){
    long long x=1,y=a; // long long is taken to avoid overflow of intermediate results
    while(b > 0){
        if(b%2 == 1){
            x=(x*y)%c;
        }
        y = PowMod(y,2,c); // squaring the base
        b /= 2;
    }
    return x%c;
}


int main(){

    // cycle length of x^a mod 15! for x = 0,1,2,...,100
    const int poword[] = {1, 1, 170100, 268800, 85050, 4354560, 2100, 311040, 56700, 134400,
                    1134, 21772800, 2100, 21772800, 12150, 13440, 42525, 1814400, 60, 
                    1036800, 34020, 12800, 170100, 10886400, 420, 2177280, 1890, 89600, 
                    2700, 21772800, 30, 388800, 34020, 33600, 170100, 207360, 1050, 
                    7257600, 170100, 134400, 17010, 10886400, 300, 4354560, 56700, 10752, 
                    56700, 5443200, 300, 155520, 4860, 53760, 170100, 2419200, 2100, 
                    48384, 12150, 8960, 170100, 21772800, 420, 21772800, 56700, 2400,
                    28350, 54432, 1050, 3110400, 4860, 268800, 4860, 3628800, 2100,
                    3628800, 17010, 53760, 34020, 3110400, 700, 777600, 180, 67200, 1260, 
                    21772800, 300, 4354560, 170100, 134400, 170100, 3628800, 70, 1036800,
                    170100, 53760, 85050, 544320, 2100, 388800, 8100, 2560, 567};

    int f15o = 217728000; //fib mod 15 order

    // for tst only 
    //f15o = 100;

    // Create and store fib-nums mod 15 up to when they repeat
    vector<long> fvec; 
    long long fct=1;

    for(long i = 2; i<=15; i++)
    {
        fct*=i;
    }

    fvec.push_back(0); //start at zero
    fvec.push_back(1);

    for(long i=2; i!=f15o; i++)
    {
        fvec.push_back((fvec[i-1] + fvec[i-2])%fct);
    }

    //    long long x = 2; // actual x value in problem

    //vector<long> pmdtmp;

    //for(long long k = 0; k!=poword[x]; ++k)
    //{
    //    long long tmp = modExp(x,k,fct);
    //    pmdtmp.push_back(tmp);

    //    if(k==35334)
    //        cout << tmp << endl;
    //}

    //Debug Output
    cout << fvec[f15o-1] << " " << fvec[f15o - 2] << "  " <<  fvec[f15o-3] << endl;
    //cout << fct << endl;

    //cout << pmdtmp[123] << "  " << pmdtmp[124] << "  " << pmdtmp[125] << endl;

    //    cout << modExp(2,34535,fct) << endl;
    //cout << PowMod(2,34535,fct) << endl;
    //cout << PowMod2(2,34535,fct) << endl;
    //cout << pwmodulo(2,34535,fct) << endl;
    
    cout << fvec[3452] << "  " << fvec[89573] << "  " << fvec[77934793] << endl; 
    return 0;

}
