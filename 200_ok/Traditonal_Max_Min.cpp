#include <stdio.h>

int main()
{
	int a[10]={28,-5,13,12,0,40,-3,62,12,1};
	int max,min;
	max=min=a[0];
	for (int i=1;i<10;i++)
		if(a[i]>max)
			max=a[i];
		else if(a[i]<min)
			min=a[i];
	printf("\n Max: %d, Min: %d\n",max,min);
	return 0;
}
