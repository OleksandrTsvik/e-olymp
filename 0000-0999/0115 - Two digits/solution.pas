function Fibonacci(N:integer):longint;
var
 A:array [1..30] of longint;
 i:integer;
begin
 A[1]:=2;
 A[2]:=4;
 for i:=3 to N do
  A[i]:=A[i-1]+A[i-2];
  Fibonacci:=A[n];
end;

var
 n:integer;
begin
 readln(n);
 if n=0 then writeln(0) else
 writeln(Fibonacci(n));
end.