var
 h1, m1, s1, h2, m2, s2 : integer;
begin
 readln (h1, m1, s1);
 readln (h2, m2, s2);
  if m2 >= m1 then begin 
       if s2 >= s1 then writeln (h2-h1, ' ', m2-m1, ' ', s2-s1)
                  else  writeln (h2-h1, ' ', m2-m1-1, ' ', (s2+60)-s1);
                  end
             else begin
        if s2 >= s1 then writeln (h2-h1-1, ' ', (m2+60)-m1, ' ', s2-s1)
                    else writeln (h2-h1-1, ' ', (m2+60)-m1-1, ' ', (s2+60)-s1);
                    end;
end.