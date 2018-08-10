#include <stdio.h>
struct Node
{
	long data;
	struct Node *next;
};
int main()
{
	int t, n;
	int flag,i; 
	long num;
	struct Node *home=NULL,*temp,*temp1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		while(n--)
		{
			scanf("%ld",&num);
			if(home==0)
			{
				home=(struct Node*)malloc(sizeof(struct Node));
				home->data=num;
				home->next=0;
			}
			else
			{
				temp1=home;
				if(num==home->data){
					home=home->next;
					free(temp1);	
				}
				else if(temp->next==0)
				{
					temp=(struct Node*)malloc(sizeof(struct Node));
					temp->data=num;
					temp->next=0;
					home->next=temp;
				}
				else{
					temp=home->next;
					flag=0;
					while(temp){
						if(temp->data==num){
							temp1->next=temp->next;
							free(temp);
							flag=1;
							break;
						}
						temp1=temp;
						temp=temp->next;
					}
					if(!flag){
						temp=(struct Node*)malloc(sizeof(struct Node));
						temp->data=num;
						temp->next=0;
						temp1->next=temp;
					}
				}
			}
		}
		if(home)
			printf("%u\n",home->data);
		else
			printf("-1\n");
		free(home);
		home=0;
	}
	return 0;
}	
