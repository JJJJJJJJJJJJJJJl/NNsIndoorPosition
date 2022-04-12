% Nuno Paulino (nuno.m.paulino@inesctec.pt)
% INESC TEC
% Created: 2021
% Modified: June 2021

%% Transforms a sequence of (nRefSamples + 4 + nSamplesPerAntena * nAntenas)
%% into a matrix where each row is a list of valid samples for a single
%% antena; each row is one antenna, and a circular visiting pattern is assumed

function [subsamples, rsamples] = reshapeSamples(samples, nRefSamples, nAntenas, nSamplesPerAntena, sampleSpacing, clockDrift)
  
  % trim ref
  samples = samples(nRefSamples+1:end);
  
  % drift fix
  if(clockDrift > 0) 
    deltaDrift = clockDrift * sampleSpacing;
    drift = [0:deltaDrift: deltaDrift * (size(samples, 1) - 1)]';
    samples = samples - drift; 
  endif
  
  % nr full batches
  nrBatches = floor(size(samples, 1) / (nAntenas * nSamplesPerAntena));
  
  % trim
  usefulSamples = nrBatches * nAntenas * nSamplesPerAntena;
  samples = samples(1:usefulSamples);
  
  % reshape into rows of nSamplesPerAntena samples (columns)
  rsamples = reshape(samples, nSamplesPerAntena, [])';
  
  % discard last half (switch slot of next antenna)
 % rsamples = rsamples(:,1:end-5); % end-4
   
  % scale to -180 to 180
  rsamples = rsamples .* (180.0/pi/64.0);
    % NOTE: only applicable for real data from the board?? 
    % for generated data, comment this line, I think
  
  % reflatten
  subsamples = rsamples'(:);

endfunction
