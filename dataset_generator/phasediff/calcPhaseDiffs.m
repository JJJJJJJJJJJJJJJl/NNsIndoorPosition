% Nuno Paulino (nuno.m.paulino@inesctec.pt)
% INESC TEC
% Created: 2021
% Modified: June 2021

function vecdiff = calcPhaseDiffs(
	samples, 
	nrRefSamples = 0, 
	nrAntenas = 8, 
	nrSamplesPerAntena = 3, 
	sampleSpacing = 0.5, 
	switchSpacing = 4.0, 
	clockDrift = 0.1)
  
  % 
  [~, samples] = reshapeSamples(samples, nrRefSamples, nrAntenas, nrSamplesPerAntena, sampleSpacing, clockDrift);
  
  % linearize
  samples = unwrapPhases(samples);
  
  % approximate (naive)
  #for i = 1:size(samples,1)
    #samples(i, :) = (ones(1, size(samples, 2)) * mean(samples(i, :))) + [-45, 0, +45];
  #endfor

  % approximate via linear fitting
%  maxtime = sampleSpacing * (size(samples, 2) - 1);
%  x = [0:sampleSpacing:maxtime];
%  F = [ones(3, 1), x(:)];
%  for i = 1:size(samples,1)
%    b = F \ samples(i, :)';
%    samples(i, :) = b(2)*x + b(1);
%  endfor
  
  % for each batch
  %diffs = zeros(size(samples, 1), 1));
#  maxtime = sampleSpacing * (size(samples, 2) - 1);
  #x = [0:sampleSpacing:maxtime];
  vecdiff = zeros(1, size(samples, 1));
  for i = 2:size(samples,1)
    
    % ant i-1
    batch1 = samples(i - 1, :);         
    #mest1 = mean(diff(batch1) ./ sampleSpacing);
    
    #phasePredict1 = (ones(1, size(samples, 2)) * mean(batch1)) + [-45, 0, +45];
    
    %phasePredict1 = mest1 * (x + (switchSpacing)) + batch1(1);
    phasePredict1 = batch1;
          
    % ant i
    batch2 = samples(i, :);        
    phasePredict2 = batch2;

    % phase diff
    phaseDiff = mean(phasePredict2 - phasePredict1);    
    phaseDiff = mod(phaseDiff + 180, 360) - 180;
    
    vecdiff(i - 1) = phaseDiff; 
  endfor  
  #vecdiff = vecdiff - mean(vecdiff); # center  
  #vecdiff = mod(vecdiff + 180, 360) - 180;
  #vecdiff = vecdiff - mean(vecdiff); # center  
  
  
 # for i = 2:size(vecdiff,2)
 #   while(abs(vecdiff(i - 1) - vecdiff(i)) >= 360)
 #     vecdiff(i) = vecdiff(i) + 360 * sign( vecdiff(i - 1));
 #   endwhile    
 # endfor
   
endfunction
