var
 n, min, max, i:integer;
 a:array [1..30010] of integer;
begin
 readln(n);
 for i:=1 to n do
  read(a[i]);
 if n<2 then
  writeln('Ooops!')
 else begin
 min:=a[1];
 for i:=1 to n do
  begin
   if a[i]>max then
    max:=a[i];
   if a[i]<min then
    min:=a[i];
  end;
 writeln(min, ' ', max); end;
end.