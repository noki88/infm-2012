x_t = [2, 4, 0];
u_t = [(pi)/2, 0, 1];
alpha = [0.1, 0.1, 0.01, 0.01];

x=[];
y=[];

hold on
axis([-3,7,-1,9]);

for i=1:5000
  x_t1 = motionmodel(x_t,u_t,alpha);
  x=[x,x_t1(1)];
  y=[y,x_t1(2)];
end

plot(x,y,'.');
hold off