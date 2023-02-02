#include <iostream>
#include <algorithm>

//max
/*
int main (){
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    int n, max1;
    std::cin >> n >> max1;
    for(int i = 0; i < n-1; ++i){
        int c;
        std::cin >> c;
        max1 = std::max(c, max1);
    }
    std::cout << max1 << "\n" << std::endl;
    return 0;
}
*/

//max product

using namespace std;

int main (){
    std::ios::sync_with_stdio(false); std::cin.tie(0);
    int n, a, b, m1, m2;
    std::cin >> n >> a >> b;

    m1 = max(a,b);
    m2 = min(a,b);
    for(int i = 2; i < n; ++i){
        int c;
        cin >> c;
        if(c > m1){
            m2 = m1;
            m1 = c;
        }else{m2 = max(m2, c);}
    }
    std::cout << (long long) m1 * (long long) m2 << "\n"; //<< std::endl
    return 0;
}


//two num product (multiple times)
/*
using namespace std;

int main (){
    int n, a, b;
    cin >> n;
    for(int i = 0; i < n; ++i){
        cin >> a;
        cin >> b;
        cout << a+b << endl;
        cout.flush();
    }
    return 0;
}
*/

/*
using namespace std;

int main (int argc, char const *argv[]){
    int n, prev, cur, len=1, max_len=1;
    cin >> n >> prev;
    cout << max_len << "\n";
    for(size_t i = 1; i < n; ++i){
        cin >> cur;
        if(cur >= prev){ ++len;}
        else{len = 1;}
        max_len = max(len, max_len);
        cout << max_len << "\n";
        prev = cur;
    }
    return 0;
}
*/