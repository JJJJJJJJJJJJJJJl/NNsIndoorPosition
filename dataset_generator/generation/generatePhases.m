% Nuno Paulino (nuno.m.paulino@inesctec.pt)
% INESC TEC
% Created: 2021
% Modified: June 2021

% generates a set of samples for 8 atennas, 
function [phaseSamples, allPhases] = generatePhases(incidentAngle = 0, timeCTE = 250, 
    nrSamplesPerAntenna = 8, sampleSpacing = 0.5, switchSpacing = 4, noise = 0) 

% physical parameters
nrAntennas=8;
lambda=.12; % 2.4Ghz wavelength
rho_0=lambda/2;
d=0.046; % meters

% angle of each antenna relative to incidentAngle of 0º
phi_i=[0,1,2,3,4,5,6,7]*2*pi/8; 

% angle of incoming wave
phi_s = deg2rad(incidentAngle);

% phase values at each anteanna for a single moment in time (t = 0)
%phase = 2*pi/lambda*rho_0*cos(phi_s-phi_i);
phase = 2*pi/lambda*rho_0*cos(phi_s-phi_i) + ((pi/2) * rand() * 4);

% all phases for all antennas for a total time of timeCTE
degStep = deg2rad(90) * sampleSpacing;
%phaseProgression = [0.0:degStep:(degStep * timeCTE)]';
phaseProgression = [0.0:degStep:(deg2rad(90) * timeCTE)]';
phases = phase(ones(1,size(phaseProgression, 1)), :) + phaseProgression(:, ones(1, 8));
phases = rem(rad2deg(phases), 360) - 180; % normalize to the sample values we would get
allPhases = phases;

% create sampling indexes as they would happen in the real board
pattern = [ones(1, nrSamplesPerAntenna), zeros(1, nrSamplesPerAntenna * (nrAntennas-1))]';

% nr repeats throughout time
reps = ceil(size(phases, 1) / size(pattern, 1));
pattern = repmat(pattern, reps, 1);
pattern = pattern(1:size(phases, 1));

samplePattern = pattern;
shifted = pattern;
for i=1:1:7
  shifted = [zeros(nrSamplesPerAntenna, 1); shifted(1:end-nrSamplesPerAntenna)];
  samplePattern = [samplePattern shifted];
  %samplePattern = [samplePattern, shift(pattern, (nrSamplesPerAntenna * i))];
end

% add noise before sampling everything? (seems to have the same effect)
phases = phases .+ noise * randn(size(phases));

% TODO: add multipath effect by shifting the phases themselves?

% sample
phaseSamples = phases .* samplePattern;

% flatten the samples into a single column vector (by "lateral sum")
phaseSamples = sum(phaseSamples, 2);

% add gaussian noise ("noise" is stddev given in degrees)
% see: https://www.mathworks.com/help/matlab/math/random-numbers-with-specific-mean-and-variance.html
%phaseSamples = phaseSamples .+ noise * randn(size(phaseSamples, 1), 1);

endfunction
