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

    std::cout << F(3,50) << std::endl;

}
