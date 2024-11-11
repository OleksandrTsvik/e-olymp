type Time = record
  hours:integer;
  minets:integer;
  seconds:integer;
end;

var t:array [1..100] of Time;

procedure ReadTime(i:integer);
var h, m, s:integer;
  begin
   readln(h, m, s);
   t[i].hours:=h;
   t[i].minets:=m;
   t[i].seconds:=s;
  end;
  
procedure SortTime(i, j:integer);
var ti:time;
 begin
  ti:=t[i];
  t[i]:=t[j];
  t[j]:=ti;
 end;
  
procedure WriteTime(i:integer);
  begin
   writeln(t[i].hours, ' ', t[i].minets, ' ', t[i].seconds);
  end;

var
n, i, j:integer;
begin
 readln(n);
 for i:=1 to n do
  ReadTime(i);
 
for j:=1 to n-1 do 
 for i:=1 to n-j do
   if t[i].hours>t[i+1].hours then
    SortTime(i, i+1);
for j:=1 to n-1 do 
 for i:=1 to n-j do
  if (t[i].hours=t[i+1].hours) and (t[i].minets>t[i+1].minets) then
   SortTime(i, i+1);
for j:=1 to n-1 do 
 for i:=1 to n-j do
  if (t[i].hours=t[i+1].hours) and (t[i].minets=t[i+1].minets) and (t[i].seconds>t[i+1].seconds) then
   SortTime(i, i+1);

 for i:=1 to n do
  WriteTime(i);
end.