#include <stdlib.h>
#include <stdio.h>

// Node for Binary Search Tree
struct node{
    int info;
    struct node *esq;
    struct node *dir;
};

// Defining the typedef for the node struct
typedef struct node BTS;

// Declaring the pointer to the node struct
BTS *root;

// Declaring all functions that are used
BTS *recursive_insert(BTS *r, int v);
void call_insert_by_root(BTS* root, int v);
void recursive_print_by_order(BTS *r);
void call_print_by_root(BTS *root);
BTS *recursive_search(BTS *root, int v);
BTS *search_by_root(BTS *root, int v);
BTS *recursive_remove(BTS *r, int v);
void call_remove_by_root(BTS *a, int v);

// Main function
int main(){
    printf("Create new tree");

    // Created an empty tree
    BTS *root = recursive_insert(NULL, 4);

    // Adding a few test entries
    call_insert_by_root(root, 10);
    call_insert_by_root(root, 2);
    call_insert_by_root(root, 7);
    call_insert_by_root(root, 18);
    call_insert_by_root(root, 1);
    call_insert_by_root(root, 3);
    call_insert_by_root(root, 15);
    call_insert_by_root(root, 20);

    // Test printing
    call_print_by_root(root);

    // Removing a value
    printf("\n\nRemove value 2");
    call_remove_by_root(root, 2);

    // Test printing without the value
    printf("\n\nPrint new tree");
    call_print_by_root(root);

    // Searching for some values in the tree
    printf("\n\nSearch value 3 and 10");
    printf("\n   >>> %d", search_by_root(root, 3)->info);
    printf("\n   >>> %d", search_by_root(root, 10)->info);

    return 0;
}

// This function looks for an appropriate place and inserts the new element
BTS *recursive_insert(BTS *r, int v){
    if(r == NULL){ // If the current node is null, it means that this is the appropriate location for that value
        r = (BTS*)malloc(sizeof(BTS));
        r->info = v;
        r->esq = r->dir = NULL;
    }
    else if(v < r->info) // If the value passed is less than the value of the current node, look for a place to the left
        r->esq = recursive_insert(r->esq, v);
    else // If the value passed is greater than the value of the current node, look for a place to the right
        r->dir = recursive_insert(r->dir, v);
    return r;
}

// This function receives the root and a value to fit it into the tree
void call_insert_by_root(BTS* root, int v){
    root = recursive_insert(root, v);
}

// This function prints all the elements searching from the last node on the left to the last node on the right, showing them in order.
void recursive_print_by_order(BTS *r){
    if(r!=NULL){
        recursive_print_by_order(r->esq);
        printf("\n   >>> %d", r->info);
        recursive_print_by_order(r->dir);
    }
}

// This function takes the root and prints all the values of the tree
void call_print_by_root(BTS *root){
    return recursive_print_by_order(root);
}

// This function does the recursive search from a node until it finds a value v
BTS *recursive_search(BTS *root, int v){
    if (root == NULL)
        return NULL;
    else if(root->info > v)
        return recursive_search(root->esq, v);
    else if(root->info < v)
        return recursive_search(root->dir, v);
    else return root;
}

// This function takes a root and looks for a value v in its tree
BTS *search_by_root(BTS *root, int v){
    return recursive_search(root, v);
}

// This function does the recursive search for the element and removes it
BTS *recursive_remove(BTS *r, int v){
    if(r == NULL) // If it is null it only returns.
        return NULL;
    else if(r->info > v) // If the value is less than the current node, it will look on the left.
        r->esq = recursive_remove(r->esq, v);
    else if(r->info < v) // If the value is greater than the current node, it looks for the right.
        r->dir = recursive_remove(r->dir, v);
    else{
        if(r->esq == NULL && r->dir == NULL){ // If you don't have any children, we release the allocation and change its value to NULL
            free(r);
            r = NULL;
        }
        else if(r->esq == NULL){ // If you only have the child on the right side, we need to connect the grandfather to the grandson
            BTS *t = r;
            r = r->dir;
            free(t);
        }
        else if(r->dir == NULL){ // if you only have the child on the left side, we need to connect the grandfather to the grandson
            BTS *t = r;
            r = r->esq;
            free(t);
        }
        else{ // If he has both children then it will be necessary to balance the tree again.
            BTS *f = r->esq;
            while(f->dir != NULL){
                f = f->dir;
            }
            r->info = f->info;
            f->info = v;
            r->esq = recursive_remove(r->esq, v);
        }
    }
    return r;
}

// This function receives the root and a value to be removed within the tree
void call_remove_by_root(BTS *root, int v){
    recursive_remove(root, v);
}

