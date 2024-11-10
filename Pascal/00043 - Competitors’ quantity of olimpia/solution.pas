var
 K, N, M, D:longint;
begin
 readln(K, N, M, D);
  if (K*N*M*D/(K*N*M-K*M-K*N-M*N))<>(trunc(K*N*M*D/(K*N*M-K*M-K*N-M*N))) then 
   writeln('-1') else
   writeln(trunc(K*N*M*D/(K*N*M-K*M-K*N-M*N)));
end.