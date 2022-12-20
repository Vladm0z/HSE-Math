 set of int: Colors = 0..2;

% main problm
set of int: Nodes = 1..7;
set of int: Edges = 1..11;
array[Edges] of Nodes: aFrom = [ 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5];
array[Edges] of Nodes: aTo   = [ 2, 5, 6, 7, 3, 6, 4, 6, 5, 7, 7];

% Petersen Graph
%set of int: Nodes = 1..10;
%set of int: Edges = 1..15;
%array[Edges] of Nodes: aFrom = [ 1, 2, 3, 4, 1, 1, 2, 3, 4,  5, 6,  7, 7,  8, 6 ];
%array[Edges] of Nodes: aTo   = [ 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 8, 10, 9, 10, 9 ];

array[Nodes] of var Colors: nodeColor;

constraint forall(e in Edges) (abs(nodeColor[aFrom[e]] - nodeColor[aTo[e]]) > 0);

solve satisfy;

output [ show(nodeColor[n]) ++ "\n" | n in Nodes ]; 