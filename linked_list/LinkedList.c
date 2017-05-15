#include<stdio.h>
#include<stdlib.h>
struct NODE {
	int d;		//integer type data  
	struct NODE* next;		//pointer to same structure
}*start;	//first node of the list

int main() {
	start=NULL;
	
	// Adding element to the list
	addFront(23);
    traverse();
             
	// Adding elements at the end
    addLast(25);
    addLast(46);
    traverse();
         
    // Adding elements to front
    addFront(12);
    addFront(11);
	traverse();
        
    // Adding element at a given index (Adding 4 at index 3)
    addAtPos(14, 3); 
    traverse();

    // Removing First Element
    deleteFirst();
    traverse();
	
	//search
	search(14);
	search(12);
	
	// Removing Last Element
	deleteLast();
    traverse();
         
   // Removing an element from a index
    deleteAtpos(17);
	traverse();

	return 0; 
}

//adding at First
void addFront(int data) {
	struct NODE* nw_node = (struct NODE*) malloc(sizeof(struct NODE)); 	//nw_node a node to be added
	nw_node->d = data;	//data
	if (start == NULL) {	//if list is empty make it first node
		
		nw_node->next = NULL;
		start = nw_node;
		
	}
	else {	
		nw_node->next = start;	//else add address of first node to nw_node and make it first node i.e.'start'
		start = nw_node;
	}
}

//adding at last
void addLast(int data) {
	struct NODE* nw_node = (struct NODE*) malloc(sizeof(struct NODE)); // nw_node a node to be added
	struct NODE* temp;  // 'temp' temporary node to traverse to last
	nw_node->next = NULL;		//last element must have null value in its next variable
	nw_node->d = data;	//data
	if (start == NULL) {
		start = nw_node;
	}
	else {
		temp = start;
		while (temp->next != NULL)		//loop until we get last node
		{
			temp = temp->next;
		}
		temp->next = nw_node;		//assiging address of nw_node to next variable of last element of list
	}
}

//adding at given position
void addAtPos(int data, int pos) {
	struct NODE* nw_node = (struct NODE*) malloc(sizeof(struct NODE));	// nw_node a node to be added,
	struct NODE* temp;	// 'temp' temporary node to traverse to last.
	nw_node->d = data;	//data 
	if (start == NULL){
		start = nw_node;
	}
	else {
		int i = 1;
		temp = start;
		while (temp->next != NULL && i < pos-1) //loop we reach to the position or last element of list is encountered
		{
			temp = temp->next;
			i++;
		}
		if (i != pos)
			printf("\nInvalid Index\n");
		else {
		    nw_node->next = temp->next;	//placing address of next node to nw_node->next
		    temp->next = nw_node;		//assiging address of nw_node in list after temp node.
		}	    
	}	
}

//deleting first element
void deleteFirst() {
	if (start == NULL)
		printf("List is Empty.");
	else {
		start = start->next;		//shifting 'start' to second node 
	}
}

//deleting last element
void deleteLast() {
	if (start == NULL)
		printf("List is Empty.");
	else {
		struct NODE* temp = start;	//temp node to go through each node
		while (temp->next->next != NULL)	//loop until second last element is encountered
			temp = temp->next;
		temp->next = NULL;		//removing last element
	}
}

//delete element at given position
void deleteAtpos(int pos) {
	if (start == NULL){
		printf("List is Empty");
	}
	else {
		struct NODE* temp = start;	//temp node to go through each node
		int i = 1;
		while (temp->next->next != NULL && i < pos-1)		//until we reach to the position or last element of list is encountered
		{	temp = temp->next;
			i++;
		}
		if (i != pos)
			printf("\nInvalid Index\n");
		else
		    temp->next = temp->next->next;	//replacing address of position 'pos' with  node next to 'pos'
	}
}

//to traverse whole list
void traverse() {
    printf("\nLinked List\n");
	if (start == NULL)
		printf("List is Empty");
	else
	{
		struct NODE* temp = start;	//temp node to go through each node
		while (temp->next != NULL){
			printf(" %d ->",temp->d);
			temp = temp->next;
		}
		printf(" %d",temp->d);
	}
	printf("\n");
}

//to search an element
void search(int data){
	struct NODE* temp = start;
	int found = 0,i = 1;
	while (temp->next != NULL){
		if(temp->d == data){
			found = 1;
			break;
		}
		i++;
		temp = temp->next;
	}
	if (found != 0)
		printf("\nElement %d is found at position %d\n",temp->d,i);
	else
		printf("\nElement is not in the list\n");
}