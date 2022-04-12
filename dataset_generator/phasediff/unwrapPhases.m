% Nuno Paulino (nuno.m.paulino@inesctec.pt)
% INESC TEC
% Created: 2021
% Modified: June 2021

% for each row of samples, perfom an unwrapping
function rsamples = unwrapPhases(samples)
  
  rsamples = samples;
  for i = 1:size(rsamples,1)
    for j = 2:size(rsamples,2)
      if(rsamples(i, j) < (rsamples(i, j - 1) - 180))
      %if(rsamples(i, j) < (rsamples(i, j - 1)))
        %rsamples(i, j) = rsamples(i, j) + 360;
        rsamples(i, j:end) += 360;
      endif
    endfor
  endfor
  
endfunction
