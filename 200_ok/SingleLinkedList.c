#include "stdio.h"
#include "stdlib.h"
void insert_node();
void delete_Start();
void disp();
struct Node
{
	int data;
	struct Node *next;
};
struct Node *home=0;
int main()
{
	int ch;
	while(1){
		printf("\n 1.Insert at End\n 2.Delete from Start\n 3.Disp\n 4.Exit\n Enter ur choice :");
		scanf("%d",&ch);
		switch(ch)
		{
			case 1:
			insert_node();
			break;
			case 2:
			delete_Start();
			break;
			case 3:
			disp();
			break;
			case 4:
			exit(0);
		}
		
	}
}

void insert_node()
{
	int data;
	printf(" Enter a data :");
	scanf("%d",&data);
	if(home==0){
		home=(struct Node*)malloc(sizeof(struct Node));
		home->data=data;
		home->next=NULL;
	}
	else{
		struct Node *temp=home;
		while(temp->next!=NULL)
			temp=temp->next;
		temp->next=(struct Node*) malloc(sizeof(struct Node));
		temp=temp->next;
		temp->data=data;
		temp->next = 0;
	}
}

void delete_Start(){
	if(home!=0){
		struct Node *temp=home;
		home=home->next;
		free(temp);
	}
}

void disp(){
	struct Node *temp=home;
	while(temp){
		printf("\n %d",temp->data);
		temp=temp->next;
	}
}
