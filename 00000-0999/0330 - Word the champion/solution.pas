function isPal(s: string): boolean;
var
  i,j: integer;
begin
  i:= 1;
  j:= Length(s);
 
  isPal:= (i <= j); 
  
   
     while(i < j) do begin
    if(s[i] <> s[j]) then begin ispal:=false; break; end;
    inc(i);
    dec(j);
  end;
end; 

var s:string;
     PS:string;
    i,j:integer;
    Words:array [1..130] of string; 
    PalNumber:byte; palWords:string;
    
const Sword=['A'..'Z','a'..'z','0'..'9',#39,'-'];
      SSmallLetters=['a'..'z'];
begin
read(s);
s:=s+' ';
for i:=1 to length(s) do 
  if s[i] in SSmallLetters then s[i]:=Upcase(s[i]);
  
i:=1; j:=0;
PS:='';
    for i:=1 to length(s) do begin
    
    if (s[i]in Sword) and (s[i+1] in Sword) then 
       
            PS:=PS+s[i];
            
        
    if (s[i] in Sword) and not (s[i+1] in Sword) then 
           begin
           PS:=PS+S[i];
          
           j:=j+1;
           words[j]:=PS;
           PS:='';
           end;       
end;

PalNumber:=0; palWords:='-';
for i:=1 to j do
  begin
  if isPal(words[i]) and (length(words[i])> length(palWords)) then begin
     palWords:=words[i];
     PalNumber:=i;
  end;
  end;
writeln(PalNumber);
end.