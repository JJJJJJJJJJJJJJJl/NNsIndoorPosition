% Luís Pessoa (luis.m.pessoa@inesctec.pt)
% INESC TEC
% Created: 2021
% Modified: June 2021

%% generates theoretical phase difference wave profiles for circular array board

lambda=.12;
rho_0=lambda/2;
%d=lambda/2;
d=.04592;
phi_i=[0,1,2,3,4,5,6,7]*2*pi/8;

figure; hold on;
for phi_s=0:deg2rad(5):deg2rad(20)
    phase=2*pi/lambda*rho_0*cos(phi_s-phi_i);
    aux=zeros(1,length(phase)+1);
    aux1=aux;
    aux(2:end)=phase;
    aux1(1:end-1)=phase;
    aux3=aux1-aux;
    phase_diff=aux3(2:end-1);
    figure(1); hold on; plot(phase_diff*180/pi)
    %figure(2); hold on; plot(acos(lambda*phase_diff/(2*pi*d))*180/pi)
end

