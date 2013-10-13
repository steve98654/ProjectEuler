#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

// Values below 100000 are 9, 10404, 16900, 97344
// sq roots are 3, 102, 130, 312 

int main(){

    int nmin = 1;
    int nmx = 100000;
    int q,r,n,d;
    float sq;
    std::vector<int> tpvec;
    std::vector<int> vls;
    std::vector<int> sqvls;
    
    for(n=nmin; n<nmx; n++)
    {
        
        if(n%10000==0)
            std::cout<<n<<std::endl;

        for(d = 1; d<n; d++)
        {

            tpvec.clear();
            q = n/d; r = n%d;
            tpvec.push_back(r); tpvec.push_back(d); tpvec.push_back(q);
            std::sort(tpvec.begin(),tpvec.end());

            if(tpvec[0]!=0 && float(tpvec[2])/tpvec[1] == float(tpvec[1])/tpvec[0])
            {
                vls.push_back(n);
            }
        }
    }

    for(int i = 0; i<vls.size(); i++)
    {
        sq = std::sqrt(vls[i]);
        if(std::abs(sq - int(sq))<1e-8)
            sqvls.push_back(vls[i]);
    }


    // for(int j = 0; j<tpvec.size(); ++j)
    //    std::cout << tpvec[j] << std::endl;


    for(int k = 0; k< sqvls.size(); ++k)
    {
        std::cout << sqvls[k] << std::endl;
    }

    return 0;
}
