#include <iostream>
#include <cmath>
#include <iomanip>

// Compute array of all pairwise sums 
// sort array
// lower pointer and upper pointer for this array 

using namespace std;

long maxPD(long n)
{
    long MPD = -1;
    long size;
    long i;

    if(n == 1){ 
        return 1;
    }

    while(n%2 == 0){
        MPD = 2;
        n = n/2;
    }

    size = long(sqrt(n)) + 1;
    for(i=3;i < size; i+=2){
        while(n% i == 0){
            MPD = i;
            n = n/i;
        }
    }

    MPD = max(n,MPD);

    return MPD;
}

int main (void)
{
    long cnt = 1;
    long mxvl = 10000000000;
    for(long i=1; i <= mxvl; i++){
        if(maxPD(i) < sqrt(i)){
            cnt++;
            //cout << i << endl;
        }
        if(i%10000000==0){
            cout << double(i)/10000000 << endl;
            cout << cnt << endl;
        }
    }

    cout << "Fin Count" << endl;
    cout << cnt << endl;

    return 0;
}
