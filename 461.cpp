#include <iostream>
#include <cmath>
#include <iomanip>

// Compute array of all pairwise sums 
// sort array
// lower pointer and upper pointer for this array 

using namespace std;

double f(double k, double n)
{
    return exp(double(k)/double(n)) - 1;
}

int main (void)
{

    // 798, 1808, 4717, 11810
    
    // Try a course grid and then refine to a smaller one 

    int sft = 60;
    int albd = 400;
    int aubd = 600;
    int blbd = 800;
    int bubd = 1000;
    int clbd = 3450;
    int cubd = 3650;
    int dlbd = 12600;
    int dubd = 12800;
    int spc = 1;

    double pi = 3.1415926535897932;
    long n = 10000;

    double tmp = 200;
    double minval=200;
    int amx,bmx,cmx,dmx;

    for(int a = albd; a <= aubd; a+=spc)
    {
        for(int b = blbd; b <= bubd; b+=spc)
        {
            for(int c = clbd; c <= cubd; c+=spc)
            {
                for(int d = dlbd; d <= dubd; d+=spc)
                {
                    tmp = abs(f(a,n) + f(b,n) + f(c,n) + f(d,n) - pi);
                    if(tmp < minval)
                    {
                        minval = tmp;
                        amx=a; bmx=b; cmx=c; dmx=d;
                    }
                }
            }
        }
    }
    
    cout << "a: " << amx << " b: " << bmx << " c: " << cmx << " d: " << dmx << endl;
    cout << scientific << setprecision(15) << minval << endl;

    return 0;
}
