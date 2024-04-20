//problem A
/*
#include <iostream>
#include <vector>
#include <map>
using namespace std;
 
int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);
  int n;
  int x = 0;
  cin >> n;
  vector<int> a(n);
  vector<int> dp(n, 1);
  map<int, int> m;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    auto it = m.upper_bound(a[i]);
    if (it != m.begin()) {
      it--;
      dp[i] = it->second + 1;
    }
    m[a[i]] = dp[i];
    it = m.upper_bound(a[i]);
    while (it != m.end() && it->second <= dp[i]) {
      auto temp = it;
      it++;
      m.erase(temp);
    }
    x = max(dp[i], x);
    cout << x << endl;
  }
  return 0;
}
*/


//problem B
/*
#include <iostream>
#include <vector>
using namespace std;

const int INF = 1e9; // a large value to represent infinity

int main() {
  // read the number of vertices
  int n;
  cin >> n;

  // read the weight matrix
  vector<vector<int>> w(n, vector<int>(n));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> w[i][j];
      // replace zero weights with infinity, except on the diagonal
      if (i != j && w[i][j] == 0) {
        w[i][j] = INF;
      }
    }
  }

  // initialize the distance matrix with the weight matrix
  vector<vector<int>> d = w;

  // apply the Floyd-Warshall algorithm
  for (int k = 0; k < n; k++) { // for each intermediate vertex
    for (int i = 0; i < n; i++) { // for each source vertex
      for (int j = 0; j < n; j++) { // for each destination vertex
        // relax the distance using the intermediate vertex
        d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
      }
    }
  }

  // output the distance matrix
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cout << d[i][j] << " ";
    }
    cout << "\n";
  }

  return 0;
}
*/


//problem C
/*
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// A function to find the longest path in a DAG
int longest_path(vector<vector<int>>& adj, vector<int>& dp, int u) {
  // If the longest path from u is already computed, return it
  if (dp[u] != -1) return dp[u];

  // Initialize the longest path from u as 0
  int ans = 0;

  // Iterate over all the adjacent vertices of u
  for (int v : adj[u]) {
    // Recursively find the longest path from v and update the answer
    ans = max(ans, 1 + longest_path(adj, dp, v));
  }

  // Store and return the longest path from u
  return dp[u] = ans;
}

int main() {
  // Read the number of vertices and edges
  int n, m;
  cin >> n >> m;

  // Create an adjacency list to store the graph
  vector<vector<int>> adj(n + 1);

  // Read the edges and add them to the adjacency list
  for (int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    adj[u].push_back(v);
  }

  // Create a vector to store the longest path from each vertex
  vector<int> dp(n + 1, -1);

  // Initialize the answer as 0
  int ans = 0;

  // Iterate over all the vertices and update the answer
  for (int i = 1; i <= n; i++) {
    ans = max(ans, longest_path(adj, dp, i));
  }

  // Print the answer
  cout << ans << endl;

  return 0;
}
*/


//problem D
/*
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// A function to return the minimum of three integers
int min(int a, int b, int c) {
  return min(min(a, b), c);
}

// A function to compute the edit distance between two words
int edit_distance(string word1, string word2) {
  // Get the lengths of the words
  int m = word1.length();
  int n = word2.length();

  // Create a 2D array to store the subproblem solutions
  int dp[m + 1][n + 1];

  // Fill the first row and column with the base cases
  for (int i = 0; i <= m; i++) {
    dp[i][0] = i; // The cost of deleting i characters from word1
  }
  for (int j = 0; j <= n; j++) {
    dp[0][j] = j; // The cost of inserting j characters to word1
  }

  // Fill the rest of the array using the recurrence relation
  for (int i = 1; i <= m; i++) {
    for (int j = 1; j <= n; j++) {
      // If the characters match, there is no penalty
      if (word1[i - 1] == word2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1];
      }
      // Otherwise, choose the minimum of three options:
      // - Delete a character from word1
      // - Insert a character to word1
      // - Replace a character in word1
      else {
        dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1);
      }
    }
  }

  // Return the final answer
  return dp[m][n];
}

// A main function to test the code
int main() {
  // Read the input words from the standard input
  string word1, word2;
  cin >> word1 >> word2;

  // Compute and print the edit distance
  cout << edit_distance(word1, word2) << endl;

  return 0;
}
*/


//problem E
/*
#include <iostream>
using namespace std;

int main() {
  int m, n; // input dimensions
  cin >> m >> n;
  int dp[n+1]; // array to store number of ways
  dp[0] = 1; // base case
  for (int i = 1; i <= n; i++) {
    dp[i] = dp[i-1]; // add a vertical tile
    if (i-m >= 0) {
      dp[i] += dp[i-m]; // add m horizontal tiles
    }
  }
  cout << dp[n] << endl; // output the answer
  return 0;
}
*/


//problem F
/*
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<vector<int>> triangle(n);
  for (int i = 0; i < n; i++) {
    triangle[i].resize(i + 1);
    for (int j = 0; j <= i; j++) {
      cin >> triangle[i][j];
    }
  }
  for (int i = n - 2; i >= 0; i--) {
    for (int j = 0; j <= i; j++) {
      triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1]);
    }
  }
  cout << triangle[0][0] << endl;
  return 0;
}

*/


//problem G
/*
#include <iostream>
using namespace std;

// A function to count the number of ways to reach (n, m) from (1, 1)
// using a knight's moves
int countWays(int n, int m) {
  // Create a 2D array to store the results of subproblems
  int dp[n + 1][m + 1];

  // Base case: there is only one way to reach (1, 1)
  dp[1][1] = 1;

  // Fill the rest of the array using the recurrence relation
  // dp[i][j] = dp[i - 2][j - 1] + dp[i - 1][j - 2]
  // where (i, j) are valid coordinates on the chess board
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      // If the cell is not (1, 1), then calculate its value
      if (!(i == 1 && j == 1)) {
        // Initialize the cell value to zero
        dp[i][j] = 0;

        // If the cell can be reached from the left-up diagonal, then add its value
        if (i - 2 >= 1 && j - 1 >= 1) {
          dp[i][j] += dp[i - 2][j - 1];
        }

        // If the cell can be reached from the right-up diagonal, then add its value
        if (i - 1 >= 1 && j - 2 >= 1) {
          dp[i][j] += dp[i - 1][j - 2];
        }
      }
    }
  }

  // Return the final answer
  return dp[n][m];
}

int main() {
  // Read the input
  int n, m;
  cin >> n >> m;

  // Call the function and print the result
  cout << countWays(n, m) << endl;

  return 0;
}
*/


//problem H
/*
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
  int n;
  cin >> n;
  string road;
  cin >> road;
  vector<int> dp(n, -1);
  dp[0] = 0;
  for (int i = 0; i < n; i++) {
    if (road[i] == 'w') continue;
    if (road[i] == '"') dp[i]++;
    for (int j : {i+1, i+3, i+5}) {
      if (j < n && dp[j] < dp[i]) {
        dp[j] = dp[i];
      }
    }
  }
  cout << dp[n-1] << endl;
  return 0;
}
*/


//problem I
/*
#include <iostream>
#include <vector>

using namespace std;


int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);
    int n;
    cin >> n;
    vector <int> dp(n);
    for (int i = 0; i < n; ++i) {
        cin >> dp[i];
        int temp = dp[i];
        if (i > 0) {
            temp = max(temp, dp[i] + dp[i - 1]);
            if (i > 1) {
                temp = max(temp, dp[i] + dp[i - 2]);
            }
        }
        dp[i] = temp;
    }
    cout << dp[n - 1];
}
*/


//problem J
/*
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
int n;
const int dx[] = { 0,-1,1,0 };
const int dy[] = { 1,0,0,-1 };
vector<vector<int>> X;
vector<vector<int>> Y;
vector<vector<bool>> v;
const char dir[] = "URLD";
vector<vector<char>> ans;
 
inline bool boardValidation(int x, int y) {
    return 0 < x && x <= n && 0 < y && y <= n && !v[y][x];
}
 
void dfs(int x, int y) {
    v[y][x] = true;
    for (int i = 0; i < 4; ++i) {
        int nx = x + dx[i], ny = y + dy[i];
        if (boardValidation(nx, ny) && X[y][x] == X[ny][nx] && Y[y][x] == Y[ny][nx]) {
            ans[ny][nx] = dir[i];
            dfs(nx, ny);
        }
    }
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    cin >> n;
    X.resize(n + 1);
    Y.resize(n + 1);
    v.resize(n + 1);
    ans.resize(n + 1);
    for (int i = 1; i <= n; ++i) {
        X[i].resize(n + 1);
        Y[i].resize(n + 1);
        v[i].resize(n + 1);
        ans[i].resize(n + 1);
        for (int j = 1; j <= n; ++j) {
            cin >> Y[i][j] >> X[i][j];
        }
    }
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j) {
            if (v[i][j]) continue;
            if (X[i][j] == j && Y[i][j] == i) {
                ans[i][j] = 'X';
                dfs(j, i);
            }
            if (X[i][j] == -1) {
                bool b = true;
                for (int k = 0; k < 4; ++k) {
                    int x = j + dx[k], y = i + dy[k];
                    if (boardValidation(x, y) && X[y][x] == -1) {
                        ans[y][x] = dir[k];
                        ans[i][j] = dir[3 - k];
                        dfs(x, y);
                        dfs(j, i);
                        b = false;
                        break;
                    }
                }
                if (b) {
                    cout << "INVALID" << endl;
                    return 0;
                }
            }
        }
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j)
            if (!v[i][j]) {
                cout << "INVALID" << endl;
                return 0;
            }
    cout << "VALID" << endl;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) cout << ans[i][j];
        cout << '\n';
    }
    return 0;
}
*/


//problem K
/*
#include <iostream>
#include <string>
#include <set>
using namespace std;

const int MAXN = 1e5 + 5;

int prefix[MAXN];
int suffix[MAXN];

int max_coins(string ribbon) {
  int n = ribbon.size();
  set<char> types;

  prefix[0] = 0;
  for (int i = 0; i < n; i++) {
    types.insert(ribbon[i]);
    prefix[i+1] = prefix[i] + types.size();
    if (types.size() == 3) {
      types.clear();
    }
  }

  suffix[n] = 0;
  for (int i = n-1; i >= 0; i--) {
    types.insert(ribbon[i]);
    suffix[i] = suffix[i+1] + types.size();
    if (types.size() == 3) {
      types.clear();
    }
  }

  int max_c = 0;
  for (int i = 0; i <= n; i++) {
    max_c = max(max_c, prefix[i] + suffix[i]);
    types.clear();
  }

  return max_c;
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);
  int n;
  string ribbon;

  cin >> n;
  cin >> ribbon;

  cout << max_coins(ribbon) << endl;

  return 0;
}
*/


