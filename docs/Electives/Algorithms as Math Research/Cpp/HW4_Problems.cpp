//problem A
/*
#include <iostream>
using namespace std;

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    int n, m;
    cin >> n >> m;

    int *nums = new int[n];
    for (int i = 0; i < n; i++) {
        nums[i] = i + 1;
    }

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;

        int len = b - a + 1;
        int *temp = new int[len];
        for (int j = 0; j < len; j++) {
            temp[j] = nums[a + j - 1];
        }

        for (int j = a - 2; j >= 0; j--) {
            nums[j + len] = nums[j];
        }

        for (int j = 0; j < len; j++) {
            nums[j] = temp[j];
        }
        delete[] temp;
    }

    for (int i = 0; i < n; i++) {
        cout << nums[i] << " ";
    }
    cout << endl;

    return 0;
}
*/


//problem B
/*
#include <iostream>
#include <deque>
using namespace std;

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    int n, p;
    cin >> n >> p;

    deque<int> nums;
    for (int i = 1; i <= n; i++) {
        nums.push_back(i);
    }

    int i = 0;
    while (!nums.empty()) {
        i = (i + p - 1) % nums.size();
        cout << nums[i] << " ";
        nums.erase(nums.begin() + i);
    }

    cout << endl;

    return 0;
}
*/

//problem C
/*
#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    vector<int64_t> prefix_sum(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        prefix_sum[i] = prefix_sum[i - 1] + a[i - 1];
    }

    int m;
    cin >> m;

    for (int i = 0; i < m; i++) {
        int l, r;
        cin >> l >> r;

        int64_t sum = prefix_sum[r] - prefix_sum[l - 1];
        cout << sum << endl;
    }

    return 0;
}
*/

//problem D
/*
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    while (k--) {
        char c;
        int l, r, x;
        cin >> c >> l >> r;
        if (c == 'A') {
            cin >> x;
            for (int i = l - 1; i < r; i++) {
                a[i] = x;
            }
        } else {
            int sum = 0;
            for (int i = l - 1; i < r; i++) {
                sum += a[i];
            }
            cout << sum << endl;
        }
    }
    return 0;
}
*/

//problem E
/*
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int k;
    cin >> k;
    vector<int> a;
    while (k--) {
        char c;
        cin >> c;
        if (c == '+') {
            int i, x;
            cin >> i >> x;
            if (i == 0) {
                a.insert(a.begin(), x);
            } else {
                a.insert(a.begin() + i, x);
            }
        } else {
            int l, r;
            cin >> l >> r;
            int min_val = INT_MAX;
            for (int i = l; i <= r; i++) {
                min_val = min(min_val, a[i - 1]);
            }
            cout << min_val << endl;
        }
    }
    return 0;
}
*/

//problem F TODO
/*
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<long long> heights(n, 0);
    while (m--) {
        string cmd;
        cin >> cmd;
        if (cmd == "build") {
            int l, r, a;
            cin >> l >> r >> a;
            heights[l - 1] += a;
            if (r < n) {
                heights[r] -= a;
            }
        } else {
            int l, r;
            cin >> l >> r;
            long long max_height = 0;
            for (int i = l - 1; i < r; i++) {
                max_height = max(max_height, heights[i]);
            }
            cout << max_height << endl;
        }
    }
    return 0;
}
*/

//problem G
/*
#include<iostream>
#include<queue>

using namespace std;

struct node {
    int u, v;
    bool operator<(const node a) const {
        return v<a.v;
    }
};

priority_queue<node> q;
int ans[200001];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m;
    cin >> n >> m;
    n += m;
    int64_t sm = 0;

    for (int i = 1; i <= n; i++) {
        int u;
        cin >> u;
        if (u > 0) {
            ans[i] = -1;
            sm += u;
            continue;
        }
        u = -u;
        node p;
        if (u <= sm) {
            ans[i] = 1;
            sm -= u;
        }
        else if (!q.empty() && u <= sm + (p=q.top()).v && u < p.v) {
            sm = sm+p.v-u;
            ans[i] = 1;
            ans[p.u] = 0;
            q.pop();
        }
        else continue;
        q.push((node) {i, u});
    }

    for (int i = 1; i <= n; i++) {
        if (ans[i] == -1) {
            cout << "resupplied\n";
        }
        else if (ans[i] == 0) {
            cout << "declined\n";
        }
        else {
            cout << "approved\n";
        }
    }
    return 0;
}
*/

//problem H
/*
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

const int N = 500005;
int fa[N], c[N];

int find(int x) {
    if (x == fa[x])
        return x;
    return fa[x] = find(fa[x]);
}

void join(int x, int y) {
    int fx = find(x), fy = find(y);
    if (fx != fy)
        fa[fx] = fy;
}

int main() {

    int n, m;
    cin >> n >> m;

    for (int i = 1; i <= n; i++) {
        fa[i] = i;
    }

    int k, x, y;
    while (m--) {
        cin >> k;
        if (k)
            cin >> x;
        for (int i = 1; i < k; i++) {
            cin >> y;
            join(y, x);
        }
    }

    for (int i = 1; i <= n; i++) {
        x = find(i);
        c[x]++;
    }

    for (int i = 1; i < n; i++) {
        x = find(i);
        cout << c[x] << " ";
    }

    x = find(n);
    cout << c[x] << endl;

    return 0;
}
*/

//problem I
/*
#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

int vis[100001];
vector<int> Vec[100001];
int64_t a1, a2;

void dfs(int x, int step) {
    for (int i = 0; i < Vec[x].size(); i++) {
        int neighbor = Vec[x][i];
        if (!vis[neighbor]) {
            vis[neighbor] = 1;
            if (step & 1)
                a1++;
            else
                a2++;
            dfs(neighbor, step + 1);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    a1 = 1;
    a2 = 0;
    for (int i = 0; i < n - 1; i++) {
        int x, y;
        cin >> x >> y;
        Vec[x].push_back(y);
        Vec[y].push_back(x);
    }

    vis[1] = 1;
    dfs(1, 0);

    cout << a1 * a2 - (n - 1) << endl;

    return 0;
}
*/

//problem J
/*
#include <iostream>
using namespace std;

int n, a[2001], out, k;

void dfs(int u){
    k++;
    if (a[u] == -1)
        return;
    dfs(a[u]);
}

void solve(){
    out = -1;
    for (int i = 1; i <= n; i++){
        k = 0;
        dfs(i);
        out = max(out, k);
    }
    cout << out << endl;
}

int main(){
    cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

    while (cin >> n){
        for (int i = 1; i <= n; i++)
            cin >> a[i];
        solve();
    }
    return 0;
}
*/

//problem K
/*
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int d[101], n, m;
vector<int> adj[101];

int topsort(){
    queue<int> q;
    int i, x = 1, cnt = 0;
    while (x){
        x = 0;
        for (i = 1; i <= n; i++){
            if (d[i] == 1){
                q.push(i);
                x = 1;
            }
        }
        while (!q.empty()){
            int j = q.front();
            q.pop();
            d[j]--;
            for (i = 0; i < adj[j].size(); i++){
                d[adj[j][i]]--;
            }
        }
        if (x){
            cnt++;
        }
    }
    return cnt;
}

int main(){
    ios::sync_with_stdio(false);
    int a, b, i;
    cin >> n >> m;
    for (i = 1; i <= m; i++){
        cin >> a >> b;
        d[a]++;
        d[b]++;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    cout << topsort() << endl;
    return 0;
}
*/

//problem L
/*
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

const int MAXN = 1000;

int n; // number of vertices
int adj[MAXN + 1][MAXN + 1]; // adjacency matrix
vector<int> rev_adj[MAXN + 1]; // reversed adjacency list
bool visited[MAXN + 1];
stack<int> st;

void dfs1(int u) {
    visited[u] = true;
    for (int v = 1; v <= n; v++) {
        if (adj[u][v] && !visited[v]) {
            dfs1(v);
        }
    }
    st.push(u);
}

void dfs2(int u) {
    visited[u] = true;
    for (int v : rev_adj[u]) {
        if (!visited[v]) {
            dfs2(v);
        }
    }
}

int main() {
    // input phase
    cin >> n;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> adj[i][j];
            if (adj[i][j]) {
                rev_adj[j].push_back(i);
            }
        }
    }

    // Tarjan's algorithm for finding SCCs
    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            dfs1(i);
        }
    }
    for (int i = 1; i <= n; i++) {
        visited[i] = false;
    }
    int num_sccs = 0;
    while (!st.empty()) {
        int u = st.top();
        st.pop();
        if (!visited[u]) {
            dfs2(u);
            num_sccs++;
        }
    }
    cout << num_sccs << endl;

    return 0;
}
*/

//problem M
/*
#include <iostream>
#include <vector>
#include <tuple>
#include <queue>
#include <cstdint>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int num_cities, num_roads, num_train_routes, u, v, x;
    cin >> num_cities >> num_roads >> num_train_routes;
    vector<vector<pair<int, int64_t>>> graph(num_cities);

    for (int i = 0; i < num_roads; i++) {
        cin >> u >> v >> x;
        u--; v--;
        graph[u].emplace_back(v, x);
        graph[v].emplace_back(u, x);
    }

    vector<int64_t> dist(num_cities, 1e14);
    vector<bool> has_route(num_cities);
    priority_queue<tuple<int64_t, bool, int>> pq;

    dist[0] = 0;
    pq.push(make_tuple(0LL, true, 0));
    for (int i = 0; i < num_train_routes; i++) {
        cin >> u >> x;
        u--;
        if (x < dist[u]) {
            pq.push(make_tuple(-x, false, u));
            dist[u] = x;
            has_route[u] = true;
        }
    }

    bool no_route;
    int64_t distance, weight;
    while (!pq.empty()) {
        tie(distance, no_route, u) = pq.top(); pq.pop();
        distance = -distance;
        if (distance > dist[u]) continue;
        for (auto& edge : graph[u]) {
            tie(v, weight) = edge;
            int64_t cost = distance + weight;
            if (cost < dist[v] || (cost == dist[v] && has_route[v])) {
                dist[v] = cost;
                pq.push(make_tuple(-cost, true, v));
                has_route[v] = false;
            }
        }
    }
    int num_to_remove = count(has_route.begin(), has_route.end(), true);
    cout << num_train_routes - num_to_remove << endl;
}
*/

//problem N
/*
#include <iostream>
#include <algorithm>
#include <climits>

const int MAXN = 100;
const int MAXW = 1000;
const int INF = INT_MAX;

using namespace std;

int n;
int w[MAXN][MAXN];
int d[MAXN][MAXN];
int maxd[MAXN];

void floyd() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            d[i][j] = w[i][j];
        }
        maxd[i] = d[i][i];
    }
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (d[i][k] != INF && d[k][j] != INF) {
                    d[i][j] = std::min(d[i][j], d[i][k] + d[k][j]);
                }
            }
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (d[i][j] != INF && d[i][j] > maxd[i]) {
                maxd[i] = d[i][j];
            }
        }
    }
}

int diameter() {
    int diam = 0;
    for (int i = 0; i < n; i++) {
        diam = std::max(diam, maxd[i]);
    }
    return diam;
}

int radius() {
    int rad = INF;
    for (int i = 0; i < n; i++) {
        rad = std::min(rad, maxd[i]);
    }
    return rad;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            std::cin >> w[i][j];
            if (w[i][j] == -1) {
                w[i][j] = INF;
            }
        }
    }
    floyd();
    std::cout << diameter() << " " << radius() << std::endl;
    return 0;
}
*/

//problem O
/*

*/

//problem P
/*
#include <iostream>
#include <vector>
using namespace std;

const int MAXN = 1e5;

vector<int> adj[MAXN+1];
int parent[MAXN+1];
int height[MAXN+1];
int entry[MAXN+1], exits[MAXN+1];
int time_;

void dfs(int u, int h) {
    height[u] = h;
    entry[u] = ++time_;
    for (int v : adj[u]) {
        dfs(v, h+1);
    }
    exits[u] = time_;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int n, m;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> parent[i];
        if (parent[i] > 0) {
            adj[parent[i]].push_back(i);
        }
    }

    dfs(1, 0);

    cin >> m;
    for (int k = 0; k < m; k++) {
        int a, b;
        cin >> a >> b;
        if (entry[a] <= entry[b] && exits[b] <= exits[a]) {
            cout << 1 << '\n';
        } else {
            cout << 0 << '\n';
        }
    }
    return 0;
}
*/

//problem Q
/*
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;

const int MAXN = 5005;

int n, x[MAXN], y[MAXN], parent[MAXN], rank[MAXN];

struct Edge {
    int u, v;
    double w;
    bool operator<(const Edge& e) const {
        return w < e.w;
    }
};

double dist(int i, int j) {
    return sqrt((x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]));
}

int find(int u) {
    if (parent[u] == u) return u;
    return parent[u] = find(parent[u]);
}

void merge(int u, int v) {
    u = find(u), v = find(v);
    if (::rank[u] > ::rank[v]) swap(u, v);
    parent[u] = v;
    ::rank[v] += ::rank[u];
}

double kruskal(const vector<vector<pair<int,double>>>& adj_list) {
    vector<Edge> edges;
    for (int i = 1; i <= n; ++i) {
        parent[i] = i;
        ::rank[i] = 1;
        for (const auto& p : adj_list[i]) {
            edges.push_back({i, p.first, p.second});
        }
    }
    sort(edges.begin(), edges.end());
    double cost = 0;
    for (const Edge& e : edges) {
        if (find(e.u) != find(e.v)) {
            cost += e.w;
            merge(e.u, e.v);
        }
    }
    return cost;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    vector<vector<pair<int,double>>> adj_list(n+1);
    for (int i = 1; i <= n; ++i) {
        cin >> x[i] >> y[i];
        for (int j = 1; j < i; ++j) {
            double d = dist(i, j);
            adj_list[i].push_back({j, d});
            adj_list[j].push_back({i, d});
        }
    }
    double cost = kruskal(adj_list);
    cout << fixed << setprecision(6) << cost << "\n";
    return 0;
}
*/