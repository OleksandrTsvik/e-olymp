function min(a,b:integer):integer;
begin
 if a>b then min:=b else min:=a;
end;

var
a,b:array [1..3] of integer;
 i, count:integer;
begin
 for i:=1 to 3 do
  read(a[i]);
 for i:=1 to 3 do
  read(b[i]);
   for i:=1 to 2 do
   begin
    count:=count+min(a[i], b[i]);
    a[i]:=a[i]-min(a[i], b[i]);
    b[i]:=b[i]-min(a[i], b[i]);
   end;
  for i:=1 to 2 do
   begin
    count:=count+min(a[3], b[i]);
    a[3]:=a[3]-min(a[3], b[i]);
   end;
  for i:=1 to 2 do
   begin
    count:=count+min(b[3], a[i]);
    b[3]:=b[3]-min(b[3], a[i]);
   end;
  count:=count+min(a[3], b[3]);
writeln(count);
end.