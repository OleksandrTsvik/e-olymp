var
 a:array [1..400000] of longint;
 i, L, W, H, n:integer;
begin
 readln(n);
 for i:=1 to n do
  begin
  readln(L, W, H);
   a[i]:=(((W*H*2)+(L*H*2)) div 16);
    if (((W*H*2)+(L*H*2)) mod 16)<>0 then
    a[i]:=a[i]+1;
  end;
  for i:=1 to n do
   writeln(a[i]);
end.