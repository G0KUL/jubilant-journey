#include "stdio.h"

int gcd(int a, int b){
	if(b==0)
		return a;
	else
		return gcd(b,a%b);
}
int main(){
	printf("GCD: %d\n",gcd(16,10));
	return 0;
}