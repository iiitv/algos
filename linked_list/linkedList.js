class Node {
	// Constructs Node
	constructor (data) {
		this.data = data;
		this.next = null;
	}
}

class LinkedList {
	// Initialises Linked List
	constructor (size = 0) {
		this.head = null;
		this.length = size;
	}

	// Inserts Element with value at index
	add (value, index) {
		let temp = this.head;
		if (index === 0) {
			let n = new Node(value);
			n.next = this.head;
			this.head = n;
		} else if (index < 0 || index >= this.length) {
			throw new Error('Index Out of Bound');
		} else {
			for (let i = 0; i < index - 1; i++) {
				temp = temp.next;
			}
			let n = new Node(value);
			n.next = temp.next;
			temp.next = n;
		}
		this.length++;
	}

	// Adds value at front of Linked List
	addFirst (value) {
		return this.add(value, 0);
	}

	// Adds value at end of Linked List
	addLast (value) {
		if (this.head === null) {
			this.addFirst(value);
		} else {
			let temp = this.head;
			while (temp.next !== null) {
				temp = temp.next;
			}
			let n = new Node(value);
			temp.next = n;
			this.length++;
		}
	}

	// Remove value from index in Linked List
	remove (index) {
		if (this.isEmpty()) {
			throw new Error('List is Empty');
		} else if (index < 0 || index >= this.length) {
			throw new Error('Index out of Bound');
		} else if (index === 0) {
			this.head = this.head.next;
		} else {
			let temp = this.head;
			if (temp.next == null) {
				this.head = null;
			} else {
				for (let i = 0; i < index - 1; i++) {
					temp = temp.next;
				}
				temp.next = temp.next.next;
			}
		}
		this.length--;
	}

	// Removes front element from Linked List
	removeFront () {
		this.remove(0);
	}

	// Removes last element from Linked List
	removeLast () {
		this.remove(this.length - 1);
	}

	// Searches and removes element with data = value.
	removeByValue (value) {
		this.remove(this.findFirst(value));
	}

	// Search and returns index.
	search (input) {
		let head = this.head;
		for (let i = 0; i < this.length; i++) {
			if (head.data === input) {
				return i;
			} else {
				head = head.next;
			}
		}
		throw new Error('Value not found');
	}

	// Search and return index of first occurence of input.
	findFirst (input) {
		return this.search(input);
	}

	// Search and return index of last occurence of input.
	findLast (input) {
		let newList = new LinkedList();
		newList = this.clone();
		newList.reverse();
		return this.length - newList.search(input) - 1;
	}

	// Sets Data of input at index.
	setData (input, index) {
		// If index is >= size of Linked List, It adds the value.
		if (index >= this.length) {
			this.add(input, index);
		} else {
			// If index already have some data it replaces it with input.
			let head = this.head;
			for (let i = 0; i < this.length; i++) {
				if (i === index) {
					head.data = input;
				}
				head = head.next;
			}
		}
	}

	// Clones and returns a newList.
	clone () {
		let newList = new LinkedList();
		let temp = this.head;
		while (temp.next) {
			newList.addLast(temp.data);
			temp = temp.next;
		}
		newList.addLast(temp.data);
		return newList;
	}

	// Reverses the existing Linked List.
	reverse () {
		let prev = null;
		let current = this.head;
		while (current) {
			let next = current.next;
			current.next = prev;
			prev = current;
			current = next;
		}
		this.head = prev;
	}

	// Checks if Linked List is empty.
	isEmpty () {
		return (this.length === 0);
	}

	// Clears the Linked List.
	clear () {
		this.head = null;
		this.length = 0;
	}

	// Returns the Linked List in List form.
	show () {
		let list = [];
		let head = this.head;
		while (head) {
			list.push(head.data);
			head = head.next;
		}
		return list;
	}
}

function main () {
	let linkedList = new LinkedList();

	linkedList.add(5, 0);
	console.log(linkedList.show());
	console.log('Size : ' + linkedList.length);

	linkedList.addFirst(25);
	linkedList.addFirst(251);
	console.log(linkedList.show());
	console.log('Size : ' + linkedList.length);

	linkedList.addFirst(5);
	console.log(linkedList.show());
	console.log('Size : ' + linkedList.length);

	try {
		console.log('Fist Occurrence at index: ' + linkedList.findFirst(5));
	} catch (err) {
		console.log('Value not found');
	}

	try {
		console.log('Last Occurrence at index: ' + linkedList.findLast(5));
	} catch (err) {
		console.log('Value not found');
	}

	try {
		linkedList.setData(12325, 1);
		console.log(linkedList.show());
		console.log('Size : ' + linkedList.length);
	} catch (err) {
		console.log('Index out of bound');
	}

	try {
		linkedList.removeByValue(12325);
		console.log(linkedList.show());
		console.log('Size : ' + linkedList.length);
	} catch (err) {
		console.log('Value not found');
	}

	linkedList.addLast(125);
	linkedList.addLast(11);
	console.log(linkedList.show());
	console.log('Size : ' + linkedList.length);

	try {
		console.log('Element found at index: ' + linkedList.search(1125));
	} catch (err) {
		console.log('Value not found');
	}

	console.log('Cloned : ', linkedList.clone().show());

	try {
		linkedList.remove(6);
		console.log(linkedList.show());
		console.log('Size : ' + linkedList.length);
	} catch (err) {
		console.log('Index Out of Bound');
	}

	try {
		linkedList.remove(2);
	} catch (err) {
		console.log('Index Out of Bound');
	}
	console.log(linkedList.show());
	console.log('Size : ' + linkedList.length);

	linkedList.removeFront();
	console.log(linkedList.show());
	console.log('Size : ' + linkedList.length);

	linkedList.removeLast();
	console.log(linkedList.show());
	console.log('Size : ' + linkedList.length);

	linkedList.clear();
	console.log(linkedList.show());
	console.log('Size : ' + linkedList.length);
}

main();
