var
 a, b:array [1..100] of integer;
 n, m, i, s, c, count:integer;
begin
 readln(n, m);
 for i:=1 to n do
  readln(a[i], b[i]);
  for i:=1 to n do
  begin
   s:=s+a[i];
   c:=c+b[i];
  end;
  count:=(s div m)+(c div m);
   if (s mod m)>0 then count:=count+1;
   if (c mod m)>0 then count:=count+1;
  writeln(count);
end.