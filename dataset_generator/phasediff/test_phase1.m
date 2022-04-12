% Luís Pessoa (luis.m.pessoa@inesctec.pt)
% INESC TEC
% Created: 2021
% Modified: June 2021

%clear all;
lambda=.12;
rho_0=lambda/2;
d=.04592;
phi_i=[0,1,7,6,4,5,3,2,0,1,7,6,4,5,3,2,0,1,7,6,4,5,3,2]*2*pi/8;
figure; hold on;
phi_s_sweep=0;%[0:pi/2/8:pi/2];
yy=zeros(length(phi_s_sweep),length(phi_i)-1);
idx=1;
for phi_s=phi_s_sweep
phase=2*pi/lambda*rho_0*cos(phi_s-phi_i);
aux=zeros(1,length(phase)+1);
aux1=aux;
aux(2:end)=phase;
aux1(1:end-1)=phase;
aux3=aux1-aux;
phase_diff=aux3(2:end-1);

figure(1); hold on; plot(phase_diff*180/pi)
yy(idx,:)=real(acos(lambda*phase_diff/(2*pi*d))*180/pi);

%yy1=phi_s*180/pi-yy
figure(2); hold on; plot(yy(idx,:))
idx=idx+1;
figure(3); hold on; plot(phase)
end 
