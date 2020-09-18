
function fibonacci(num){
var arr=[];
arr.length=num+1;
for(let i=1;i<arr.length;i++)
{
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
