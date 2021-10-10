
// @raunak kumar jaiswal
function mindistance(ans, visited) {
    var min_index = -1;
    var min_value = Number.MAX_VALUE;
    for (var i = 0; i < visited.length; i++) {
        if (visited[i] == 0 && ans[i] < min_value) {
            min_value = ans[i];
            min_index = i;
        }
    }
    return min_index;
}

function dijjj(visited, graph, ans, total) {
    for (var j = 0; j < total; j++) {
        var min_index = mindistance(ans, visited);
        if (min_index == -1) {
            return
        }
        visited[min_index] = 1;
        var dist = ans[min_index];
        for (var i = 0; i < graph[min_index].length; i++) {
            var ele = graph[min_index][i];
            var vrr = ele[0];
            var w = ele[1];
            if (visited[vrr] == 0 && dist + w < ans[vrr]) {
                ans[vrr] = dist + w;
            }
        }
    }
}

function make_graph(edge, graph) {
    edge.forEach(ede => {
        graph[ede[0]].push([ede[1], ede[2]])
        graph[ede[1]].push([ede[0], ede[2]])
    })
}

const dijkshtra = () => {
    var node = 6;
    var graph = [];
    for (var i = 0; i < node; i++) {
        graph[i] = [];
    }
    var edge = [[0, 1, 1], [0, 3, 7], [1, 3, 5], [0, 2, 3], [1, 2, 1], [1, 4, 3], [4, 5, 6], [5, 2, 2]];
    make_graph(edge, graph)
    var ans = new Array(node);
    var visited = new Array(node);
    for (var i = 0; i < node; i++) {
        ans[i] = Number.MAX_VALUE
        visited[i] = 0;
    }
    var sort_dist_from = 0;
    ans[sort_dist_from] = 0;
    dijjj(visited, graph, ans, node)
    console.log("distance from source node that is 0 by default")
    console.log("node      distance")
    for (var i = 0; i < ans.length; i++) {
        console.log(i + "             " + ans[i])
    }
}
dijkshtra()