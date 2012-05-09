scan = load("-ascii","laserscan.dat");
angle = linspace(-pi/2,pi/2,size(scan,2));
x1 = scan .* cos(angle);
y1 = scan .* sin(angle);
plot(1,0.5,'@1')
hold on
X_roboter = X(1,0.5,(pi)/4);
X_laser = X(0.2,0,(pi));
pos_laser = X_roboter*[0.2;0;1];
plot(pos_laser(1,1),pos_laser(2,1),'@3')

for i = 1:size(scan,2)
  pos_res = X_roboter*X_laser*[x1(i);y1(i);1];
  plot(pos_res(1,1),pos_res(2,1),'o5')
endfor
  
hold off
print('ex3b.png', '-dpng')
