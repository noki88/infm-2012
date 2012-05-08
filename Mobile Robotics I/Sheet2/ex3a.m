scan = load("-ascii","laserscan.dat");
angle = linspace(-pi/2,pi/2,size(scan,2));
plot(angle, scan, '.')
print('ex3a.png', '-dpng')
