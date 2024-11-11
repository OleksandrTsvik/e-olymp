var
 x1, y1, x2, y2, x3, y3:real;
begin
 readln(x1, y1, x2, y2, x3, y3);
 writeln((sqrt((sqr(x2-x1))+(sqr(y2-y1))))+(sqrt((sqr(x3-x2))+(sqr(y3-y2))))+(sqrt((sqr(x3-x1))+(sqr(y3-y1)))):0:4, ' ', (abs((0.5*(((x1*y2)+(x2*y3)+(x3*y1))-((y1*x2)+(y2*x3)+(y3*x1)))))):0:4);
end.