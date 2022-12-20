%DATA
% planning horizon
int: T = 365;
% food ids: 1 to F
int: F = 77;
% nutrient ids: 1 to N
int: N = 9;
% allowed violation of nutrition target
float: delta = 0.1;
% nutrition target per day
array[1..N] of float: k;
% food nutrition per 1$ (1939)
array[1..F, 1..N] of float: s;
% VARIABLES
% dollars of food to be purchased
array[1..F] of var float: x;
% total bill
var float: cost = sum(f in 1..F) (x[f]);

% OBJECTIVE - MINIMIZE TOTAL COST
solve minimize cost;

% CONSTRAINTS
constraint
  forall(f in 1..F)(x[f] >= 0) /\
  forall(n in 1..N)(sum(f in 1..F)(s[f,n]*x[f]) <= T*(1+delta)*k[n]) /\
  forall(n in 1..N)(sum(f in 1..F)(s[f,n]*x[f]) >= T*(1-delta)*k[n]);
  
output[show(x), "\n",
       show(cost)]