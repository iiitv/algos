function minKey (key, visited) {
	let min = Number.MAX_VALUE;
	let minIdx = -1;
	let length = key.length;

	for (let i = 0; i < length; i++) {
		if (!visited[i] && key[i] < min) {
			min = key[i];
			minIdx = i;
		}
	}

	return minIdx;
}

function generate (graph) {
	/*
	* Get the parent nodes in the MST
	* :param graph: array which represents the graph
	* :return: returns array of parent nodes
	*/
	let length = graph.length;

	// stores the parent of each vertex
	let parent = [];
	// key value of each vertex
	let key = [];
	// flag for included in the MST
	let mstSet = [];

	// initialize arguments
	for (let i = 0; i < length; i++) {
		mstSet[i] = false;
		key[i] = Number.MAX_VALUE;
	}

	// starting from the first vertex
	// the first vertex is the root, so it doesn't have any parent
	key[0] = 0;
	parent[0] = -1;

	for (let i = 0; i < length - 1; i++) {
		// minimum key from given vertices
		let u = minKey(key, mstSet);
		mstSet[u] = true;

		// updating the neighbours key
		for (let j = 0; j < length; j++) {
			if (graph[u][j] !== 0 && !mstSet[j] && graph[u][j] < key[j]) {
				parent[j] = u;
				key[j] = graph[u][j];
			}
		}
	}

	return parent;
}

function main () {
	// given graph
	let graph = [
		[0, 2, 0, 6, 0],
		[2, 0, 3, 8, 5],
		[0, 3, 0, 0, 7],
		[6, 8, 0, 0, 9],
		[0, 5, 7, 9, 0]
	];

	// get the parent nodes of all the vertices
	let parent = generate(graph);
	let length = graph.length;

	// print the MST
	console.log('Edge : Weight');
	for (let i = 1; i < length; i++) {
		console.log(parent[i] + ' - ' + i + ' : ' + graph[i][parent[i]]);
	}
}

main();
