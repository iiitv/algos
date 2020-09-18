/*fibonacci function is going to take a number "num"
and going to show the "num" th Fibonacci number on the console*/
function fibonacci(num){
	/*declaring an array*/
var arr=[];
	/*array's num+1 th position will contain fibonacci number at num th position*/
arr.length=num+1;
for(let i=1;i<arr.length;i++)
{
	/* Base case*/
  if(i===1 ||i===2)
  {
   arr[i]=1;
  }
  else{
    arr[i]=arr[i-1]+arr[i-2];
  }
}
console.log(arr[num]);
}

fibonacci(20);

Output: 6765
