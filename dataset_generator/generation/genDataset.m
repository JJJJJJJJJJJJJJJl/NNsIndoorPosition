% Nuno Paulino (nuno.m.paulino@inesctec.pt)
% INESC TEC
% Created: 2021
% Modified: September 2021

% generates a dataset of phase differences, with groundtruth
function [dataset] = genDataset(N = 1000, incidentAngle = 0, noise = 0)  
  
  addpath ("../phasediff"); % for reshapeSamples2 and calcPhase2
  sampleSpacing = 0.5;
  switchSpacing = 4.0;
  nrSamplesPerAntena = 8;
  clockDrift = 0.0;
  nrAntenas = 8;
  nrRefSamples = 0;

  % generate a single wave of phase differences from raw phase data
  % nrPhaseDiffs = 
  % dataset = zeros(N, 
  for i=1:1:N
    [rawdata, ~] = generatePhases(incidentAngle, 140, nrSamplesPerAntena, sampleSpacing, switchSpacing, noise);       
    [est] = calcPhaseDiffs(rawdata, nrRefSamples, nrAntenas, nrSamplesPerAntena, sampleSpacing, switchSpacing, clockDrift);
    
    est=est(:, 1:8);
    
    dataset(i, :) = [est, incidentAngle];
  endfor
  
endfunction
