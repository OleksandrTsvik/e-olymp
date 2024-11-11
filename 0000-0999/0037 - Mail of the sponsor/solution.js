const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const lines = [];

rl.on('line', (line) => lines.push(line)).on('close', () => {
    const [n, s, k] = lineToNumbers(lines[0]);
    const linksBetweenDepartments = lines.slice(1, k + 1).map((line) => lineToNumbers(line).slice(0, 2));

    solve(n, s, linksBetweenDepartments);
});

function lineToNumbers(line) {
    return line?.split(/\s+/).map((number) => +number) ?? [];
}

function solve(departmentCount, sponsorDepartmentNumber, linksBetweenDepartments) {
    const graph = Array(departmentCount)
        .fill()
        .map(() => new Set());

    for (const [a, b] of linksBetweenDepartments) {
        const rowIndex = a - 1;
        const columnIndex = b - 1;

        graph[rowIndex].add(columnIndex);
        graph[columnIndex].add(rowIndex);
    }

    const visitedVertices = Array(departmentCount).fill(false);
    let minNewConnectionCount = 0;

    dfs(graph, sponsorDepartmentNumber - 1, visitedVertices);

    for (let i = 0; i < visitedVertices.length; i++) {
        if (visitedVertices[i]) continue;

        minNewConnectionCount++;
        dfs(graph, i, visitedVertices);
    }

    console.log(minNewConnectionCount);
}

function dfs(graph, startVertex, visited) {
    if (visited[startVertex]) {
        return;
    }

    visited[startVertex] = true;

    for (const vertex of graph[startVertex]) {
        if (visited[vertex]) continue;

        dfs(graph, vertex, visited);
    }
}
