//problem 1
/*
#include <iostream>
#include <vector>
#include <queue>

int main() {
    std::ios_base::sync_with_stdio(false);std::cin.tie(NULL);std::cout.tie(NULL);
    int n;
    std::cin >> n;
    std::vector<std::vector<int>> tree(n);
    for (int i = 1; i < n; i++) {
        int p;
        std::cin >> p;
        tree[p-1].push_back(i);
        tree[i].push_back(p-1);
    }

    std::queue<int> q;
    q.push(0);
    std::vector<int> dist(n, -1);
    dist[0] = 0;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : tree[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }

    int maxDist = 0;
    for (int d : dist) {
        maxDist = std::max(maxDist, d);
    }
    
    int maxNum = 0;
    int maxArr[n];
    for (int i = 1; i < n; i++) {
        if (dist[i] == maxDist) {
            maxArr[maxNum] = i+1;
            maxNum += 1;
        }
    }


    if (n == 1) {
        std::cout << 0 << "\n" << 1 << "\n" << 1 << "\n";
    } else {
        std::cout << maxDist << "\n";
        std::cout << maxNum << "\n";
        for (int i = 0; i < maxNum; i++) {
            std::cout << maxArr[i] << " ";
        }
    }
    std::cout << "\n";
}
*/



//problem 2
/*
#include <iostream>
#include <stack>
#include <vector>

int dfs(int u, std::vector<std::vector<int>>& tree,
        std::vector<char>& color,
        int& res,
        bool has_black_ancestor) {
    int white = (color[u] == 'w');
    for (int v : tree[u]) {
        int w = dfs(v, tree, color, res, has_black_ancestor || (color[u] == 'b'));
        if (color[u] == 'b' && !has_black_ancestor) {
            res += w;
        }
        white += w;
    }
    return white;
}

int main() {
    std::ios_base::sync_with_stdio(false);std::cin.tie(NULL);std::cout.tie(NULL);
    std::string s;
    std::cin >> s;
    
    int n = 0;
    for (char c : s) {
        if (c == '(') {
            n++;
        }
    }

    std::stack<int> stack;
    std::vector<std::vector<int>> tree(n);
    std::vector<char> color(n);
    
    int i = 0;
    for (char c : s) {
        if (c == '(') {
            if (!stack.empty()) {
                tree[stack.top()].push_back(i);
            }
            stack.push(i++);
        } else if (c == ')') {
            stack.pop();
        } else if (c != ',') {
            color[stack.top()] = c;
        }
    }

    int res = 0;
    dfs(0, tree, color, res, false);
    
    std::cout << res << "\n";
}
*/

//problem 3
/*
#include <iostream>
#include <string>
#include <stack>
#include <algorithm>
using namespace std;

string rotateString(string s) {
    stack<char> st;
    string result = "";
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ')') {
            string temp = "";
            while (!st.empty() && st.top() != '(') {
                temp += st.top();
                st.pop();
            }
            st.pop();
            if (i + 1 < s.length() && s[i + 1] == 'R') {
                i++;
            } else {
                reverse(temp.begin(), temp.end());
            }
            for (char c : temp) {
                st.push(c);
            }
        } else if (s[i] != ',') {
            st.push(s[i]);
        }
    }
    while (!st.empty()) {
        result += st.top();
        st.pop();
    }
    reverse(result.begin(), result.end());
    return result;
}

int main() {
    string input;
    getline(cin, input);
    cout << rotateString(input) << endl;
    return 0;
}
*/



//problem 4
/*
#include <iostream>
#include <queue>

int main() {
    std::ios_base::sync_with_stdio(false);std::cin.tie(NULL);std::cout.tie(NULL);
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
    int n;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        std::cin >> x;
        minHeap.push(x);
    }

    int res = 0;
    while (minHeap.size() > 1) {
        int a = minHeap.top();
        minHeap.pop();
        int b = minHeap.top();
        minHeap.pop();
        res += a + b;
        minHeap.push(a + b);
    }
    std::cout << res << "\n";
}
*/