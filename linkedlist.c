#include <stdio.h>
#include <stdlib.h>
#include <string.h>


struct _Node {
	int data;
	struct _Node* next;
};
typedef struct _Node Node;

typedef struct {
	Node* first;
} LinkedList;

LinkedList* newLinkedList();
short isEmpty(LinkedList* list);

LinkedList* newLinkedList()
{
	LinkedList* list;
	list = (LinkedList*) malloc( sizeof (LinkedList) );
	list->first = NULL;
	return list;
}









void insertfront(LinkedList* list,int data) {
	Node *temp, *p;
	int c;
	//create room for new node and copy parameter data into it
	temp = (Node *) malloc( sizeof(Node) );
	(*temp).data = data;
	//when empty list or insert in list->firsting
	if (list->first == NULL) {
	temp->next =list->first;
	list->first = temp;
	return;
	}
	
	p = list->first;
       temp->next=p;

	//p points to the node after which new node to be inserted
	list->first=temp;
}






void insertlast(LinkedList* list,int data) {
	Node *temp, *p;
	int c;
	//create room for new node and copy parameter data into it
	temp = (Node *) malloc( sizeof(Node) );
	(*temp).data = data;
	//when empty list or insert in list->firsting
	if (list->first == NULL) {
	temp->next =list->first;
	list->first = temp;
	return;
	}
	//locate the position for insertion otherwise
	p = list->first;
       	while(p->next!=NULL)
	p=p->next;
	p->next=temp;

	//p points to the node after which new node to be inserted
	
}


void insertany(LinkedList* list,int pos,int data) {
	Node *temp, *p,*prep;
	int c;
	//create room for new node and copy parameter data into it
	temp = (Node *) malloc( sizeof(Node) );
	(*temp).data = data;
	//when empty list or insert in list->firsting
	if (list->first == NULL) {
	temp->next =list->first;
	list->first = temp;
	return;
	}
	//locate the position for insertion otherwise
	p = list->first;
	prep = list->first;
       	while(pos-->0&&p->next!=NULL)
	{
		prep=p;
		p=p->next;
	}
	prep->next=temp;
	temp->next=p;

	//p points to the node after which new node to be inserted
	
}






void Print(LinkedList* list)
{
Node *p;
int j=0;
p=list->first;
while ( p!= NULL )
	{
		j++;
		printf("%d\t\n",(p->data));
		p = p->next;
	}

}








void deletefront(LinkedList* list) {
	if(isEmpty(list)==0){
		printf("list is empty\n");
	}
	else{
		Node *p=list->first;
		list->first=p->next;
	}
}


void deletelast(LinkedList* list) {
	if(isEmpty(list)==0){
		printf("list is empty\n");
	}
	else{
		Node *p=list->first,*prep=list->first;
	
		while(p->next->next!=NULL)
		{	
			p=p->next;
		}
		p->next=NULL;
	}
}





int peek(LinkedList* list, int pos) {

	int dummy;
	Node *p=list->first;
	while(--pos>0&&p!=NULL)
	{
		p=p->next;
	}


	dummy=p->data;
	return dummy;
}





short isEmpty(LinkedList* list) {
//returns true if list is empty, false otherwise
	if(list->first==NULL)
		return 0;
	else	
		return 1;
}






int search(LinkedList* list, int x) 
{	
	Node *p=list->first;
	while(p->next!=NULL&&x!=p->data)
		p=p->next;
	if(x==p->data)
		return 1;
	else
	     return 0;

}





void destroy(LinkedList* list){
//removes all nodes and destroyed storage used by all nodes.
	Node* p;
	while( list->first ) {
	p = list->first;
	list->first = p->next;
	free( p );
	}
}




int main() {
	

	LinkedList* list;
	list = newLinkedList();

	deletefront(list);
	insertfront(list, 11);
	insertfront(list, 21);
	insertfront(list, 31);
	insertfront(list, 41);
	Print(list);

	
	insertany(list,4,998);
	Print(list);

	insertlast(list, 99);
	insertlast(list, 19798);
	Print(list);

	deletefront(list);
	Print(list);

	deletelast(list);
	Print(list);
	
	int element=peek(list,3);
	printf("element is %d\n",element);
	int empty=isEmpty(list);
	if(empty==0)
		printf("list is empty\n");
	else
		printf("list is not empty\n");
	



	int f=search(list,41);
	if(f)
		printf("found\n");
	else 
		printf("not found\n");


	destroy(list);
	Print(list);
	return 0;
}
