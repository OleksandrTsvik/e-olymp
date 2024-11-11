const Nmax=4;
type matrix=array [1..Nmax, 1..Nmax] of longint;
var
 A:matrix;
 i, j, x, y, M, N :longint;
begin
 readln(M, N);
 readln(x, y);
    A[1, 1]:=x;    A[1, 2]:=y-1;
    A[2, 1]:=x+1;  A[2, 2]:=y;
    A[3, 1]:=x;    A[3, 2]:=y+1;
    A[4, 1]:=x-1;  A[4, 2]:=y;
    
    for i:=1 to 4 do
    if ((A[i, 1] in [1..M]) and (A[i, 2] in [1..N])) then writeln(A[i, 1], ' ', A[i, 2]);
end.