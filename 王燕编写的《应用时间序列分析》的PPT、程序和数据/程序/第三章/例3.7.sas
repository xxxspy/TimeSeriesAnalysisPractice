data a;
x_1=0;
e_1=0;
do t=-100 to 1000;
e=rannor(12345);
x=0.5*x_1+e-0.8*e_1;
x_1=x;
e_1=e;
if t>0 then output ;
end;
data a;
set a;
keep t x;
proc arima;
identify var=x nlag=20 outcov=out;
proc gplot data=out;
plot corr*lag partcorr*lag ;
symbol c=red i=needle v=none;
run;
