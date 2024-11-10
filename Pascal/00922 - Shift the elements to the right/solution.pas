var
 n, i : integer;
 a : array [1..100] of real;
 temp : real;
begin
 readln (n);
 for i:=1 to n do
  read(a[i]);
  temp := a[n];
 for i:=n downto 2 do
  a[i]:=a[i-1];
  a[1]:=temp;
  for i:=1 to n do
  write (a[i], ' ');
end.