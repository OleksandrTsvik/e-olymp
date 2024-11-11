var
 N, M, count:integer;
begin
 readln(N, M);
 if (M=0) and (N mod 2=1) then writeln('-1') else
 begin
  while M>2 do
   begin
    M:=M-2;
    N:=N+1;
    count:=count+1;
   end;
  if (N mod 2=1) and (M=2) then
   begin
    N:=N+1;
    count:=count+1;
   end else 
  if (N mod 2=1) and (M=1) then
   begin
    N:=N+1;
    count:=count+2;
   end else
  if (N mod 2=0) and (M=2) then
   begin
    N:=N+2;
    count:=count+4;
   end else
  if (N mod 2=0) and (M=1) then
   begin
    N:=N+2;
    count:=count+5;
   end;
  while N<>0 do
   begin
    N:=N-2;
    count:=count+1;
   end;
 writeln(count);
 end;
end.