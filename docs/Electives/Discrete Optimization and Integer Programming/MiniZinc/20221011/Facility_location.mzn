%UNCAPACITATED FACILITY LOCATION
%DATA
% number of facilites
int: n;
% number of customers
int: m;
% facility opening cost
array[1..n] of int : c;
% customer serving cost 
array[1..n, 1..m] of int : d;
%VARIABLES
% if facility is open
array[1..n] of var 0..1: x;
% facility serves customer
array[1..n, 1..m] of var 0..1: y;
%OBJECTIVE
solve minimize sum(i in 1..n) (x[i]*c[i]) + sum(i in 1..n, j in 1..m) (d[i, j]*y[i,j]);
%CONSTRAINT
% all customers are serviced
constraint forall(j in 1..m) (
  sum(i in 1..n) (y[i,j]) > 0
);
% facility is open if it serves customer 
constraint forall(i in 1..n, j in 1..m) (
  x[i] >= y[i,j]
);

% OUTPUT 
output ["Total value = \( sum(i in 1..n) (x[i]*c[i]) + sum(i in 1..n, j in 1..m) (d[i, j]*y[i,j]))\n"];