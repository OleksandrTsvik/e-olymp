function Palindrom(s:string):boolean;
 var i, j:integer;
begin 
  j:=Length(S);
  Palindrom:=true;
  for i:=1 to Length(S) do
   begin
  if S[i]<>S[j] then Palindrom:=false
  else j:=j-1;
   end;
end;

function Mirror(s:string):string;
var 
 i:integer;
 k:string;
begin
 k:=S;
 for i:=1 to Length(S) do
  k[Length(S)-i+1]:=s[i];
  Mirror:=k;
end;

function Suma(s1, s2:string):string;
var
 res:string;
 a, b, c:int64;
 error:integer;
begin
 Val(s1, a, error);
 Val(s2, b, error);
 c:=a+b;
 Str(c, res);
 Suma:=res;
end;

var
 count:integer;
 S:string;
begin
 readln(S);
  count:=0;
  While  Palindrom(S)=False do
   begin
    S:=Suma(Mirror(S), S);
    count:=count+1;
   end; 
  writeln(count);
end.