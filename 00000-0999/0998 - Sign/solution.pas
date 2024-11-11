function Distance(x1, y1, x2, y2:integer):integer;
begin
 Distance:=abs(x1-x2)+abs(y1-y2);
end;

var
 i, j, ii, count, n, m, min:integer;
 a:array [1..100, 1..100] of integer;
 b:array [1..10000, 1..2] of integer;
 c:array [1..100, 1..100] of integer;
begin
 readln(n, m);
 for i:=1 to n do
  for j:=1 to m do
   read(a[i, j]);
   
 for i:=1 to n do
  for j:=1 to m do
    if a[i, j]=1 then
     begin
      count:=count+1;
      b[count, 1]:=i;
      b[count, 2]:=j;
     end;
 
 for i:=1 to n do
  for j:=1 to m do
  begin
   min:=Distance(i, j, b[1, 1], b[1, 2]);
    for ii:=1 to count do
     if min>Distance(i, j, b[ii, 1], b[ii, 2]) then
      min:=Distance(i, j, b[ii, 1], b[ii, 2]);
   c[i, j]:=min;
  end;
 
 for i:=1 to n do
 begin
  for j:=1 to m do
  if j<>m then
   write(c[i, j], ' ')
  else write(c[i, j]);
   writeln();
 end;
end.