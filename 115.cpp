#include<iostream>

long long F(int m, int n)
{

    long long sols = 1;

    if(m>n)
    {
        return sols;
    }

    for(int spos = 0; spos <= n-m; spos++)
    {
        for(int blen = m; blen <= n - spos; blen++)
        {
            sols += F(m, n - spos - blen - 1);
        }

    }

    return sols;
}

int main(){

    long long tout = 0;
    int i = 52;

    while(tout < 1e6) 
    {
        tout = F(50,i);
        std::cout << i << "  " << tout << std::endl;
        i++;
    }
}
