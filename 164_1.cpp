#include<iostream>
#include<vector>

using namespace std;
using std::vector;

class Prob164{
public:

static const int dgts = 4;
//long long* count = new int[10][10][dgts]={{{0}}};

vector<vector<vector<long long> > > count;

for(int i=0;i<10;i++)
{
    for(int j=0;j<10;j++)
    {
        for(int k = 0; k<dgts; k++)
        {
            count[i][j][k] = 0;
        }
    }
}

long long ForIt(int i1, int i2, int depth)
{
    if(depth == 0)
    {
        return 1;
    }
    else
    {
        if(count[i1][i2][depth]==0)
        {long long res = 0;
            for(int i=0; i<=9-i2-i1;++i)
            {
                count[i1][i2][depth] += ForIt(i2,i,depth-1);
            }
        
        }
        return count[i1][i2][depth];
    }

}

int main(){

    long long cnt = 0;
    
    for(int i1=1; i1<=9; ++i1)
    {
        for(int i2=0;i2<=9-i1;++i2)
        {
            cnt+=ForIt(i1,i2,4);
        }
    }
    
    cout << cnt << endl;
    return 0;
    
}
}
