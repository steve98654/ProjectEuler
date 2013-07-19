" Project Euler Problem 86 solution "

#include <math.h>
#include <iostream>
#include <time.h>

double cnsols(int l, int w, int h)
{
    using std::min;

    return fmin(fmin(sqrt(l*l + (h+w)*(h+w)), sqrt(h*h + (l+w)*(l+w))), sqrt((h+l)*(h+l)+w*w));

}

int rtcnt(int mxend)
{
    int cnt = 0;
    double tol = 1e-8;
    double vl = 0;

    for(int l=1; l<=mxend; l++)
    {
        for(int w=l; w<=mxend; w++)
        {
            for(int h=w; h<=mxend; h++)
            {
                vl = cnsols(l,w,h);
                if(fabs(vl-round(vl))<tol)
                { 
                    cnt++;
                }
            }
        }
    }

    return cnt;
}

int main()
{
    double tol = 1e-8;
    int mxstr = 1800;
    int mxend = 1850;
     
    clock_t start = clock();

    for(int i=mxstr; i<=mxend; i++)
    {
        std::cout << "For m = " << i << " we have " << rtcnt(i) << " cuboids." << std::endl;
    }

    clock_t end = clock();
    float diff ((float)end - (float)start);

    std::cout << "Total time is: " << diff/CLOCKS_PER_SEC << std::endl;
    
    return 0;
}

