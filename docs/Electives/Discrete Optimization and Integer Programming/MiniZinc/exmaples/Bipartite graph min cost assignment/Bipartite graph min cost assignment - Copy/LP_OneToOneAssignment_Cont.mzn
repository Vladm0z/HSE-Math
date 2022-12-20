%TASK ASSIGNMENT MINIMAL COST [0,1] CONT MODEL  

% DATA
% num workers
int: w;
% num tasks (we know that n = w!)
int: n;
% cost function matrix
array[1..w,1..n] of int: c;

% VARIABLES
% if worker j is assigned on task i
array[1..w,1..n] of var 0.0..1.0: x;

% OBJECTIVE 
% minimize total cost
solve minimize sum(i in 1..w, j in 1..n)(c[i,j]*x[i,j]);

%CONSTRAINTS
% all workers are assigned on exactly one task
constraint forall (i in 1..w) (
  sum(j in 1..n) (x[i,j]) = 1
);
% all tasks are assigned to exactly one worker
constraint forall (j in 1..n) (
  sum(i in 1..w) (x[i,j]) = 1
);

% OUTPUT 
output ["Total cost = \( sum(i in 1..w, j in 1..n)(c[i,j]*x[i,j]))\n"];
