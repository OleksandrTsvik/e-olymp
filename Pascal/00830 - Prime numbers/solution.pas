var
 i, j, n, m, count:longint;
 isPrime:boolean;
begin
 readln(n, m);
 isPrime:=True;

 for i:=n to m do
 begin
  isPrime:=True;
  for j:=2 to round(sqrt(i)) do
   if i mod j=0 then
    begin
     isPrime:=False;
     break;
    end;
   if isPrime then
   begin
    writeln(i);
    count:=1;
   end;
 end;
 
 if count=0 then
  writeln('Absent')
end.