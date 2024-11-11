var
 s:string;
 suma, i:integer;
begin
  s := ' ';
  while s<>'' do begin
  read(s);
  for i:=1 to length(s) do
    begin
      if s[i]='1' then
			  suma += 1
		  else if s[i]='2' then
			  suma := suma + 2
  		else if s[i]='3' then
  			suma := suma + 3
  		else if s[i]='4' then
  			suma := suma + 4
  		else if s[i]='5' then
  			suma := suma + 5
  		else if s[i]='6' then
  			suma := suma + 6
  		else if s[i]='7' then
  			suma := suma + 7
  		else if s[i]='8' then
  			suma := suma + 8
  		else if s[i]='9' then
  			suma := suma + 9;
    end; end;
  
  writeln(suma);
end.