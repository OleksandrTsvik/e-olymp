const maxn=32;
type matrix=array [0..maxn, 0..maxn] of string;

var
 s:string;
 n, m, w, i, j, x, y, ii, jj, count:integer;
 a:matrix;
begin
 readln(n, m);
 for i:=0 to n+1 do
 for j:=0 to m+1 do
  a[i, j]:='0';
  
   readln(w);
   for i:=1 to w do
    begin
     readln(x, y);
     a[x, y]:='*';
    end;
   
   for i:=1 to n do
   for j:=1 to m do
    begin
     if a[i, j]='0' then
      begin
       for ii:=i-1 to i+1 do
       for jj:=j-1 to j+1 do
        if a[ii, jj]='*' then
         count:=count+1;
       str(count, s);
       a[i, j]:=s;
       count:=0;
      end;
    end;
   
   for i:=1 to n do
    begin
   for j:=1 to m do
   begin
   if j<m then
   write(a[i, j], ' ')
   else write(a[i, j]);
   end;
   writeln;
    end;
end.