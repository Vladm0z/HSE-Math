#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

//problem 1
/*
int main (){
    int n, a;
    cin >> n;
    long long int ma=0, a3=0, a5=0, a15=0;
    int b3, b5;
    for(int i = 0; i < n; i++){
        cin >> a;
        b3 = a%3;
        b5 = a%5;
        if(b3 == 0 && b5 == 0 && a > a15){
            if(a15 > ma){ma = a15;}
            a15 = a;
        }else if(b3 == 0 && b5 != 0 && a > a3){
            if(a3 > ma){ma = a3;}
            a3 = a;
        }else if(b3 != 0 && b5 == 0 && a > a5){
            if(a5 > ma){ma = a5;}
            a5 = a;
        }else if(a > ma){ma = a;}
    }
    
    long long int p1, p2;
    p2 = a3 * a5;
    p1 = max(ma, a3);
    p1 = max(p1, a5);
    p1 = a15 * p1;
    p1 = max(p1, p2);
    cout << p1 << "\n";
}
*/


//problem 2
/*
int main(){
    std::ios::sync_with_stdio(false); std::cin.tie(0);
    int n;
    float l=1001, r=-1001, y=0, cx, cy;
    
    cin >> n;

    for(int i = 0; i < n; i++){
        cin >> cx;
        cin >> cy;
        
        if(cy == 0){
            if(l == 1001){
                r = cx;
                l = cx;
            }else if(cx > r){
                r = cx;
            }else if(cx < l){
                l = cx;
            }
        }else if(abs(cy) > y){
            y = abs(cy);
        }
    }
    
    if(l == 1001){
        cout << 0 << "\n";
    }else if(r == -1001){
        cout << 0 << "\n";
    }else if(y == 0){
        cout << 0 << "\n";
    }else{
        float a = ((r-l)*y)/2;
        cout << a << "\n";
    }
}
*/

/*
//problem 3
int main (){
	float n;
	cin >> n;
    float a, p = ceil(n/2), f = n, c = 1;
    
    for(int i = 0; i < n; i++){
        cout << p << endl;
        cout.flush();
        cin >> a;
        
        if(a == 2){
            c = p;
            p = ceil((f+c)/2);
        }else if(a == 0){
            f = p;
            p = floor((f+c)/2);
        }else if(a == 1){
            break;
        }
    }
}
*/

//problem 4
/*
#include <iostream>
#include <algorithm>
#include <vector>
 
using namespace std;
     
int main (){
    int n, k, b, pos = -1;
    cin >> n >> k;
    vector<int> arr;
    for(int i = 0; i < n; i++){
        cin >> b;
        if(i < k+2){
            arr.push_back(b);
            sort(arr.begin(), arr.end());
        }else{
            for(int i = k; i >= 0; i--){
                if(arr[i] > b){pos = i;}}
            if(pos < k && pos != -1){
                for(int i = k; i > pos; i--){
                    arr[i] = arr[i-1];}
                arr[pos] = b;
            }else if(pos == k){arr[k] = b;} 
            pos = -1;
        }
        
        if(i < k){cout << arr[i] << "\n";
        }else{cout << arr[k-1] << "\n";}
        cout.flush();
    }
}
*/


//problem 5
/*
int main (){
    std::ios::sync_with_stdio(false); std::cin.tie(0);
	string s, t;
	cin >> s;
	cin >> t;
	int k = s.length();
	
    for(int i = 0; i < t.length(); i++){
        if(k == -1){break;}
        k = s.substr(0,k).rfind(t[t.length()-1-i]);
    }

    for(int i = 0; i < k+1; i++){
        cout << "yes" << "\n";
    }
    for(int i = k+1; i < s.length(); i++){
        cout << "no" << "\n";
    }
}
*/

//problem 6
/*
int main (){
    std::ios::sync_with_stdio(false); std::cin.tie(0);
	int na, nb, k, m, a[100001], b[100001];
    cin >> na >> nb >> k >> m;
    for(int i = 0; i < na; i++){cin >> a[i];}
    for(int i = 0; i < nb; i++){cin >> b[i];}
    if(a[k - 1] < b[nb - m]){cout << "YES" << "\n";
    }else{cout << "NO" << "\n";}
    return 0;
}
*/


//problem 7
#include <iostream>
#include <algorithm>
#include <vector>
 
using namespace std;

int main (){
    std::ios::sync_with_stdio(false); std::cin.tie(0);
    int64_t n, x, y, out = 0;
    vector<int> arrX;
    vector<int> arrY;

    cin >> n;

    for(int i = 0; i < n; i++){
        cin >> x >> y;
        arrX.push_back(x);
        arrY.push_back(y);}

    sort(arrX.begin(), arrX.end());
    sort(arrY.begin(), arrY.end());

    for(int i = 0; i < n/2; i++){
        out += (arrX[n-i-1] - arrX[i] + arrY[n-i-1] - arrY[i]);}

    cout << out << endl;
}


//problem 8
/*
int main (){
	int n, m, a=1, b=1, res;
    long long out = 0;
	string ans;
	
	cin >> n >> m;
	
    for(int i = 0; i < (n+m); i++){
        cout << "? " << a << " " << b << endl;
        cout.flush();
        cin >> ans;
        res = ans.compare("YES");
        if(res == 0){
            if(a < n){
                a += 1;
                out += (m-b+1);
            }else{out += (m-b+1); break;}
        }else if(b < m){
            b += 1;
        }else{break;}
    }
    cout << "! " << out << endl;
}
*/
