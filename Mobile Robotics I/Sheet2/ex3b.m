scan = load("-ascii","laserscan.dat");
angle = linspace(-pi/2,pi/2,size(scan,2));
x1 = scan .* cos(angle);
y1 = scan .* sin(angle);
plot(1,0.5,'@1')
hold on
laser = X(1,0.5,(pi)/4)*[0.2;0;1];
plot(laser(1,1),laser(2,1),'@2')
hold off
print('ex3b.png', '-dpng')
