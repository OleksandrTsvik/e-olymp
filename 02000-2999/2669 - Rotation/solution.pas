const Nmax=50;
type matrix=array [1..Nmax, 1..Nmax] of longint;
var
 A, B:matrix;
 i, j, x, y :longint;
begin
 readln(x, y);
  for i:=1 to x do
   for j:=1 to y do
    read(A[i, j]);
    
  writeln(y, ' ', x);  
  
  for i:=1 to x do
   for j:=1 to y do
    B[j, x-i+1]:=A[i, j];
    
  for i:=1 to y do
   begin
   for j:=1 to x do
    write(B[i, j], ' ');
    writeln;
   end;
end.