function Max(x, y:real):real;
 begin
  if x>y then Max:=x else Max:=y;
 end;
 
function Min(x, z:real):real;
 begin
  if z<x then Min:=z else Min:=x;
 end;
 
function Min(x, y, z:real):real;
 begin
  if Min(x, y)<z then
   Min:=Min(x, y) else Min:=z;
 end;
 
var
 x, y, z : real;
begin
 read(x, y, z);
 
  writeln((min(max(x,y), max(y,z), x+y+z)):0:2);
end.