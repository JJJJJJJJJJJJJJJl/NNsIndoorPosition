% Nuno Paulino (nuno.m.paulino@inesctec.pt)
% INESC TEC
% Created: 2021
% Modified: September 2021

% generates a dataset of phases, with groundtruth
function [dataset] = genRawDataset(N = 1000, incidentAngle = 0, noise = 0)  
  
  sampleSpacing = 0.5;
  switchSpacing = 4.0;
  nrSamplesPerAntena = 8;
  clockDrift = 0.1;
  
  % generate a single wave of rawoctaved phases
  % nrPhaseDiffs = 
  % dataset = zeros(N, 
  for i=1:1:N
    [rawdata, ~] = generatePhases(incidentAngle, 250, nrSamplesPerAntena, sampleSpacing, switchSpacing, noise);    
    dataset(:, i) = [rawdata; incidentAngle];
  endfor
  
endfunction