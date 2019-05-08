#include<stdio.h>

int main()
{
    int n,t,a[1000],l,r,sum,i;
    scanf("%d %d",&n,&t);

    for(i=1;i<=n;i++)
        scanf("%d",&a[i]);

    while(t--){
        sum=0;
        scanf("%d %d",&l,&r);
        printf("\n%d %d",l,r);
        for(i=l;i<=r;i++)
            sum=sum+a[l];
        printf("\n Sum calculated: %d",sum);
        i=r-l;
        printf("\nDeninator: %d",i);
		sum/=i;
        printf("%d\n",sum);
    }
    return 0;
}
