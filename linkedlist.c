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




void insertlast(LinkedList* list,int data) {
	Node *temp, *p,*prep;
	int c;
	//create room for new node and copy parameter data into it
	temp = (Node *) malloc( sizeof(Node) );
	(*temp).data = data;

	if (list->first == NULL) {
	temp->next =list->first;
	list->first = temp;
	return;
	}
	
	//when empty list or insert in list->firsting
    temp->next=NULL;
	//locate the position for insertion otherwise
	p = list->first;
p = list->first;
       	while(p->next!=NULL)
            p=p->next;
            p->next=temp;
        
return;
	

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
	if(pos==0){
		temp->next=list->first;
		list->first=temp;
	}
	else{

       	while(pos-->0&&p!=NULL)
	{
		prep=p;
		p=p->next;
	}
	prep->next=temp;
	temp->next=p;
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


	insertfront(list, 11);
	insertfront(list, 21);
	insertfront(list, 31);
	insertfront(list, 41);
	Print(list);

	printf("inser any\n");
	insertany(list,0,998);
	insertany(list,1,98);
	insertany(list,5,100);
	insertany(list,6,55);
	Print(list);

    printf("insert last\n");
	insertlast(list,3);
	insertlast(list,333);
	Print(list);



	printf("delete front\n");
	deletefront(list);
	Print(list);

	printf("delete last\n");
	deletelast(list);
	Print(list);


	printf("peek element\n");
	int element=peek(list,3);
	printf("element is %d\n",element);

	printf("check list \n");
	int empty=isEmpty(list);
	if(empty==0)
		printf("list is empty\n");
	else
		printf("list is not empty\n");



	printf("search element\n");
	int f=search(list,41);
	if(f)
		printf("found\n\n");
	else
		printf("not found\n\n");



	printf("destroy list\n");
	destroy(list);
		Print(list);
	return 0;
}
