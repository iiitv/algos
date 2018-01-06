// Implements an AVL tree in C

#include <stdlib.h>
#include <stdio.h>

#define max(a,b) (((a)>(b))?(a):(b))

typedef struct AVLNode {
	struct AVLNode* left;		// left child node
	struct AVLNode* right;		// right child node
	struct AVLNode* parent;		// parent node
	int value; 					// integer type data
	int height;					// current height in the tree
} AVLNode;

typedef struct AVLTree {
	struct AVLNode* root;		// the tree's root node
	int size;					// the tree's size
} AVLTree;


// Adjusts the height of the given node respective to its current position
void adjust_height(AVLNode* avln) {
	if (avln->left == NULL && avln->right == NULL) {
		avln->height = 1;
	} else if (avln->left == NULL) {
		avln->height = 1 + avln->right->height;
	} else if (avln->right == NULL) {
		avln->height = 1 + avln->left->height;
	} else {
		avln->height = 1 + max(avln->left->height, avln->right->height);
	}
}

// Performs a left rotation on the given node in the given tree
void rotate_left(AVLTree* avlt, AVLNode* avln) {
	AVLNode* y = avln->right;
	avln->right = y->left;

	if (y->left != NULL) {
		y->left->parent = avln;
	}

	y->parent = avln->parent;

	if (avln->parent == NULL) {
		avlt->root = y;
	} else if (avln->value == avln->parent->left->value) {
		avln->parent->left = y;
	} else {
		avln->parent->right = y;
	}

	y->left = avln;
	avln->parent = y;

	adjust_height(avln);
	adjust_height(y);
}

// Performs a right rotation on the given node in the given tree
void rotate_right(AVLTree* avlt, AVLNode* avln) {
	AVLNode* x = avln->left;
	avln->left = x->right;

	if (x->right != NULL) {
		x->right->parent = avln;
	}

	x->parent = avln->parent;

	if (avln->parent == NULL) {
		avlt->root = x;
	} else if (avln->value == avln->parent->right->value) {
		avln->parent->right = x;
	} else {
		avln->parent->left = x;
	}

	x->right = avln;
	avln->parent = x;

	adjust_height(avln);
	adjust_height(x);
}

// Helper method to get the height of the given node
// Used to easily implement the required NULL-checks
int get_height(AVLNode* avln) {
	if (avln == NULL) {
		return 0;
	} else {
		return avln->height;
	}
}

// Helper method to get the height of the node to the left
// Used to easily implement the required NULL-checks
int get_left_height(AVLNode* avln) {
	if (avln == NULL || avln->left == NULL) {
		return 0;
	} else {
		return avln->left->height;
	}
}

// Helper method to get the height of the node to the right
// Used to easily implement the required NULL-checks
int get_right_height(AVLNode* avln) {
	if (avln == NULL || avln->right == NULL) {
		return 0;
	} else {
		return avln->right->height;
	}
}

// Balances the sub-tree below the given node
void balance(AVLTree* avlt, AVLNode* avln) {
	// check if the tree is left-heavy
	if (get_height(avln->left) > get_height(avln->right) + 1) {
		if (get_left_height(avln->left) < get_right_height(avln->left)) {
			rotate_left(avlt, avln->left);
		}
		rotate_right(avlt, avln);

	// check if the tree is right-heavy
	} else if (get_height(avln->right) > get_height(avln->left) + 1) {
		if (get_right_height(avln->right) < get_left_height(avln->right)) {
			rotate_right(avlt, avln->right);
		}
		rotate_left(avlt, avln);
	}
}

// Recursive method to insert a value into the tree, NOT to be used by the outside
void insert_value_recursive(AVLTree* avlt, AVLNode** avln, AVLNode* parent, int value) {
	// If the given node is NULL (i.e. the tree is empty or we have reached a leaf node)
	if (*avln == NULL) {
		*avln = malloc(sizeof(AVLNode));
		(*avln)->left = NULL;
		(*avln)->right = NULL;
		(*avln)->parent = parent;
		(*avln)->value = value;
		(*avln)->height = 1;

		avlt->size++;

	// If the the given value is lower than the currently viewed node, view the left child
	} else if (value < (*avln)->value) {
		insert_value_recursive(avlt, &(*avln)->left, *avln, value);

	// If the the given value is greater than the currently viewed node, view the right child
	} else if (value > (*avln)->value) {
		insert_value_recursive(avlt, &(*avln)->right, *avln, value);

	// If the the given value is equal to the currently viewed node, return because we don't allow double entries
	} else {
		return;
	}

	// Determine the height of the newly created node
	(*avln)->height = 1 + max(get_height((*avln)->left), get_height((*avln)->right));

	// Re-balance the node to check for possibly needed rotations
	balance(avlt, *avln);
}

// Inserts the given value into the tree
void insert_value(AVLTree* avlt, int value) {
	// Use the recursive function to allow the function to correctly position the newly created node
	insert_value_recursive(avlt, &avlt->root, NULL, value);
}

void traverse_in_order(AVLNode* avln) {
	if (avln != NULL) {
		// traverse the left sub-tree first
		traverse_in_order(avln->left);

		// print the current node's value
		printf("%d ", avln->value);

		// traverse the right sub-tree later
		traverse_in_order(avln->right);
	}
}

int main() {
	// create a new AVLTree
	AVLTree avlt;
	avlt.root = NULL;
	avlt.size = 0;

	insert_value(&avlt, 2);
	insert_value(&avlt, 5);
	insert_value(&avlt, 7);
	insert_value(&avlt, 3);
	insert_value(&avlt, 10);
	insert_value(&avlt, 1);
	insert_value(&avlt, 20);

	traverse_in_order((&avlt)->root);
	printf("\n");
}
