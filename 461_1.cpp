#include <iostream>
#include <cmath>
#include <iomanip>
#include <vector>
#include <algorithm>

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
    int mxind = 1400;  // Eventually make this 14000


    vector<double> vals;
    vector<double> sums;

    for(int k = 0; k < mxind; k++)
    {
        vals.push_back(f(k,n));
    }

    for(int k = 0; k < mxind; k++)
    {
        for(int j = 0; j < mxind; j++)
        {
            sums.push_back(vals[k] + vals[j]); 
            sums.push_back(vals[k] + vals[j]-pi); 
        }
    }

    sort(sums.begin(),sums.end());
   

    // NEED BETTER ALGORITHMS HERE 
    // GIVEN AN ARRAY FIND THE TWO ENTRIES WITH SMALLEST SUM
    // begin main algo here 


    int i = 0; 
    int j = mxind - 1;
    int k = j;
    int istr, jstr;

    double tmpval,tmpvalpre;
    double minvl = 10;

    while(j - i > 3)
    {
        k = j;
        tmpvalpre = 0;
        tmpval = abs(sums[j] - sums[i]);

        while(tmpval > tmpvalpre)
        {
            tmpvalpre = tmpval;
            k--;
            tmpval = abs(sums[k] - sums[i]);
        }

        if(tmpval < minvl)
        {
            minvl = tmpval;
            istr = i; jstr = k;
        }

        j=k;

    }

    cout << vals[0] << " " << vals[13531] << endl;
    cout << sums[0] << " " << sums.back() << endl;
    cout << istr << " " << jstr << " " << minvl << endl; 

    //    cout << "a: " << amx << " b: " << bmx << " c: " << cmx << " d: " << dmx << endl;
    //cout << scientific << setprecision(15) << minval << endl;

    return 0;
}
