var
 i, j, n, count:integer;
 a:array [1..100, 1..100] of integer;
 color:array [1..100] of integer;
 
 begin
  readln(n);
  for i:=1 to n do
   for j:=1 to n do
   read(a[i, j]);
   
  for i:=1 to n do
   read(color[i]);
  
  for i:=1 to n do
   for j:=1 to i do
   if (a[i, j]=1) and (color[i]<>color[j]) then
    count:=count+1;
  
 writeln(count);
end.