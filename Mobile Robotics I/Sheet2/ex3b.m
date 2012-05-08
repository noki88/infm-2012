scan = load("-ascii","laserscan.dat");
angle = linspace(-pi/2,pi/2,size(scan,2));
x1 = scan .* cos(angle);
y1 = scan .* sin(angle);
plot(x1, y1,'.')
print('ex3b.png', '-dpng')
