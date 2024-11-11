var
 n, i, j, temp:longint;
 a:array [1..1000] of int64;
begin
 readln(n);
 for i:=1 to n do
  read(a[i]);
  
 for i:=1 to n do
  for j:=1 to n-1 do
    if a[j]>a[j+1] then
   begin
     temp:=a[j+1];
     a[j+1]:=a[j];
     a[j]:=temp;
   end;
  
  for i:=1 to n-1 do
   if a[i]<>a[i+1] then
   begin
    writeln(a[1], ' ', a[i+1]);
    break;
   end;
end.