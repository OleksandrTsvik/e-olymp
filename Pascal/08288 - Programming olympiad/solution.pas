var 
 n,a,b,c,x,y,z,sum,sum1,sum2:integer; 
begin 
 readln(n,a,b,c,x,y,z); 
  sum:=a+b+c;
  sum1:=sum-n;
  if (a=0) or (b=0) or (c=0) then writeln(0) else
 begin
  sum2:=x+y+z;
  sum:=abs(sum2-sum1); 
 writeln(sum);
  end;
end.