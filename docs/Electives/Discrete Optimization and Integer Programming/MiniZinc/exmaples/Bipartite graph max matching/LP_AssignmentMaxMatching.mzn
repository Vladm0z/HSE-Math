%TASK ASSIGNMENT MAX MATCHING [0,1] CONT MODEL 

% DATA
% num workers
int: w;
% num tasks 
int: n;
% adjacency matrix
array[1..w,1..n] of int: e;

% VARIABLES
% if worker j can be assigned on task i
array[1..w,1..n] of var 0.0..1.0: x;

% OBJECTIVE 
% maximize number of tasks to be processed
solve maximize sum(i in 1..w, j in 1..n)(x[i,j]);

%CONSTRAINTS
% all workers can be assigned on not more than one task
constraint forall (i in 1..w) (
  sum(j in 1..n) (x[i,j]) <= 1
);
% all tasks can be processed by not more than one worker
constraint forall (j in 1..n) (
  sum(i in 1..w) (x[i,j]) <= 1
);
% adjacency constraint
constraint forall (i in 1..w, j in 1..n) (
  x[i,j] <= e[i,j]
);

