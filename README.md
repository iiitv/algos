# Algos

Community (college) maintained list of algorithm implementations and codes. 
**For now, we are only accepting contributions from IIITV college students**.


## Resources

* [Popular Data Structures and Algorithms - Codechef](https://discuss.codechef.com/questions/48877/data-structures-and-algorithms)


## How to contribute ?

* Have a look at open issues. They contain the list of algorithms we plan to be implemented. Pick an unassigned issue.
* You can also create a new issue for an algorithm that is not in the list.
* Make sure you are assigned for the issue. 
* Code the algorithm following the styleguide defined below.
* Send a PR.


## Code Styleguide

* Code submitted should be modular. 
* Don't use global variables.
* Folder name of algorithm should match filename (excluding the extension).
* Filename of code should be kept same as master function of the code to the best extent possible.
* Prefer classes instead of multiple helper functions (where applicable).
* Define `tester` code only in `main` routine.
* Use meaningful variable names and comments.
* No profanity.


## Samples

#### C

```c
void quicksort(int ar_size, int *  ar) {
  // stuff
  // stuff
}

int main(){
	int ar_size = 4, i;
	int a[4];
	a[0] = 2; a[1] = 3; a[2] = 0; a[3] = 4;
	quicksort(ar_size, a);

	for (i=0; i<ar_size; i++){
		printf("%d\n", a[i]);
	}
	return 0;
}
```



## Credits

Idea by [@Monal5031](https://github.com/Monal5031)
