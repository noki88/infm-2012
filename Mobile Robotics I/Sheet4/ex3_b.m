hold on

% plot density of d1
xy1=[-10:0.1:10];
[x1,y1]=meshgrid(xy1,xy1);
plot3(x1+5,y1+7,normpdf(4.1-(sqrt(x1.*x1+y1.*y1))*1,0,1.5));

% plot density of d0
xy0=[-10:0.1:10];
[x0,y0]=meshgrid(xy0,xy0);
surf(x0+12,y0+4,normpdf(3.9-(sqrt(x0.*x0+y0.*y0))*1,0,1));

hold off