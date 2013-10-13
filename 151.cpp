#include<iostream>
#include<boost/random/mersenne_twister.hpp>
#include<boost/random/discrete_distribution.hpp>
#include<iomanip>
#include<ctime>

boost::mt19937 gen;

inline void ItFun(double (&st)[5])
{
    double summ = st[0]+st[1]+st[2]+st[3];
    double probs[]={st[0]/summ,st[1]/summ,st[2]/summ,st[3]/summ};
    boost::random::discrete_distribution<> dist(probs);
    int tp = dist(gen);

    if(summ==1)
        st[4]++;
    if(tp==0)
    {
        st[0]--;st[1]++;st[2]++;st[3]++;
    }
    if(tp==1)
    {
        st[1]--;st[2]++;st[3]++;
    }
    if(tp==2)
    {
        st[2]--;st[3]++;
    }
    if(tp==3)
    {
        st[3]--;
    }
}

int main(){

    int cnt = 0;
    int runs = 1000000000;
    clock_t t;

    t = clock();
    for(int i = 0; i < runs; ++i)
    {
        if(i%1000000 == 0)
            std::cout << i/1000000 << std::endl;

        double st[5] = {1,1,1,1,0};

        ItFun(st);ItFun(st);ItFun(st);ItFun(st);ItFun(st);
        ItFun(st);ItFun(st);ItFun(st);ItFun(st);ItFun(st);
        ItFun(st);ItFun(st);ItFun(st);ItFun(st);
    
        cnt += st[4];
    }

    t = clock() - t;

    std::cout << "Time was: " << ((float)t)/CLOCKS_PER_SEC << std::endl;
    std::cout << std::setprecision(8) << (double)cnt/runs << std::endl;
    return 0;
}

