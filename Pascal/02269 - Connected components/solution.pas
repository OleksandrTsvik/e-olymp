var
 i, j, n, col:integer;
 a:array [1..100, 1..100] of integer;
 color:array [1..100] of integer;
 v:array [1..100] of boolean;
 
procedure dfs(u, cl:integer);
 var i:integer;
 begin
  v[u]:=True;
  color[u]:=cl;
  for i:=1 to n do
   if (a[u, i]=1) and (not v[i]) then
    dfs(i, cl);
 end;
 
 begin
  readln(n);
  for i:=1 to n do
   for j:=1 to n do
   read(a[i, j]);
   
  col:=0;
  for i:=1 to n do
   begin
    if color[i]=0 then
     col:=col+1;
     dfs(i, col);
   end;
 writeln(col);
end.