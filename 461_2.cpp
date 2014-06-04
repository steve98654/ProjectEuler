#include <iostream>
#include <cmath>
#include <iomanip>
#include <vector>
#include <algorithm>

//Outline of algorithm

// (1) Compute and sort a vector of pairwise sums taking values up to maxind
// (2) Put a left and right index at endpoints of this sum, and compute 
//     left plus right minus pi
// (3) Move the right pointer down until the absolute error is greater than the
//     error from the previous step and compare previous error to min val
// (4) Increment the left pointer  
// (5) Set the right pointer to min(last right pointer + 2, maxind*mxind) 
// (6) Look over left index 
// (7) return the min error and two pointer values
// (8) Back out original function inds and print result

using namespace std;

double f(double k, double n)
{
    return exp(double(k)/double(n)) - 1;
}

int main (void)
{
    // Constants 
    double pi = 3.1415926535897932;
    int n = 10000;                         // values of the function 
    int maxind = 14000;                     // largest value of k to choose for problem
        
    vector<double> vals;                  // first n values of the function
    vector<double> sums;                  // vector of pairwise sums of the function

    // Compute vals
    for(int k = 0; k < maxind; k++)
    {
        vals.push_back(f(k,n));
    }

    // Compute pairwise sums
    for(int k = 0; k < vals.size(); k++)
    {
        for(int j = 0; j < vals.size(); j++)
        {
            sums.push_back(vals[k] + vals[j]); 
        }
    }

    vector<double> unsortedsums = sums;

    // Sort the vector
    sort(sums.begin(),sums.end());
   
    // Begin main search algorithm 

    double err = 10;
    double errlast = 10.1;
    double minerr = 10;
    int lep = 0; int rep = maxind*maxind-1;
    int minlep,minrep;

    while(lep < maxind*maxind-1)
    {
        while(err <= errlast && lep < rep)
        {
            rep--;
            errlast = err;
            err = abs(sums[lep] + sums[rep] - pi);
        }

        if(errlast < minerr)
        {
            minlep = lep; 
            minrep = rep + 1;
            minerr = errlast;
            cout << setprecision(15) << "LEP: " << minlep << " REP: " << minrep << "Err: " << minerr << endl;
        }

        lep++; 
        err = 10; 
        errlast = 10.1;
        rep = min(rep + 2, maxind*maxind-1);
    }

    vector<double>::iterator leftind1, leftind2;
    vector<double>::iterator rightind1, rightind2;
    leftind1 = find(unsortedsums.begin(), unsortedsums.end(), sums[minlep]);
    advance(leftind1,1);
    leftind2 = find(leftind1, unsortedsums.end(), sums[minlep]);
    rightind1 = find(unsortedsums.begin(), unsortedsums.end(), sums[minrep]);
    advance(rightind1,1);
    rightind2 = find(rightind1, unsortedsums.end(), sums[minrep]);

    int d1,d2,d3,d4;

    d1 = distance(unsortedsums.begin(), leftind1);
    d2 = distance(unsortedsums.begin(), leftind2);
    d3 = distance(unsortedsums.begin(), rightind1);
    d4 = distance(unsortedsums.begin(), rightind2);
    
    cout << "Left Index 1 " << d1 << endl;
    cout << "Left Index 2 " << d2 << endl;
    cout << "Right Index 1 " << d3 << endl;
    cout << "Right Index 2 " << d4 << endl;

    int a,b,c,d;
    a = d1%maxind - 1;
    b = d2%maxind; 
    c = d3%maxind - 1;
    d = d4%maxind;
    
    cout << setprecision(15) << "Final LEP: " << minlep << "Final REP: " << minrep 
         << "Final Err: " << minerr << endl;
    
    cout << a << " " << b << " " << c << " " << d << endl;

    cout << "Solution: " << a*a + b*b + c*c + d*d << endl;

    return 0;
}

