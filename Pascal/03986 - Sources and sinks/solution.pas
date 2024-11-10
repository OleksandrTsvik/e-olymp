var
 i, j, n, countu, countv:integer;
 a:array [1..100, 1..100] of integer;
 v, u:array [1..100] of integer;
begin
 readln(n);
 for i:=1 to n do
  for j:=1 to n do
   read(a[i, j]);
   
 for i:=1 to n do
  for j:=1 to n do
  if a[i, j]=1 then
   begin
    v[i]:=v[i]+1;
    u[j]:=u[j]+1;
   end;
   
 for i:=1 to n do
  begin
   if v[i]=0 then
    countv:=countv+1;
   if u[i]=0 then
    countu:=countu+1;
  end;
  
  write(countu, ' ');
   for i:=1 to n do
   if u[i]=0 then
    write(i, ' ');
    
  writeln();
  
   write(countv, ' ');
   for i:=1 to n do
   if v[i]=0 then
    write(i, ' ');
end.