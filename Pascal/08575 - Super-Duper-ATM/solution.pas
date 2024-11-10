const Money:array [1..9] of integer=(500, 200, 100, 50, 20, 10, 5, 2, 1);
var
 S, count, i:integer;
begin
 readln(S);
  for i:=1 to 9 do
  begin
   count:=count+(S div Money[i]);
   S:=S mod Money[i];
  end;
  Writeln(count);
end.