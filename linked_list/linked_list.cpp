/*
* C++ Program to Implement Linked List
*/
#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;
/*
* Node Declaration
*/
class node
{
public:
	int info;
	class node *next;
}*start;
/*
* Class Declaration
*/
class single_list
{
public:
	/*
	* Creating Node
	*/
	node* create_node(int value)
	{
		class node *temp, *s;
		temp = new(class node);
		if (temp == NULL)
		{
			cout << "Memory not allocated " << endl;
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
	void insert_begin(int a)
	{
		int value = a;
		class node *temp, *p;
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
		cout << "Element Inserted at beginning" << endl;
	}
	/*
	* Insertion of node at a given position
	*/
	void insert_pos(int d, int e)
	{
		int value = e, pos = d, counter = 0;
		class node *temp, *s, *ptr;
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
			cout << "Positon out of range" << endl;
		}
	}
	/*
	* Inserting Node at last
	*/
	void insert_last(int c)
	{
		int value = c;
		class node *temp, *s;
		temp = create_node(value);
		s = start;
		while (s->next != NULL)
		{
			s = s->next;
		}
		temp->next = NULL;
		s->next = temp;
		cout << "Element Inserted at last" << endl;
	}
	/*
	* Delete element at a given position
	*/
	void delete_pos(int g)
	{
		int pos;
		if (start == NULL)
		{
			cout << "List is empty" << endl;
			return;
		}
		pos = g;
		class node *s;
		s = start;
		if (pos == 1)
		{
			start = s->next;
		}
		else
		{
			int counter = 0;
			while (s != NULL)
			{
				s = s->next;
				counter++;
			}
			if (pos > 0 && pos <= counter)
			{
				class node *ptr;
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
				cout << "Position out of range" << endl;
			}
			free(s);
			cout << "Element Deleted" << endl;
		}
	}
	/*
	* Sorting Link List
	*/
	void sort()
	{
		class node *ptr, *s;
		int value;
		if (start == NULL)
		{
			cout << "The List is empty" << endl;
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
	* Searching an element
	*/
	void search(int y)
	{
		int value = y, pos = 0;
		bool flag = false;
		if (start == NULL)
		{
			cout << "List is empty" << endl;
			return;
		}
		class node *s;
		s = start;
		while (s != NULL)
		{
			pos++;
			if (s->info == value)
			{
				flag = true;
				cout << "Element " << value << " is found at position " << pos << endl;
			}
			s = s->next;
		}
		if (!flag)
		cout << "Element " << value << " not found in the list" << endl;
	}
	/*
	* Update a given Node
	*/
	void update(int h,int i)
	{
		int value = i, pos = h;
		if (start == NULL)
		{
			cout << "List is empty" << endl;
			return;
		}
		class node *s, *ptr;
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
					cout << "There are less than " << pos << " elements";
					return;
				}
				s = s->next;
			}
			s->info = value;
		}
		cout << "Node Updated" << endl;
	}
	/*
	* Reverse Link List
	*/
	void reverse()
	{
		class node *ptr1, *ptr2, *ptr3;
		if (start == NULL)
		{
			cout << "List is empty" << endl;
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
	void display()
	{
		class node *temp;
		if (start == NULL)
		{
			cout << "The List is Empty" << endl;
			return;
		}
		temp = start;
		cout << "Elements of list are: " << endl;
		while (temp != NULL)
		{
			cout << temp->info << "->";
			temp = temp->next;
		}
		cout << "NULL" << endl;
	}
	single_list()
	{
		start = NULL;
	}
};
/*
* Main
*/
int main()
{
	int choice, nodes, element, position, i;
	single_list sl;
	start = NULL;
	sl.insert_begin(5);
	sl.insert_last(7);
	sl.insert_pos(1, 4);
	sl.sort();
	sl.delete_pos(7);
	sl.update(1, 4);
	sl.search(5);
	sl.display();
	sl.reverse();
	return 0;
}
