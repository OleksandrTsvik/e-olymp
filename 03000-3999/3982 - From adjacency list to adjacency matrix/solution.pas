var
 i, j, k, n, count:integer;
 a:array [1..100, 1..100] of integer;
begin
 readln(n);
 
 for i:=1 to n do
 begin
  read(count);
  for k:=1 to count do
  begin
   read(j);
   a[i, j]:=1;
  end;
  readln();
 end;

 for i:=1 to n do
  begin
  for j:=1 to n do
   if j<>n then
    write(a[i, j], ' ')
   else write(a[i, j]);
   writeln(); 
  end;
end.