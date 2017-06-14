#include <stdio.h>
#include <stdlib.h>

typedef struct stack {
	void *data;
	struct stack *next;
} Stack;

Stack *new_stack_node(void *data) {
	Stack *new_node = (Stack*) malloc(sizeof(Stack));
	if (new_node == NULL) {
		return NULL;
	}
	new_node -> data = data;
	new_node -> next = NULL;
	return new_node;
}

int push(Stack **stack, void *data) {
	Stack *new_node = new_stack_node(data);
	if (new_node == NULL) {
		return 0;
	}
	new_node -> next = *stack;
	*stack = new_node;
	return 1;
}

void *pop(Stack **stack) {
	if (*stack == NULL) {
		return NULL;
	}
	Stack *temp = *stack;
	*stack = (*stack) -> next;
	temp -> next = NULL;
	void *data = temp -> data;
	free(temp);
	return data;
}

int main() {
	int a = 5;
	float b = 6.0;
	char c[] = "Hello World!";
	Stack *st = NULL;
	push(&st, (void*) (&a));
	push(&st, (void*) (&b));
	push(&st, (void*) (c));
	char *c_popped = (char*) pop(&st);
	float b_popped = *((float*) pop(&st));
	int a_popped = *((int*) pop(&st));
	printf("%d %f %s\n", a_popped, b_popped, c_popped);
	if (pop(&st) == NULL) {
		printf("Unable to pop from empty stack\n");
	}
	return 0;
}
