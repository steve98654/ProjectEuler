#include <iostream>

int cntfct(int a, int b, int c, int n)
{
    return 4*(n-1)*(a+b+c+n-2)+2*(a*b+a*c+b*c);
}

int main()
{

    int mxval = 100000; 
    int cntvec[mxval+1]; 


    int a = 1; int b = 1; int c = 1; int n = 1;
    int amx = 1000; int bmx= 2000;

    for(a = 1; a < amx; a++)
    {   
        for(b = a; b < bmx; b++)
        {   
            for(c = b; cntfct(a,b,c,1) < mxval; c++)
            {
                for(n = 1; cntfct(a,b,c,n) < mxval; n++)
                {
                    cntvec[cntfct(a,b,c,n)] += 1;
                }
            }
        }
    }

    // Find max and find 1000

    for(int i = 0; i < mxval; i++)
    {
        if(cntvec[i] == 1000)
        {

            std::cout << "Thousand Ind: " << i << std::endl;
        }
    }

    return 0;
}

