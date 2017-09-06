/* A Queue object for queue-like functionality over JavaScript arrays. */
let Queue = function () {
    this.items = [];
};
Queue.prototype.enqueue = function (obj) {
    this.items.push(obj);
};
Queue.prototype.dequeue = function () {
    return this.items.shift();
};
Queue.prototype.isEmpty = function () {
    return this.items.length === 0;
};

/**
 * Performs a breadth-first search on a graph
 * @param {array} graph - Graph, represented as adjacency lists.
 * @param {number} source - The index of the source vertex.
 * @return {array} Array of objects describing each vertex, like
 *     [{distance: _, predecessor: _ }]
 */
let bfs = function (graph, source) {
    let vertexInfo = [];
    // Index of each object -> vertex number, v
    for (let i = 0; i < graph.length; i++) {
        vertexInfo[i] = {
            // Initialise to null to track which vertices have been processed
            distance: null,
            predecessor: null
        };
    }

    // Source vertex has no predecessor
    vertexInfo[source].distance = 0;

    let queue = new Queue();
    queue.enqueue(source);

    while (!queue.isEmpty()) {
        let u = queue.dequeue();
        // Search through neighbours of u
        for (let i = 0; i < graph[u].length; i++) {
            let v = graph[u][i];
            // Process if not already processed
            if (vertexInfo[v].distance === null) {
                // Update info for u
                vertexInfo[v].distance = vertexInfo[u].distance + 1;
                vertexInfo[v].predecessor = u;
                // Add to queue to process its neighbours later
                queue.enqueue(v);
            }
        }
    }

    return vertexInfo;
};


// Testing ------------------
/**
 * Compares property value level equality of two objects
 * @param {object} a 
 * @param {object} b
 * @return {boolean}
 */
let isObjectEquivalent = function (a, b) {
    // Create arrays of property names
    let aProps = Object.getOwnPropertyNames(a);
    let bProps = Object.getOwnPropertyNames(b);
    // Check number of properties
    // Compare equality of each property value
    return aProps.length === bProps.length &&
        aProps.reduce((prev, curr, i) => a[aProps[i]] === b[aProps[i]], true)
}

// Adjacency lists representing graph
let adjList = [
    [1],
    [0, 4, 5],
    [3, 4, 5],
    [2, 6],
    [1, 2],
    [1, 2, 6],
    [3, 5],
    []
];

let vertexInfo = bfs(adjList, 3);
for (let i = 0; i < adjList.length; i++) {
    console.log("vertex " + i + ": distance = " + vertexInfo[i].distance + ", predecessor = " + vertexInfo[i].predecessor);
}

console.assert(true === isObjectEquivalent(vertexInfo[0], {
    distance: 4,
    predecessor: 1
}));
console.assert(true === isObjectEquivalent(vertexInfo[1], {
    distance: 3,
    predecessor: 4
}));
console.assert(true === isObjectEquivalent(vertexInfo[2], {
    distance: 1,
    predecessor: 3
}));
console.assert(true === isObjectEquivalent(vertexInfo[3], {
    distance: 0,
    predecessor: null
}));
console.assert(true === isObjectEquivalent(vertexInfo[4], {
    distance: 2,
    predecessor: 2
}));
console.assert(true === isObjectEquivalent(vertexInfo[5], {
    distance: 2,
    predecessor: 2
}));
console.assert(true === isObjectEquivalent(vertexInfo[6], {
    distance: 1,
    predecessor: 3
}));
console.assert(true === isObjectEquivalent(vertexInfo[7], {
    distance: null,
    predecessor: null
}));