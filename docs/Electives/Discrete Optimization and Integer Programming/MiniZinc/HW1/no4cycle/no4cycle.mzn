int: N=12;
array[1..N, 1..N] of var 0..1: x;
var float: e;
solve maximize sum(i in 1..N, j in 1..N)(x[i,j])/2;
constraint
  e = sum(i in 1..N, j in 1..N)(x[i,j])/2 /\
  forall(i,j,k,m in 1..N where i!=j /\ i!=k /\ i!=m /\ j!=k /\ j!=m /\ k!=m)(
      x[i,j]+x[j,k]+x[k,m]+x[m,i]<=3) /\
  forall(i,j in 1..N)(x[i,j]=x[j,i]) /\
  forall(i in 1..N)(x[i,i]=0);
