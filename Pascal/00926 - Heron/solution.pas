function Heron(a, b, f:real):real;
 var
  p:real;
begin
 p := (a+b+f)/2;
 Heron := sqrt(p*(p-a)*(p-b)*(p-f));
end;

var
 a, b, c, d, f : real;
begin
 readln (a, b, c, d, f);
   writeln ((Heron(a, b, f)+heron(c, d, f)):0:4);
end.