var
  num : integer;
  N, M, i, j, ii, iii, ij, ijj, jj, jjj, ji, jii : byte;
  flagI, flagJ : boolean;
  a : array [0..99, 0..99] of integer;
begin
  readln(N, M);
  num := 0;
  
  i := N - 1;
  j := M - 1;

  ii := 0;
  iii := -1;
  ij := N - 1;
  ijj := N;

  jj := 0;
  jjj := -1;
  ji := M - 2;
  jii := M - 1;
  
  flagI := True;
  flagJ := False;
  
  while num <> N * M do
  begin
    num := num + 1;
    a[i, j] := num;
    if (i >= ii) and (flagI = True) and (flagJ = False) then
        i := i - 1;
    if (i = iii) and (flagI = True) and (flagJ = False) then
    begin
        i := ii;
        ii := ii + 1;
        iii := iii + 1;
        flagI := False;
        flagJ := False;
    end;
        
    if (j >= jj) and (flagI = False) and (flagJ = False) then
        j := j - 1;
    if (j = jjj) and (flagI = False) and (flagJ = False) then
    begin
        j := jj;
        jj := jj + 1;
        jjj := jjj + 1;
        flagI := True;
        flagJ := True;
    end;

    if (i <= ijj) and (flagI = True) and (flagJ = True) then
        i := i + 1;
    if (i = ijj) and (flagI = True) and (flagJ = True) then
    begin
        i := ij;
        ij := ij - 1;
        ijj := ijj - 1;
        flagI := False;
        flagJ := True;
    end;

    if (j <= jii) and (flagI = False) and (flagJ = True) then
        j := j + 1;
    if (j = jii) and (flagI = False) and (flagJ = True) then
    begin
        j := ji;
        ji := ji - 1;
        jii := jii - 1;
        flagI := True;
        flagJ := False;
        i := i - 1;
    end;
  end;
  
  for i := 0 to N - 1 do
  begin
    for j := 0 to M - 1 do
      write(a[i, j], ' ');
    writeln();
  end;
end.