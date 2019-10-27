#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <iostream>
#include <bitset>
#include <cassert>
#include <queue>
#include <random>
#include <stack>
#include <iomanip>

using namespace std;

typedef unsigned int uint;
typedef long long llong;
typedef unsigned long long ullong;
typedef long double ldouble;

typedef vector<llong> vecllong;
typedef vector<vecllong> vvecllong;

const llong MOD = 1e9 + 7;
const llong INF = 1e17;

#define FOR(i, n) for (llong i = 0; i < n; i++)
#define FORS(i, a, b) for (llong i = a; i < b; i++)
#define FORR(i, n) for (llong i = n; i > 0; i++)

llong dijkstra(llong start, llong end, vector<vector<pair<llong, llong>>> edge) {
    llong minCost[edge.size()];
    for (llong i = 0; i < edge.size(); i++) {
        minCost[i] = INF;
    }

    priority_queue<
        pair<llong, llong>,  // cost, index
        vector<pair<llong, llong>>,
        greater<pair<llong, llong>>
    > nodeHeap;

    nodeHeap.push(make_pair(0, start));

    while (!nodeHeap.empty()) {
        llong cost = nodeHeap.top().first;
        llong node = nodeHeap.top().second;
        nodeHeap.pop();

        if (minCost[node] <= cost) {
            continue;
        }

        minCost[node] = cost;

        for_each(edge[node].begin(), edge[node].end(), [&](pair<llong, llong> e){
            llong nextNode = e.first;
            llong newCost = cost + e.second;
            nodeHeap.push(make_pair(newCost, nextNode));
        });
    }

    return minCost[end];
}

int main(void) {
    llong N, M;
    cin >> N >> M;  // N頂点 M辺

    vector<vector<pair<llong, llong>>> edge(N*3);

    for (llong i = 0; i < M; i ++) {
        llong fromNode, toNode;
        llong cost = 1;
        cin >> fromNode >> toNode;
        fromNode--;
        toNode--;
        edge[fromNode*3].push_back(make_pair(toNode*3 + 1, cost));
        edge[fromNode*3 + 1].push_back(make_pair(toNode*3 + 2, cost));
        edge[fromNode*3 + 2].push_back(make_pair(toNode*3, cost));
    }

    llong start, end;
    cin >> start >> end;

    start--;
    end--;

    llong dist = dijkstra(start*3, end*3, edge);

    if (dist == INF) {
        cout << "-1" << endl;
    } else {
        cout << dist / 3 << endl;
    }

    return 0;
}

