#include <stdio.h>
void prime(int n);
int main(){
	int num;
	scanf("%d", &num);
	if(num!=1)
	    prime(num);
	return 0;
}
void prime(int n){
    char p[n+1];
    int i,j;
    memset(p,1,n+1);
    for(i=2;i<=n;i++){   
        for(j=i+i;j<=n;j=j+i)
            p[j]=0;
        if(p[i])
        	printf("%d ",i);
    }
}
