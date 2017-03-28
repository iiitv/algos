## How to contribute an implementation (code)?

* Have a look at open issues. They contain the list of algorithms/DS we plan to be implemented. Pick an unassigned issue.
* You can also create a new issue for an algorithm that is not in the list.
* Make sure you are assigned for the issue. You can assign an unassigned issue to yourself. 

> If you are not able to assign an issue to yourself, it means you are not a IIITV member. Get an [invite here](https://github.com/iiitv/getmein). If you already part of IIITV org, then maybe you are not a part of [Members team](https://github.com/orgs/iiitv/teams/members). Go add yourself. If any problems, open an issue at [getmein](https://github.com/iiitv/getmein).

* When assigned, also mention the languages you want to code in. So suppose if you don't want to code in a particular language, another person can be assigned to do so. 
* Code the algorithm/DS following the styleguide defined below.
* Send a PR. 
* Be sure to not include any compiled binaries in the patch.
* While sending a PR make sure you follow one PR per issue rule.


<a name="sa"></a>

## Suggesting an algorithm / DS

* First make sure you are not suggesting a duplicate.
* If not, proceed and create the issue. Make sure that you specify only one language in an issue. Create multiple issues for different languages.
* Title of issue should be of the following format -
    ```
        Algorithm/DS Name [Language]
    ```
    Also add corresponding language label (`lang-*`) to the issue.
* Please include at least one external link for the algorithm/DS in the issue's body for each issue. The link should explain the algorithm/problem/DS in detail.


<a name="cs"></a>

## Code Styleguide

* Code submitted should be modular. 
* Don't use global variables.
* Use separate folders for each concept. Folder name should be in full lowercase. If the algorithm/DS name has multiple words, separate them by underscores. (eg `longest_common_subsequence`)
* Filename should be derived from the folder name. (eg `longest_common_subsequence` becomes `longestCommonSubsequence.c` or `LongestCommonSubsequence.java`)
* Name of master function of the code should be kept same as filename to the best extent possible.
* Prefer classes instead of multiple helper functions (where applicable).
* Define `tester` code only in `main` routine.
* Use meaningful variable names and comments.
* No profanity.
* Use external libraries only when no other solution is possible/plausible.
* We have defined [skeleton codes](#samples) for some popular languages below. Please follow them whenever possible.


<a name="points"></a>

## Standalone points

* In some cases, C and C++ implementation will be similar. In that case, only the C implementation must be done.


<a name="improving"></a>

## Improving an implementation

* If you feel you can improve upon an implementation, feel free to open an issue discussing the improvements.
* If you are confident enough, you may directly open a PR with the required changes.


<a name="samples"></a>

## Samples

#### C

```c
void quicksort(int ar_size, int *ar) {
    /*
        Your implementation here...
    */
}

int main() {
	int ar_size = 4, i;
	int a[4] = {2, 3, 0, 4};
	quicksort(ar_size, a);

	for (i=0; i<ar_size; i++){
		printf("%d\n", a[i]);
	}
	return 0;
}
```

#### Python
```python
def quicksort(arr):
    #
    # Your implementation here...
    #


def main():
    arr = [2, 3, 0, 4]
    sorted_arr = quicksort(arr)
    print(sorted_arr)

    
if __name__ == '__main__':
    main()
```

#### Java
```java
public class QuickSort {
    
    static void quickSort(int[] a) {
        /*
            Your implementation here...
        */
    }
    
    public static void main(String[] args) {
        int[] arr = new int[] {2, 3, 0, 4};
        quickSort(arr);
        for(int element: arr) {
            System.out.println(element);
        }
    }
}
```