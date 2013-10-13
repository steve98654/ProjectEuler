#include<iostream>
#include<vector>

int main(){

    long cnt = 0;
    std::vector<long> vec;
    
    for(int i = 1; i != 12; ++i)
    {
        vec.push_back(0);
    }

    //    long long vec[12]={0,0,0,0,0,0,0,0,0,0,0,0};

    for(int i1 = 1; i1 <=9; ++i1)
    {
        vec[0]++;
        for(int i2 = 0; i2 <=9-i1; ++i2)
        {  
            vec[1]++;
            for(int i3 = 0; i3 <=9-i2-i1; ++i3)
            {
                vec[2]++;
                for(int i4 = 0; i4 <=9-i3-i2; ++i4)
                {
                    vec[3]++;
                    for(int i5 = 0; i5 <=9-i4-i3; ++i5)
                    {
                        vec[4]++;
                        for(int i6 = 0; i6 <=9-i5-i4; ++i6)
                        {
                            vec[5]++;
                            for(int i7 = 0; i7 <=9-i6-i5; ++i7)
                            {
                                vec[6]++;
                                for(int i8 = 0; i8 <=9-i7-i6; ++i8)
                                {
                                    vec[7]++;
                                    for(int i9 = 0; i9 <=9-i8-i7; ++i9)
                                    {    
                                        vec[8]++;
                                        for(int i10 = 0; i10 <=9-i9-i8; ++i10)
                                        {
                                            vec[9]++;
                                            for(int i11 = 0; i11 <=9-i10-i9; ++i11)
                                            {
                                                vec[10]++;
                                                for(int i12 = 0; i12 <=9-i11-i10; ++i12)
                                                {
                                                    vec[11]++;
                                                }
                                            }
                                        }
                                    }
                                }   
                            }
                        }
                    }
                }
            }
        }
    }
    
    for(int i = 0; i < 12; ++i)
    {
        std::cout << i << " " << vec[i] << std::endl;
    }
    return 0;
}

