package main

//Imported Libraries
import (
	"fmt"
)

//Constants
const x  = 10

//Implementation of the stack structure
type stack struct {
	items [x] string
}
//pop from the stack
func (a *stack) push (value string){
	var found bool = false
	for index,valuea := range a.items{
		if valuea == "" {
			a.items[index]=value
			found=true
			break
		}
	}
	if found == false{
		fmt.Printf("Stack is full, Try on PUSH something outside\n")
	}
}

//pop form the stack
func (a *stack) pop()  {
	var empty bool = true
	for index := range a.items{
		if a.items[x-index-1]!="" {
			a.items[x-index-1]=""
			empty= false
			break
		}
	}
	if empty==true{
		fmt.Printf("Stack is empty! Cannot pop! Try on push in something\n")
	}
}

//print the stack
func (a *stack) printstack()  {
	fmt.Printf("(")
	for index := range a.items{
		value := "None"
		if a.items[index]!=""{
			value=a.items[index]
		}
		fmt.Printf("%s,",value)
	}
	fmt.Println(")")
}

//peek for the last value of the stack
func (a *stack) peek()  {
	var empty bool = true
	for index := range a.items{
		if a.items[x-index-1] != ""{
			fmt.Println(a.items[x-index-1])
			empty = false
			break
		}
	}
	if empty == true {
		fmt.Println("The Stack is Empty. Can't print for a last value")
	}
}

//End of Implementation of the Stack

//Start of the Main programme
func main(){
	mydata := new(stack)
	mydata.push("Kamal")
	mydata.push("Saman")
	mydata.push("Nimal")
	mydata.push("Ruwan")
	mydata.push("Kumara")
	mydata.printstack()
	mydata.peek()
	mydata.pop()
	mydata.peek()
	mydata.pop()
	mydata.peek()
	mydata.printstack()
}
//End of the Main programme