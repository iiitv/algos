#define _XOPEN_SOURCE 500 /* Enable certain library functions (strdup) on linux. See feature_test_macros(7) */

#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#include <string.h>

struct avl_node_s {
	struct avl_node_s *left;
	struct avl_node_s *right;
	int value;
};

typedef struct avl_node_s avl_node_t;

struct avl_tree_s {
	struct avl_node_s *root;
};

typedef struct avl_tree_s avl_tree_t;


/* Create a new AVL tree. */
avl_tree_t *avl_create() {
	avl_tree_t *tree = NULL;

	if( ( tree = malloc( sizeof( avl_tree_t ) ) ) == NULL ) {
		return NULL;
	}

	tree->root = NULL;

	return tree;
}

/* Initialize a new node. */
avl_node_t *avl_create_node() {
	avl_node_t *node = NULL;
	
	if( ( node = malloc( sizeof( avl_node_t ) ) ) == NULL ) {
		return NULL;
	}

	node->left = NULL;
	node->right = NULL;
	node->value = 0;

	return node;	
}

/* Insert a new node. */
void avl_insert( avl_tree_t *tree, int value ) {
	avl_node_t *node = NULL;
	avl_node_t *next = NULL;
	avl_node_t *last = NULL;

	/* Well, there must be a first case */ 	
	if( tree->root == NULL ) {
		node = avl_create_node();
		node->value = value;

		tree->root = node;

	/* Okay.  We have a root already.  Where do we put this? */
	} else {
		next = tree->root;
		last = NULL;

		while( next != NULL ) {
			last = next;

			if( value < next->value ) {
				next = next->left;

			} else if( value > next->value ) {
				next = next->right;

			/* Have we already inserted this node? */
			} else if( value == next->value ) {
				/* This shouldn't happen. */	
			}
		}

		node = avl_create_node();
		node->value = value;

		if( value < last->value ) last->left = node;
		if( value > last->value ) last->right = node;
	}

}

/* Find the height of an AVL node recursively */
int avl_node_height( avl_node_t *node ) {
	int height_left = 0;
	int height_right = 0;

	if( node->left ) height_left = avl_node_height( node->left );
	if( node->right ) height_right = avl_node_height( node->right );

	return height_right > height_left ? ++height_right : ++height_left;
}

/* Find the balance of an AVL node */
int avl_node_balance( avl_node_t *node ) {
	int balance = 0;
	if( node->left  ) balance += avl_node_height( node->left );
	if( node->right ) balance -= avl_node_height( node->right );

	return balance;
}

/* Do a depth first traverse of a node. */
void avl_traverse_node_dfs( avl_node_t *node, int depth ) {
	int i = 0;

	if( node->left ) avl_traverse_node_dfs( node->left, depth + 2 );

	for( i = 0; i < depth; i++ ) putchar( ' ' );
	printf( "%d: %d\n", node->value, avl_node_balance( node ) );

	if( node->right ) avl_traverse_node_dfs( node->right, depth + 2 );
}

/* Do a depth first traverse of a tree. */
void avl_traverse_dfs( avl_tree_t *tree ) {

	avl_traverse_node_dfs( tree->root, 0 );
}

int main( int argc, char **argv ) {
	avl_tree_t *tree = NULL;

	tree = avl_create();

	avl_insert( tree, 2 );
	avl_insert( tree, 3 );
	avl_insert( tree, 4 );
	avl_insert( tree, 5 );
	avl_insert( tree, 1 );

	avl_traverse_dfs( tree );

	return 0;
}
