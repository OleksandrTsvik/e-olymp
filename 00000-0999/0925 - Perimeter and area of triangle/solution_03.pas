var
 x1, y1, x2, y2, x3, y3, P, h, S, D, A, B, C:real;
begin
 readln (x1, y1, x2, y2, x3, y3);
  A:=sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
  B:=sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3));
  C:=sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3));
   P:=A+B+C;
   h:= P/2;
   S:=sqrt(h*(h-A)*(h-B)*(h-C));
    writeln(P:0:4, ' ', S:0:4);
end.