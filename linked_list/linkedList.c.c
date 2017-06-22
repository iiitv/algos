#include<stdio.h>
#include<stdlib.h>

struct Node {
	int d;			//integer type data
	struct Node* next;	// pointer to same structure
};

//  Creating node
struct Node* getNewNode(int data) {
	struct Node *nw_node;
	nw_node = (struct Node*) malloc(sizeof(struct Node));	//  nw_node a Node to be added
	if (nw_node == NULL) {
		return NULL;
	}
	nw_node->d = data;
	nw_node->next = NULL;
	return nw_node;
}

//  Adding at Front
int addFront(struct Node **start, struct Node* nw_node) {
	if (*start == NULL) {		// If list is empty make it first Node
		nw_node->next = NULL;
		*start = nw_node;
	} else {
		nw_node->next = *start;	// Else add address of first node to nw_node and make it first node i.e.'start'
		*start = nw_node;
	}
	return 1;
}

//  Adding at last
int addLast(struct Node **start, struct Node* nw_node) {
	struct Node* temp;		//  'temp' temporary node to traverse to last
	if (*start == NULL) {
		*start = nw_node;
	} else {
		temp = *start;
		while (temp->next != NULL) {	// Loop until we get last node
			temp = temp->next;
		}
		temp->next = nw_node;		// Assiging address of nw_node to next variable of last element of list
	}
	return 1;
}

//  Adding at given position
int addAtPos(struct Node **start, struct Node* nw_node, int pos) {
	struct Node* temp;		// 'temp' temporary node to traverse to last.
	if (*start == NULL) {
		*start = nw_node;
		return 1;
	} else {
		int i = 1;
		temp = *start;
		while (temp->next != NULL && i < pos-1) {	// Loop we reach to the position or last element of list is encountered
			temp = temp->next;
			i++;
		}
		if (i != pos-1) {
			return 0;
		} else {
			nw_node->next = temp->next;		// Placing address of next node to nw_node->next
			temp->next = nw_node;		// Assiging address of nw_node in list after temp node.
			return 1;
		}
	}
}

//  Deleting first element
struct Node* deleteFirst(struct Node **start) {
	if (*start == NULL) {
		return *start;
	} else {
		struct Node* temp = *start;
		*start = (*start)->next;		// Shifting 'start' to second node
		return temp;
	}
}

//  Deleting last element
struct Node* deleteLast(struct Node **start) {
	if (*start == NULL) {
		return NULL;
	} else {
		struct Node* temp = *start;		// temp node to go through each node
		if((*start)->next == NULL) {
			return 	*start;
		}
		while (temp->next->next != NULL)	// Loop until second last element is encountered
			temp = temp->next;
		struct Node* tmp = temp->next;		// storing last element
		temp->next = NULL;			// Removing last element
		return tmp;
	}
}

//  Delete element at given position
struct Node* deleteAtPos(struct Node **start, int pos) {
	if (*start == NULL) {
		return NULL;
	} else {
		struct Node* temp = *start;		// temp node to go through each node
		int i = 1;
		while (temp->next->next != NULL && i < pos-1) {	// until we reach to the position or last element of list is encountered
			temp = temp->next;
			i++;
		}
		if (i != pos-1) {
			printf("Invalid Index\n\n");
			return NULL;
			} else {
			struct Node* tmp = temp->next;
				temp->next = temp->next->next;	// Replacing address of position 'pos' with  node next to 'pos'
			return tmp;
		}
	}
}

//  To traverse whole list
void traverse(struct Node *start) {
	printf("Linked List\n");
	if(start == NULL) {
		printf("Linked List is Empty");
	} else {
		struct Node* temp = start;		// temp node to go through each node
		while (temp->next != NULL) {
			printf(" %d ->", temp->d);
			temp = temp->next;
		}
		printf("%d", temp->d);
	}
	printf("\n\n");
}

//  To search an element
int search(struct Node *start, int data) {
	struct Node* temp = start;
	int found = 0, i = 1;
	while (temp->next != NULL) {
		if(temp->d == data) {
			found = 1;
			break;
		}
		i++;
		temp = temp->next;
	}
	if (found != 0) {
		return i;
	} else {
		return -1;
	}
}

// to print search result
void searchResult(int d, int pos) {
	if(pos == -1) {
		printf("Element %d is not in list\n", d);
	} else {
		printf("Element %d is found at position %d\n", d, pos);
	}
	printf("\n");
}

void deleteResult(struct Node** node) {
	if(*node == NULL) {
		printf("Deletion is unsuccessfull\n");
	} else {
		printf("Node %d is deleted\n", (*node)->d);
		free(*node);
	}
	printf("\n");
}

void insertResult(int res, int d) {
	if(res == 0) {
		printf("Invalid Index\n");
	} else {
		printf("Element %d is inserted\n", d);
	}
	printf("\n");
}

int main() {
	struct Node *start = NULL;
	struct Node *newNode, *freeNode;
	int res;
	// Adding element to the list
	newNode = getNewNode(23);
	if (newNode != NULL) {
		res = addFront(&start, newNode);
		insertResult(res, 12);
	}
	traverse(start);
	// Adding elements at the end
	newNode = getNewNode(25);
	if (newNode != NULL) {
		res = addLast(&start, newNode);
		insertResult(res, 25);
	}
	newNode = getNewNode(46);
	if (newNode != NULL) {
		res = addLast(&start, newNode);
		insertResult(res, 46);
	}
	traverse(start);	
	// Adding elements to front
	newNode = getNewNode(12);
	if (newNode != NULL) {
		res = addFront(&start, newNode);
		insertResult(res, 12);	
	}
	newNode = getNewNode(11);
	if (newNode != NULL) {
		res = addFront(&start, newNode);
		insertResult(res, 11);	
	}
	traverse(start);
	// Adding element at a given index (Adding 14 at index 3)
	newNode = getNewNode(14);
	if (newNode != NULL) {
		res = addAtPos(&start, newNode, 3);
		insertResult(res, 14);	
	}
	traverse(start);
	// Removing First Element
	freeNode = deleteFirst(&start);
	deleteResult(&freeNode);
	traverse(start);
	
	// Search
	res = search(start, 14);
	searchResult(14, res);
	res = search(start, 12);
	searchResult(12, res);
	traverse(start);
	// Removing Last Element
	freeNode = deleteLast(&start);
	deleteResult(&freeNode);
	traverse(start);
	// Removing an element from a index
	freeNode = deleteAtPos(&start, 17);
	deleteResult(&freeNode);
	traverse(start);
	return 0;
	
}
