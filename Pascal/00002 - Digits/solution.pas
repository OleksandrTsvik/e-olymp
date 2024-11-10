var
  numbers : array ['0'..'9'] of char;
 i, count:integer;
 S:string;
begin
 readln(S);
  for i:=1 to Length(S) do
   if s[i] in ['0'..'9'] then
    count:=count+1;
 writeln(count);
end.