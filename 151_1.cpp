#include<iostream>
#include<boost/random/mersenne_twister.hpp>
#include<boost/random/discrete_distribution.hpp>
#include<iomanip>

double summe(double a, double b)
{
    return a + b;
}

double nest(double (*fun)(double,double), double a, int n)
{
    if(n!=1)
        return nest(fun,fun(a,a),n-1);
    else
        return fun(a,a);
}

void nest1( void (*fun)(double[5]), double(&st)[5],int n)
{
   if(n!=1)
       nest1(fun,st,n-1);
   else
       fun(st);
}

boost::mt19937 gen;
//boost::random::discrete_distribution<> dist(probs);

void ItFun(double (&st)[5])
{
    double summ = st[0]+st[1]+st[2]+st[3];
    double probs[]={st[0]/summ,st[1]/summ,st[2]/summ,st[3]/summ};
    //    boost::mt19937 gen;
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

    //double probs[] = {0.5,0.1,0.1,0.1};

    //boost::mt19937 gen;
    //boost::random::discrete_distribution<> dist(probs);

    //for(int i = 1; i != 10; ++i)
    //{
    //    std::cout << dist(gen) << std::endl;
    //}

    double sum = 0;
    double a = 1.2;
    int cnt = 0;
    int runs = 1000000;

    //    double (*fp)(double,double);
    //fp = summe;

    //std::cout << nest(summe,2.1,2) << std::endl;
    //

    for(int i = 0; i < runs; ++i)
    {
        double st[5] = {1,1,1,1,0};

        ItFun(st);ItFun(st);ItFun(st);ItFun(st);ItFun(st);
        ItFun(st);ItFun(st);ItFun(st);ItFun(st);ItFun(st);
        ItFun(st);ItFun(st);ItFun(st);ItFun(st);
    
        cnt += st[4];
        //   std::cout << st[0] << st[1] << st[2] << st[3] << st[4] << std::endl;  
    }

    std::cout << std::setprecision(8) << (double)cnt/runs << std::endl;
    return 0;

}
