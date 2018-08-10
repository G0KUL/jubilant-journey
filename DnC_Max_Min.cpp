#include<stdio.h>
#include<stdlib.h>
struct Values MinMax(int[],int, int);

struct Values
{
	int max, min;
};

int main(){
	int a[15]={28,-5,13,12,0,40,-3,62,12,100,-11,-12,-13,-100,101};
	struct Values v=MinMax(a,0,14);	
	printf("\n Max: %d, Min: %d \n",v.max,v.min);
	return 0;
}

struct Values MinMax(int a[],int i, int j){
	int mid;
	struct Values u;
	u.max=a[i];
	u.min=a[i];

	if(i==j){
		u.max=a[i];
		u.min=a[i];
	}
	else if(i+1==j){
		if(a[j]>u.max)
			u.max=a[j];
		else if(a[j]<u.min)
			u.min=a[j];
	}
	else{
		mid=(i+j)/2;
		struct Values v;
		u=MinMax(a,i,mid);
		v=MinMax(a,mid+1,j);
		if(u.max<v.max)
			u.max=v.max;
		if(u.min>v.min)
			u.min=v.min;
	}
	return u;
}
