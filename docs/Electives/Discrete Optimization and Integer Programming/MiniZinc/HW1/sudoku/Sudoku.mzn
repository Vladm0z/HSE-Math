% sudoku solver
int: S;
int: N = S * S;
int: digs = ceil(log(10.0, int2float(N)));

set of int: PuzzleRange = 1..N;
set of int: SubSquareRange = 1..S;

array[1..N, 1..N] of 0..N: start; % 0 = empty square
array[1..N, 1..N] of var PuzzleRange: puzzle;

% fill initial grid
constraint forall(i,j in PuzzleRange)(
           if start[i,j] > 0 then puzzle[i,j] = start[i,j] else true endif );

% all different in rows
constraint forall(i,j,k in PuzzleRange)(
           if abs(j - k) > 0 then (abs(puzzle[i,j] - puzzle[i,k]) > 0) endif );

% all different in columns
constraint forall(i,j,k in PuzzleRange)(
           if abs(j - k) > 0 then (abs(puzzle[j,i] - puzzle[k,i]) > 0) endif );

% all different in sub-squares
constraint forall(a, o, x1, x2, y1, y2 in SubSquareRange)(
           if (abs(x1 - x2) > 0 /\ abs(y1 - y2) > 0) then (
               abs(puzzle[(a-1)*S + x1, (o-1)*S + y1]
                 - puzzle[(a-1)*S + x2, (o-1)*S + y2]) > 0)
           endif );

solve satisfy;

output [ 
  show_int(digs,puzzle[i,j]) ++ " " ++
    if j mod S == 0 then " " else "" endif ++
    if j == N /\ i != N then
      if i mod S == 0 then "\n\n" else "\n" endif
    else "" endif
  | i,j in PuzzleRange ] ++ 
  ["\n"];