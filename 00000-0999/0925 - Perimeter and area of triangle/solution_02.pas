function D(x1, y1, x2, y2:real):real;
begin
 D:=sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
end;


function S(A, B, C:real):real;
 var h:real;
begin
 h:= (A+B+C)/2; 
 S:=sqrt(h*(h-A)*(h-B)*(h-C));
end; 

var
 x1, y1, x2, y2, x3, y3, A, B, C:real;
begin
 readln (x1, y1, x2, y2, x3, y3);
  A:=D(x1, y1, x2, y2);
  B:=D(x1, y1, x3, y3);
  C:=D(x2, y2, x3, y3);
   
 writeln((A+B+C):0:4, ' ', S(A, B, C):0:4);
end.