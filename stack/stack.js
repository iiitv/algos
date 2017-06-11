class Stack {
	constructor (size = 0) {
		this._array = [];
		this._size = size;
	}

	push (argument) {
		if (this._size > 0 && this._array.length === this._size) {
			throw new Error('Unable to push to full stack');
		}
		this._array.push(argument);
	}

	pop () {
		if (this._array.length === 0) {
			throw new Error('Unable to pop from empty stack');
		}
		return this._array.pop();
	}
}

function main () {
	let st = new Stack();
	st.push('Hello World!');
	st.push(1223);
	st.push('last one');
	console.log(st.pop());
	console.log(st.pop());
	console.log(st.pop());
	try {
		console.log(st.pop());
	} catch (error) {
		console.log('Error: ' + error.message);
	}
}

main();
