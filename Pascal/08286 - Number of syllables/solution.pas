var
 a:array [0..1000] of integer;
 i, n:integer;
begin
 readln(n);
 a[1]:=2; a[2]:=1; a[3]:=1; a[4]:=3; a[5]:=1;
 a[6]:=1; a[7]:=1; a[8]:=2; a[9]:=2; a[11]:=4;
 a[12]:=3; a[13]:=3; a[14]:=4; a[15]:=3; a[16]:=3; a[17]:=3;
 a[18]:=4; a[19]:=4;
 
 a[10]:=2; a[20]:=2; a[30]:=2; a[40]:=2; a[50]:=3; a[60]:=3; 
 a[70]:=3; a[80]:=4; a[90]:=4;
 
 a[100]:=1; a[200]:=2; a[300]:=2; a[400]:=4; a[500]:=2; a[600]:=2; a[700]:=2;
 a[800]:=3; a[900]:=3; a[1000]:=3;
 
 if n=0 then writeln(1) else
 if n<=19 then writeln(a[n]) else
 if (n mod 10=0) and (n<100) then writeln(a[n]) else
 if (n>=20) and (n<100) then writeln(a[n mod 10]+a[(n div 10)*10]) else
 if (n mod 100=0) or (n mod 1000=0) then writeln(a[n]) else
 if (n>100) and (((n div 10)mod 10)=0) then writeln(a[(n div 100)*100]+a[n mod 10]) else
 if (n>100) and (n mod 100<=19) then writeln(a[n mod 100]+a[(n div 100)*100]) else
 if (n>119) and ((n mod 10)=0) then writeln(a[((n div 10)mod 10)*10]+a[(n div 100)*100]) else
 if (n>119) and ((n mod 10)>0) and (((n div 10)mod 10)>0) then writeln(a[((n div 10)mod 10)*10]+a[(n div 100)*100]+a[n mod 10]);
end.