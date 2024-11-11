var
 n:string;
 p, x, s, error:longint;
begin
 repeat
 begin
  readln(n);
  if (n='') then break;
  Val(n, x, error);
  p:=x*4;
  s:=x*x;
  writeln(p, ' ', s);
 end;
 until (n='');
end.