var
 a:array [1..100] of real;
 i, n, countmilk, countpatty:integer;
begin
 readln(n);
 for i:=1 to n do
  read(a[i]);
 for i:=1 to n do
  if a[i]<30 then 
  countpatty:=countpatty+1;
 for i:=1 to countpatty do
  countmilk:=countmilk+200;
  
   if (countmilk mod 900)<>0 then
   countmilk:=1+countmilk div 900
   else  countmilk:=countmilk div 900;
  writeln(countmilk, ' ', countpatty);
end.