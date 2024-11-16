var
    x1, y1, x2, y2, x3, y3, x4, y4: integer;
    d1, d2, d3, max: real;
begin
    readln(x1, y1, x2, y2, x3, y3);

    d1:=sqrt(sqr(x2-x1)+sqr(y2-y1));
    d2:=sqrt(sqr(x3-x2)+sqr(y3-y2));
    d3:=sqrt(sqr(x3-x1)+sqr(y3-y1));

    max:=d1;

    if max<d2 then max:=d2;
    if max<d3 then max:=d3;

    if d1=max then
    begin
        x4:=x1+x2-x3;
        y4:=y1+y2-y3;
    end;

    if d2=max then
    begin
        x4:=x2+x3-x1;
        y4:=y2+y3-y1;
    end;

    if d3=max then
    begin
        x4:=x3+x1-x2;
        y4:=y3+y1-y2;
    end;

    writeln(x4, ' ', y4);
end.
