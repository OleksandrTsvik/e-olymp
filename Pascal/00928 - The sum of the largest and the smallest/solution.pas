var
 i, n, max, min : integer;
 a : array [1..100] of integer;
begin
 readln (n);
  for i := 1 to n do
    read (a[i]);
  min := a[1];
  max := a[1];
  for i := 1 to n do
   begin
   if a[i]>max then max := a[i];
   if a[i]<min then min := a[i];
   end;
     writeln (max+min);
end.