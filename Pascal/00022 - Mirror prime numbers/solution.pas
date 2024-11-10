function isSimple(N:integer):boolean;
 var i, count:integer;
 begin
  count:=0;
 for i:=1 to N do
   if N mod i=0 then
    count:=count+1;
  if count=2 then isSimple:=True else isSimple:=False;
 end;
 
function mirror(a:integer):integer;
 var c, res:integer;
 begin
 res:=0;
  while a>0 do
   begin
     c:=a mod 10;
     a:=a div 10;
     res:=res*10+c;
   end;
   mirror:=res;
 end;
 
var
 x, y, i, count:integer;
begin
 readln(x, y);
   for i:=x to y do
    begin
     if (isSimple(i) and isSimple(mirror(i))) then count:=count+1;
    end;
    writeln(count);
end.