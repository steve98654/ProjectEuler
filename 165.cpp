// NEED TO FIND DISTINCT POINTS! LETS REDO IN PYTHON AND TAKE SETS

#include <iostream>
#include <cmath>
// Check our main function, make sure that we are doing write thing here.


// These args are really ints, but treat them as doubles so that we 
// do not have to worry about them later.  See 165.nb
double parm(double x0, double y0, double x1, double y1, 
            double x2, double y2, double x3, double y3)
{
    double denom = (x3-x2)*(y0-y1) + (x0-x1)*(y2-y3);
    if(std::abs(denom) <1e-6)
    {
        // Case that lines are parallel
        return 0;
    }
    else
    {
        double s = (x2*(y1-y0)+x1*(y0-y2)+x0*(y2-y1))/denom;
        if(s > 0 && s < 1)
        {
            double t;
            if(x0 != x1)
            {
                t = (x0-x2+s*(x2-x3))/(x0-x1);
            }
            else
            {
                t = (y0-y2+s*(y2-y3))/(y0-y1);
            }

            if(t > 0 && t < 1)
            {
                return 1;
            }
            else
            {
                return 0;
            }
        }
        else
        {
            return 0;
        }
    }
}

int main()
{

    // Generate the random numbers 
    int tnum = 20000;
    long long  s[tnum+1];
    long long t[tnum+1];
    s[0] = 290797; 

    for(int i = 0; i <= tnum; ++i)
    {
        s[i+1] = (s[i]*s[i])%50515093;
        t[i]   = s[i]%500;
    }


    // Begin the brute force checking of the lines 
    int numlines = 5000;
    long long intcnt = 0;
    for(int i = 0; i < numlines; ++i)
    {
        for(int j = i+1; j < numlines; ++j)
        {
            intcnt += parm(t[4*i+1], t[4*i+2], t[4*i+3], t[4*i+4],       
                           t[4*j+1], t[4*j+2], t[4*j+3], t[4*j+4]);
        }
    }

    // Sample output of ran nums (shows agreement with prob hint)
    for(int i = 0; i < 20; ++i)
    {
        std::cout << s[i] << "  " << t[i] << std::endl;
    }

    // Output result 

    std::cout << "Number of true intersection pairs: " << intcnt << std::endl;

    std::cout << t[0] << "  " << t[19999] << "  " << t[20000] << std::endl;

    return 0;
}
