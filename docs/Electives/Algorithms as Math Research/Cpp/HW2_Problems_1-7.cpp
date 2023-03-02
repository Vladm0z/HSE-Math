//problem A
/*
#include <iostream>
#include <map>

int main (){
    std::ios_base::sync_with_stdio(false);std::cin.tie(NULL);std::cout.tie(NULL);
    int n, m, out = 0;
    std::cin >> n >> m;
    std::map<int, int> a;

    int l, r;
    
    for(int i = 0; i < m; i++){
        std::cin >> l >> r;
        if(a.find(l) == a.end()){
            a[l] = 1;
        }else{
            a[l] += 1;
        }
        
        if(a.find(r+1) == a.end()){
            a[r+1] = -1;
        }else{
            a[r+1] -= 1;
        }
    }
    
    for(int i = 1; i < n+1; i++){
        if(a[i] != 0){
            out += a[i];
        }
        std::cout << out << " ";
    }
    std::cout << std::endl;
    return 0;
}
*/




//problem B
/*
void swap(int *a, int *b){
    int tmp = *a;
      *a = *b;
      *b = tmp;
}
  
void heapify(int arr[], int N, int i){
    int largest = i; // Initialize largest as root
    int l = 2 * i + 1; // left = 2*i + 1
    int r = 2 * i + 2; // right = 2*i + 2
  
    if (l < N && arr[l] > arr[largest])
        largest = l;
  
    if (r < N && arr[r] > arr[largest])
        largest = r;
  
    if (largest != i) {
        swap(&arr[i], &arr[largest]);
        heapify(arr, N, largest);
    }
}

void buildHeap(int arr[], int N){
    int startIdx = (N / 2) - 1;
    for (int i = startIdx; i >= 0; i--) {
        heapify(arr, N, i);
    }
}

void printHeap(int arr[], int N){
    cout << "Array representation of Heap is:\n";
  
    for (int i = 0; i < N; ++i)
        cout << arr[i] << " ";
    cout << "\n";
}

int main(){
    int arr[] = {1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17};
  
    int N = sizeof(arr) / sizeof(arr[0]);

    buildHeap(arr, N);
    printHeap(arr, N);
  
    return 0;
}
*/




//problem D
/*
#include <iostream>
#include <map>

int main (){
    std::ios_base::sync_with_stdio(false);std::cin.tie(NULL);std::cout.tie(NULL);
    int n;
    int64_t a, b, c = 0;
    int64_t out = 0;
    std::map<int64_t, int64_t> m;
    
    std::cin >> n;
    
    for(int i = 0; i < n; i++){
        std::cin >> a >> b;
        if(m.find(a) == m.end()){
            m[a] = a;}
        if(m.find(b) == m.end()){
            m[b] = b;}
        
        out = m[a];
        m[a] = m[b];
        m[b] = out;
        
        out = std::abs(m[a] - m[b]);
        std::cout << out << "\n";   
    }
    return 0;
}
*/



//problem E

#pragma GCC optimize("Ofast")
#pragma GCC optimization ("O3")
#pragma GCC optimization ("unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,fma,tune=native")


#include <iostream>
#include <cmath>

using namespace std;



int main(){
    std::ios_base::sync_with_stdio(false);std::cin.tie(NULL);std::cout.tie(NULL);
    int n, m, max_index;
    std::cin >> n >> m;
    int64_t votes[n];
    int mandates[n];
    std::fill(mandates, mandates + n, 0);
    float calc_table[n];
    float max_value;
    
    for(int i = 0; i < n; i++){
        std::cin >> votes[i];
        calc_table[i] = votes[i];
    }
    
    for(int i = 0; i < m; i++){
        max_value = -1.0f;
        for (int j = 0; j < n; j++){
            if(max_value < calc_table[j]){
                max_value = calc_table[j];
                max_index = j;
            }
        }
        mandates[max_index]++;
        calc_table[max_index] = (votes[max_index] * 1.0f)/(mandates[max_index] + 1.0f);
    }
    
    for(int i = 0; i < n; i++){
        std::cout << mandates[i] << " ";
    }
    std::cout << "\n";
    return 0;
}






//problem F
/*
#include <iostream>
#include <map>

int main() {
    std::ios_base::sync_with_stdio(false);std::cin.tie(NULL);std::cout.tie(NULL);

    int64_t t;
    std::cin >> t;

    while (t--) {
        int64_t n;
        std::cin >> n;

        std::map<int64_t, int64_t> mp;
        int64_t out = 0;

        for (int64_t i = 0; i < n; i++) {
            int64_t a;
            std::cin >> a;
            out += mp[a - i];
            mp[a - i]++;
        }
        std::cout << out << std::endl;
    }
    return 0;
}
*/


//problem G
/*
#include <iostream>

int main() 
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    int t, n, num;
    std::cin >> t;

    for (int i = 0; i < t; i++){
        std::cin >> n;
        int a[n];

        for (int j = 0; j < n; j++){
            std::cin >> num;
            a[j] = num;            
        }

        int l = 0;
        int al = 1;
        int r = n - 1;
        int ar = n;

        for (int j = 1; j < n + 1; j++){
            if (a[r] == al){
                al += 1;
                r -= 1;
            }
            else if (a[r] == ar){
                ar -= 1;
                r -= 1;
            }
            else if (a[l] == al){
                al += 1;
                l += 1;
            }
            else if (a[l] == ar){
                ar -= 1;
                l += 1;
            }
            else{
                j = n + 1;
            }
        }

        if (l > r){
            std::cout << -1 << "\n";
        }
        else{
            std::cout << l + 1 << " " << r + 1 << "\n";
        }
    }
    return 0;
}
*/