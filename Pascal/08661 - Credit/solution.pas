var
 flag:boolean;
 i, count, b:integer;
 p, k, a, percent:real;
begin
 flag:=True;
 readln(a, p, b);
 while (a>0) do
 begin
  for i:=1 to 7 do
  begin
   percent:=a*(p/100);
   a:=a+percent;
  end;
  if (b<percent) then 
   begin
    flag:=False;
    writeln('-1');
    break;
   end else
  begin
    k:=a;
    a:=a-b;
    count:=count+1;
  end;
 end;
 if flag=True then
  writeln(count, ' ', k:0:2);
end.