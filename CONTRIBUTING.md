## How to contribute an implementation (code) ?

* Have a look at open issues. They contain the list of algorithms we plan to be implemented. Pick an unassigned issue.
* You can also create a new issue for an algorithm that is not in the list.
* Make sure you are assigned for the issue. 
* When assigned, also mention the languages you want to code in. So suppose if you don't want to code in a particular language, another person can be assigned to do so. 
* Code the algorithm following the styleguide defined below.
* Send a PR.


<a name="sa"></a>

## Suggesting an algorithm

* First make sure you are not suggesting a duplicate.
* If not, proceed and create the issue.
* Please include at least one external link for the algorithm in the issue's body which explains the algorithm/problem in detail.


<a name="cs"></a>

## Code Styleguide

* Code submitted should be modular. 
* Don't use global variables.
* Folder name of algorithm should match filename (excluding the extension).
* Filename of code should be kept same as master function of the code to the best extent possible.
* Prefer classes instead of multiple helper functions (where applicable).
* Define `tester` code only in `main` routine.
* Use meaningful variable names and comments.
* No profanity.


<a name="points"></a>

## Standalone points

* In some cases, C and C++ implementation will be similar. In that case, only the C implementation must be done.


<a name="improving"></a>

## Improving an implementation

* If you feel you can improve upon an implementation, feel free to open an issue discussing the improvements.
* If you are confident enough, you may directly open a PR with the required changes.


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

