var
 holosni : set of char;
 i, count : integer;
 S : string;
begin
 count := 0;
 holosni := ['a', 'o', 'e', 'y', 'u', 'i', 'A', 'O', 'E', 'Y', 'U', 'I'];
 readln (S);
 for i:=1 to length(S) do
     if S[i] in holosni then
     count := count+1;
 writeln (count);
end.