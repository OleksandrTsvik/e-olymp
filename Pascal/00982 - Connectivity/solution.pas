var
 i, j, k, n, m, v:integer;
 a:array [1..100, 1..100] of integer;
 b:array [1..100] of boolean;
 connected:boolean;

procedure dfs(v:integer);
var i:integer;
 begin
  b[v]:=True;
  for i:=1 to n do
   if (a[v, i]=1) and (not b[i]) then
    dfs(i);
 end;

begin
 connected:=True;
 readln(n, m);
 for k:=1 to m do
 begin
  read(i, j);
  a[i, j]:=1;
  a[j, i]:=1;
 end;
  
   dfs(1);
    
  for i:=1 to n do
   if not b[i] then
   begin
    connected:=False;
    break;
   end;
   
  if connected then
   writeln('YES')
  else writeln('NO');
 end.