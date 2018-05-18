#include<stdio.h>
#include<stdlib.h>

typedef struct node
{   // Node for binary search tree
    int data;
    struct node * left;
    struct node * right;

}node;




// Function for insering a node in the tree
node * insert_node(node * root, int a)
{
    if(root == NULL)
    {
        root = (node *)malloc(sizeof(node));
        root->data = a;
        root->left = NULL;
        root->right = NULL;
    }
    else
    {
        node * temp;
        temp = (node *)malloc(sizeof(node)); // Space allcated for the node
        temp->data = a;
        temp->left = NULL;
        temp->right = NULL;
        node * temp1 = root;
        while(1)
        {
            int key = temp1->data;
            if(key<=a){
                if(temp1->right==NULL){
                    temp1->right = temp;
                    break;
                }
                else
                {
                    temp1=temp1->right;
                }
            }
            else{
                if(temp1->left==NULL){
                    temp1->left = temp;
                    break;
                }
                else
                {
                    temp1=temp1->left;
                }

            }

        }



    }

    return root;
}

// Function for swapping node values
void swap(node *a, node *b){
    int temp1 = a->data;
    a->data = b->data;
    b->data = temp1;
}

// Function for finding the smallest node in the right subtree.
node * successor(node * temp, node * temp1)
{
    node * tmp = temp1;
    temp = tmp;
    if(tmp->right!=NULL)
    {
        tmp=tmp->right;
        while(tmp->left!=NULL)
        {
            temp=tmp;
            tmp=tmp->left;
        }

    }
    else
    {
        tmp = temp1;
    }
    return tmp;
}

// Funtion for finding the parent of node with smallest value in the right subtree.
node * parent_of_successor(node * temp, node * temp1)
{
    node * tmp = temp1;
    temp = tmp;
    tmp=tmp->right;
    while(tmp->left!=NULL)
    {
        temp=tmp;
        tmp=tmp->left;
    }
    return temp;
}


// Function for deleting a node with no children
node * delzero(node * root, node * pretemp, node * temp){
    if(temp == root)
        root = NULL;
    else
     {
        if (temp == pretemp->left)
            pretemp->left = NULL;
        else
            pretemp->right = NULL;
        free(temp);                         // Freeing the memory space occupied by the node
    }

    return root;
}


// Function for deleting a node with one child
node * delone(node * root, node * temp, node * temp1, int ty){


    switch(ty) 
    {
        case 1:
           
            if(temp1==root){
                root = root->left;
            }
            else if (temp1 == temp->left) {
                temp->left = temp1->left;
            } else {
                temp->right = temp1->left;
            }
            free(temp1);
            break;
        case 2:
            
            if(temp1==root){
                root = root->right;
            }
            else if (temp1 == temp->left) {
                temp->left = temp1->right;
            } else {
                temp->right = temp1->right;
            }
           
            free(temp1);

            break;
    }
return root;
}

 node * delete_node(node * root, int a){
    node * temp1 = root; // temp1 will store the value of node
    node * temp = root; // It will store the previous value of temp1


    // Traversing the tree ...
    while(1)
    {
        int key = temp1->data;
        if(key==a)
            break;

        else if(key<a)
        {
            if(temp1->right==NULL)
                return root;


            else
            {
                temp =  temp1;
                temp1=temp1->right;
            }
        }
        else
        {
            if(temp1->left==NULL)
                return root;


            else
            {
                temp = temp1;
                temp1=temp1->left;
            }

        }

    }
        int ty = 0;
        if(temp1->left == NULL && temp1->right == NULL)
            ty=0;                                           // node has no children
        else if(temp1->left != NULL && temp1->right == NULL)
            ty=1;                                           // node has one child, at right
        else if(temp1->left == NULL && temp1->right != NULL)
            ty=2;                                           // node has one child at left
        else if(temp1->left != NULL && temp1->right != NULL)
            ty=3;                                           // node has two children
    
    
        node * tmp;
        switch(ty){
            case 0:
                root = delzero(root, temp,temp1);
                break;
            case 1:
                root = delone(root,temp,temp1,ty);
                break;
            case 2:
                root = delone(root, temp,temp1,ty);
                break;
            case 3:
                tmp = successor(temp,temp1);
                swap(tmp,temp1);
                temp = parent_of_successor(temp,temp1);
                temp1 = tmp;
                if(temp1->right!=NULL)
                   root =  delone(root, temp,temp1,2);
                else
                   root = delzero(root, temp,temp1);

    }

    return root;
}

// Function for searching a node
// It will return 1 if a node is found
// It will return 0 if node is not found
int search(node * root, int a){
    node * temp1 = root; // temp1 will traverse through the tree
    while(1)
    {
        int key = temp1->data;
        if(key==a){         // Node is found
            return 1;
        }
        else if(key<a)
        {
            if(temp1->right==NULL){

                return 0;       //Node is not found
            }
            else
            {
                temp1=temp1->right;
            }
        }
        else{
            if(temp1->left==NULL){

                return 0;      //Node is not found

            }
            else
            {
                temp1=temp1->left;
            }

        }

    }


}


// Inorder printing of the tree
void print_inorder(node * root){
    node * temp = root;
    if(temp==NULL)
        return;
    else {
        print_inorder(temp->left);
        printf("%d ", temp->data);
        print_inorder(temp->right);
    }
}



int main(){
    node * root = NULL;

    // Inserting values in Binary Search Tree
    root = insert_node(root,60);
    root = insert_node(root,40);
    root = insert_node(root,30);
    root = insert_node(root,50);
    root = insert_node(root,80);
    root = insert_node(root,70);
    root = insert_node(root,90);



    //Searching a node
    int k =  search(root,20);

    if(k==1)
        printf("Node found\n"); // Node was found
    else if(k==0)
        printf("Node not found\n"); // Node was not found


    // deleting a node
    root = delete_node(root, 40);

    // Inorder printing of the tree
    print_inorder(root);
    printf("\n");

    // deleting another node
    root = delete_node(root, 30);

    // Inorder printing of the tree
    print_inorder(root);
    printf("\n");

    // deleting the root
    root = delete_node(root, 50);

    // Inorder printing of the tree
    print_inorder(root);
    printf("\n");


    return 0;
}
