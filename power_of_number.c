#include "stdio.h"

int Power(int a,int b){
	int result=1;
	while(b>0){
		if(b%2==1)
			result=result*a;
		a=a*a;
		b=b/2;
	}
	return result;
}

int binaryExponentiation(int x,int n)
{
    if(n==0)
        return 1;
    else if(n%2 == 0)        //n is even
        return binaryExponentiation(x*x,n/2);
    else                             //n is odd
        return x*binaryExponentiation(x*x,(n-1)/2);
}

int main(){
	printf("%d\n",Power(2,3));
	return 0;
}