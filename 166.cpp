//Project Euler Problem 166
#include<iostream>

int main(){

    int cnt=0; 

    for(int a1=0; a1<=9; ++a1)
    {
        for(int a2=0; a2<=9; ++a2)
        {
            for(int a3=0; a3<=9; ++a3)
            {
                for(int a5=0; a5<=9; ++a5)
                {
                    for(int a6=0; a6<=9; ++a6)
                    {
                        for(int a7=0; a7<=9; ++a7)
                        {
                            for(int a9=0; a9<=9; ++a9)
                            {
                                for(int c=0; c<=36; ++c)
                                {
                                    if(0 <= c-a1-a2-a3 && c-a1-a2-a3 <=9
                                       && 0 <= -a5-a6-a7+c && -a5-a6-a7+c <=9 
                                       && 0 <= 2*a1+a2+a3+a5-a7+a9-c 
                                       && 2*a1+a2+a3+a5-a7+a9-c <= 9
                                       && 0 <= -2*a1-a2-a3-a5-a6-a9+2*c 
                                       && -2*a1-a2-a3-a5-a6-a9+2*c <= 9
                                       && 0 <= a6+a7-a9 && a6+a7-a9<=9
                                       && 0 <= -a1-a5-a9+c && -a1-a5-a9+c<=9
                                       && 0 <= -2*a1-2*a2-a3-a5-a6+a7-a9+2*c
                                       && -2*a1-2*a2-a3-a5-a6+a7-a9+2*c <= 9
                                       && 0 <= 2*a1+a2+a5+a6-a7+a9-c 
                                       && 2*a1+a2+a5+a6-a7+a9-c <=9
                                       && 0 <= a1+a2+a3+a5+a9-c
                                       && a1+a2+a3+a5+a9-c <= 9
                                      )
                                    {
                                        cnt++;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    std::cout << cnt << std::endl;
    return 0;

}
