#include <iostream>

using namespace std;

int main(){        
    
    int a;
    int cont;
    int tot=0;
    
    for(int n=1;n<50000000;n++)
    {
        cont=0;
        
        for(a=2;a*a<n;a++)
        {            
            if(n%a==0 && (a+(n/a))%4==0)
            {
                if(3*a<=n/a) cont++;//y<=r
                else cont+=2;
            }
        }
        if(a*a==n && a%2==0) cont++;
        if(n%4==3) cont++;
        if(cont==1) tot++;

        if(n%1000000==0)
            cout << n/1e6 << "  " << cont << endl;

    }

    cout<<tot<<endl;

    //    system("pause");
    return 0;
}
