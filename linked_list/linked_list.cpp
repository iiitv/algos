    /*

     * C++ Program to Implement Linked List

     */

    #include<iostream>
    #include<cstdio>
    #include<cstdlib>

    using namespace std;

    /*

     * Node Declaration

     */

    struct node
    {
        int info;
        struct node *next;

    }*start;



    /*

     * Class Declaration

     */

    class single_llist

    {
        public:

            node* create_node(int);
            void insert_begin(int);
            void insert_pos(int, int);
            void insert_last(int);
            void delete_pos(int);
            void sort();
            void search(int);
            void update(int, int);
            void reverse();
            void display();

            single_llist()

            {
                start = NULL;
            }

    };


    /*

     * Creating Node

     */


    node *single_llist::create_node(int value)
    {

        struct node *temp, *s;
        temp = new(struct node);
        if (temp == NULL)
        {
            cout<<"Memory not allocated "<<endl;
            return 0;
        }
        else
        {
            temp->info = value;
            temp->next = NULL;
            return temp;
        }

    }



    /*

     * Inserting element in beginning

     */

    void single_llist::insert_begin(int a)

    {

        int value=a;
        struct node *temp, *p;
        temp = create_node(value);
        if (start == NULL)
        {
            start = temp;
            start->next = NULL;
        }
        else

        {
            p = start;
            start = temp;
            start->next = p;
        }

        cout<<"Element Inserted at beginning"<<endl;

    }



    /*

     * Inserting Node at last

     */

    void single_llist::insert_last(int c)
    {

        int value=c;
        struct node *temp, *s;
        temp = create_node(value);
        s = start;
        while (s->next != NULL)
        {
            s = s->next;
        }
        temp->next = NULL;
        s->next = temp;
        cout<<"Element Inserted at last"<<endl;

    }



    /*

     * Insertion of node at a given position

     */

    void single_llist::insert_pos(int d, int e)
    {

        int value=e, pos=d, counter = 0;
        struct node *temp, *s, *ptr;
        temp = create_node(value);
        int i;
        s = start;
        while (s != NULL)
        {
            s = s->next;
            counter++;
        }

        if (pos == 1)
        {
            if (start == NULL)
            {
                start = temp;
                start->next = NULL;
            }
            else
            {
                ptr = start;
                start = temp;
                start->next = ptr;
            }
        }
        else if (pos > 1  && pos <= counter)
        {
            s = start;
            for (i = 1; i < pos; i++)
            {
                ptr = s;
                s = s->next;
            }
            ptr->next = temp;
            temp->next = s;
        }
        else
        {
            cout<<"Positon out of range"<<endl;
        }
    }

    /*

     * Sorting Link List

     */

    void single_llist::sort()
    {
        struct node *ptr, *s;
        int value;
        if (start == NULL)
        {
            cout<<"The List is empty"<<endl;
            return;
        }
        ptr = start;
        while (ptr != NULL)
        {
            for (s = ptr->next;s !=NULL;s = s->next)
            {
                if (ptr->info > s->info)
                {
                    value = ptr->info;
                    ptr->info = s->info;
                    s->info = value;
                }

            }
            ptr = ptr->next;
        }
    }

    /*

     * Delete element at a given position

     */

    void single_llist::delete_pos(int g)
    {
        int pos, counter = 0;
        if (start == NULL)
        {
            cout<<"List is empty"<<endl;
            return;
        }
        pos=g;
        struct node *s;
        s = start;
        if (pos == 1)
        {
            start = s->next;
        }
        else
        {
            struct node *ptr;
            while (s != NULL)
            {
                s = s->next;
                counter++;
            }
            if (pos > 0 && pos <= counter)
            {
                s = start;
                for (int i = 1;i < pos;i++)
                {
                    ptr = s;
                    s = s->next;
                }
                ptr->next = s->next;
            }
            else
            {
                cout<<"Position out of range"<<endl;
            }
            free(s);
            cout<<"Element Deleted"<<endl;
        }
    }

    /*

     * Update a given Node

     */

    void single_llist::update(int h,int i)
    {
        int value=i, pos=h;
        if (start == NULL)
        {
            cout<<"List is empty"<<endl;
            return;
        }
        struct node *s, *ptr;
        s = start;
        if (pos == 1)
        {
            start->info = value;
        }
        else
        {
            for (int i = 0;i < pos - 1;i++)
            {
                if (s == NULL)
                {
                    cout<<"There are less than "<<pos<<" elements";
                    return;
                }
                s = s->next;
            }
            s->info = value;
        }
        cout<<"Node Updated"<<endl;
    }

    /*

     * Searching an element

     */

    void single_llist::search(int y)
    {
        int value=y, pos = 0;
        bool flag = false;
        if (start == NULL)
        {
            cout<<"List is empty"<<endl;
            return;
        }
        struct node *s;
        s = start;
        while (s != NULL)
        {
            pos++;
            if (s->info == value)
            {
                flag = true;
                cout<<"Element "<<value<<" is found at position "<<pos<<endl;
            }
            s = s->next;
        }
        if (!flag)
            cout<<"Element "<<value<<" not found in the list"<<endl;
    }

    /*

     * Reverse Link List

     */

    void single_llist::reverse()
    {
        struct node *ptr1, *ptr2, *ptr3;
        if (start == NULL)
        {
            cout<<"List is empty"<<endl;
            return;
        }
        if (start->next == NULL)
        {
            return;
        }
        ptr1 = start;
        ptr2 = ptr1->next;
        ptr3 = ptr2->next;
        ptr1->next = NULL;
        ptr2->next = ptr1;
        while (ptr3 != NULL)
        {
            ptr1 = ptr2;
            ptr2 = ptr3;
            ptr3 = ptr3->next;
            ptr2->next = ptr1;
        }
        start = ptr2;
    }

    /*

     * Display Elements of a link list

     */

    void single_llist::display()
    {
        struct node *temp;
        if (start == NULL)
        {
            cout<<"The List is Empty"<<endl;
            return;
        }
        temp = start;
        cout<<"Elements of list are: "<<endl;
        while (temp != NULL)
        {
            cout<<temp->info<<"->";
            temp = temp->next;
        }
        cout<<"NULL"<<endl;
    }

    /*

     * Main

     */

    int main()
    {
        int choice, nodes, element, position, i;
        single_llist sl;
        start = NULL;
        //"Inserting Node at Beginning: "
        sl.insert_begin(5);
        //"Inserting Node at Last: "
        sl.insert_last(7);
        //"Inserting Node at a given position:(pos,val)"
        sl.insert_pos(1,4);
        //"Sort Link List: "
        sl.sort();
        //"Delete a particular node: "
        sl.delete_pos(7);
        //"Update Node Value:(pos,val)"
        sl.update(1,4);
        //"Search element in Link List: "
        sl.search(5);
        //"Display elements of link list: "
        sl.display();
        //"Reverse elements of Link List"
        sl.reverse();
        return 0;
    }
