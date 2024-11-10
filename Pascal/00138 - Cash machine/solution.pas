const Money:array [1..6] of integer=(500, 200, 100, 50, 20, 10);
var
 S, count, i:longint;
begin
 readln(S);
  for i:=1 to 6 do
  begin
   count:=count+(S div Money[i]);
   S:=S mod Money[i];
  end;
  if S>0 then Writeln('-1')
  else Writeln(count);
end.