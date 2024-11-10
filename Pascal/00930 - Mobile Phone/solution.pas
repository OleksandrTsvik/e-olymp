var
 numbers : array ['0'..'9'] of boolean;
 i, count : integer;
 S : string;
 c:char;
begin
 count := 0;
 readln (S);
 for c := '0' to '9' do
  numbers[c] := False;
 for i:=1 to length(S) do
  if s[i] in ['0'..'9'] then  numbers[s[i]] := True;
 
 for c:='0' to '9' do
  if numbers[c]=False then
   count := count+1; 
   writeln (count);
 for c:='0' to '9' do
  if numbers[c]=False then
    write (c, ' ');
end.