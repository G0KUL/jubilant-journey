#include <stdio.h>
#include <string.h>
int main(){
	int num,i,l1,l2,flag;
	char str1[10000],str2[10000];
	int a[26],b[26];
	scanf("%d",&num);
	while(num--){
		flag=0;
	    for(i=0;i<26;i++)
	        a[i]=b[i]=0;
		scanf("%s%s",str1,str2);
	    l1=strlen(str1);
		l2=strlen(str2);
		for(i=0;i<l1;i++)
			a[str1[i]-97]++;
		for(i=0;i<l2;i++)
			b[str2[i]-97]++;
		
		for(i=0;i<26;i++)
			if(a[i]!=b[i]){
				flag=1;
				break;
			}
		
		if(flag)
			printf("NO\n");
		else
			printf("YES|n");
	}
}
