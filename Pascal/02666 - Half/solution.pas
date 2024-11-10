const Nmax=20;
type matrix=array [1..Nmax, 1..Nmax] of integer;
var
 A, B:matrix;
 n, i, j:integer;
begin
 readln(n);
  for i:=1 to n do
   for j:=1 to n do
    begin
    if i=j then A[i, j]:=0;
    if i>j then A[i, j]:=1;
    if i<j then A[i, j]:=2;
    end;
    
  for i:=1 to n do
   for j:=1 to n do
    B[i, n-j+1]:=A[i, j];
    
  for i:=1 to n do
   begin
   for j:=1 to n do
   write(B[i, j]);
   writeln;
   end;
end.