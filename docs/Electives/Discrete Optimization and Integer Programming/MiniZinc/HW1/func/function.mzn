int: N=8;
array[1..N] of var float: f;
constraint forall(i in 1..N, j in 1..N, k in 1..N)(f[i] + f[j] + f[k] <= i*j*k/(N*N*N)+1);
solve maximize f[N];