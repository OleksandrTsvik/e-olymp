function Sum(x,y:real):real;
 begin
 Sum:=x+y;
 end;
 
function Dob(x, y :real):real;
 begin
 Dob:=x*y;
 end;
 
var
 a, b:array [1..100] of real;
 N, i:integer;
 begin
  readln(N);
  for i:=1 to N do
   readln(a[i], b[i]);
  for i:=1 to N do
writeln((Sum(a[i], b[i])):0:4, ' ', (Dob(a[i], b[i])):0:4);
end.