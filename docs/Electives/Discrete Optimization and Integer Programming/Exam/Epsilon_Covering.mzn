% Epsilon Covering Problem Statement

% As an input we have the following data
% -- An edge-weighted undirected graph G with the set of vertices V(G) and the set of edges E(G). The weights of the edges are positive integers. These weights can be thought of as lengths of edges.
% -- A constant $\epsilon$ which is called covering radius. This constant is also positive integer.

% The problem is to find a subset S of the set of vertices V(G) called $\epsilon$-covering of the graph G which satisfies the following conditions
% -- every node of the graph G is within distance $\epsilon$ of at least one point in S;
% -- the number of nodes in S is as minimal as possible.

% Some remarks:
% -- by definition the distance between nodes of the graph is the length of the shortest path between these nodes;
% -- note that the lengths between arbitrary nodes are not given as an input;
% -- in general, the $\epsilon$-covering set is not unique.

% We have prepared 5 graphs which can be used for testing your solution. We recommend to use these graphs with the different constants eps.

%DATA

% N = number of nodes of graph
% Nodes are enumerated from 1 to N
int: N;

% edge lengthes matrix (all distances are integers)
% length[i,j] = 0 if i == j
% length[i,j] = -1 if nodes i and j are not connected by an edge
array[1..N, 1..N] of int: length;

% eps = covering radius (integer)
int: eps;

%VARIABLES

%OBJECTIVE

%CONSTRAINTS