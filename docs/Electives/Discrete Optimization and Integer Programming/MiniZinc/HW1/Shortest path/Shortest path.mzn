%DATA
% vertice ids 1 to N
int: N = 9;
% vertex a
%case 1
int: a = 1;
%case 2
%int: a = 2;
%case 3
%int: a = 4;

% vertex b
%case 1
int: b = 9;
%case 2
%int: b = 8;
%case 3
%int: b = 2;

%answer 1: 42
%answer 2: 37
%answer 3: 29



% edge distances matrix 
array[1..N, 1..N] of int: l = 
[|0, 8, 12, -1, -1, -1, -1, -1, -1|
 -1, 0, 13, 25, 9, -1, -1, -1, -1|
 -1, -1, 0, 14, -1, -1, 21, -1, -1|
 -1, -1, -1, 0, 20, 8, 12, 12, 16|
 -1, 9, -1, -1, 0, 19, -1, -1, -1|
 -1, -1, -1, -1, -1, 0, -1, 11, -1|
 -1, -1, -1, -1, -1, -1, 0, -1, 11|
 -1, -1, -1, -1, -1, -1, -1, 0, 9|
 -1, -1, -1, -1, -1, -1, -1, -1, 0|];
 
array[1..N,1..N] of var 0..1: x;
array[1..N] of var 0..1: c;
array[1..N] of var 0..1: d;
var int: answer = sum(i in 1..N, k in 1..N) (l[i,k] * x[i,k]);

%OBJECTIVE
solve minimize answer;

%CONSTRAINTS
constraint forall(i in 1..N, k in 1..N where l[i,k]<=0)(x[i,k]=0) /\
           c[a] = 1 /\
           forall(i in 1..N where i != a) (c[i] = 0) /\
           d[b] = 1 /\
           forall(i in 1..N where i != b) (d[i] = 0) /\
           forall(i in 1..N) (
               sum(k in 1..N where l[k,i] > 0) (x[k,i]) + c[i]  
               =
               sum(k in 1..N where l[i,k] > 0) (x[i,k]) + d[i]);
output[show(answer)];

