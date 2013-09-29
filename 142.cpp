#include<cmath>
#include<iostream>
#include<vector>
#include<algorithm>
#include<iomanip>

using namespace std;

bool sqchk(int tmp)
{
    double eps = 1e-8;
    double sqtmp = sqrt(double(tmp));
    return abs(sqtmp-round(sqtmp))<eps;
}

int main(){

    int mxsq = 2000;
    vector<double> sq;
    vector<double> lst;

    //    for(int i=1; i<=100; i++)
    //    if(sqchk(i))
    //        cout << i << endl;

    double a,b,c,d,e,f,x,y,z,tmpsum;

    for(int i1 = 1; i1 <= mxsq; ++i1)
    {    
        if(i1%100 == 0)
            cout << i1 << endl;

        for(int i2 = 1; i2 <= mxsq; ++i2)
        {
            for(int i3 = 1; i3 <= mxsq; ++i3)
            {
                a = i1*i1; b = i2*i2; c = i3*i3;
                d = a + b - c; e = c - b; f = a - c;

                if(d > 0 && e > 0 && f > 0 && sqchk(d) && sqchk(e) && sqchk(f))
                {
                    x = (a+b)/2; y = (e+f)/2; z=(c-d)/2;
                    tmpsum = x + y + z;
                    if(x>y && y>z && z > 0)
                    {
                        lst.push_back(x+y+z);
                    }
                }
            }
        }
    }

    sort(lst.begin(),lst.end());

    cout << "List size is: " << lst.size() << endl;
    cout << "Smallest sum is: " << setprecision(8) << lst[0] << " " << lst[1] << endl;

    return 0;
}

