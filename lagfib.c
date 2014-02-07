#include <stdio.h>

int main(void)
{
    printf("DB1");


    static int rnum[6000001];

    long long k;
    rnum[0] = 0;

    for(k = 1; k <= 55; ++k)
    {
        rnum[k] = (100003-200003*k+300007*k*k*k)%1000000;
    }

    printf("DB2");

    for(k = 56; k <= 6000001; ++k)
    {
        rnum[k] = (rnum[k-24] + rnum[k-55])%1000000;
    }

    printf("DB3");
    
    FILE *fp;
    fp = fopen("rannum.txt","w+");

    for(k = 1; k < 6000001; ++k)
    {
        fprintf(fp,"%d,",rnum[k]);
    }
    
    
    printf("DB4");

    fprintf(fp,"%d",rnum[6000000]);

    fclose(fp);
    
    return 0;
}
