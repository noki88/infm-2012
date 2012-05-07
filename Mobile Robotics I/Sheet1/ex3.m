% generate vectors with random numbers
v = 10000;
a = normrnd (5,2,1,v);
b = unifrnd (0,10,1,v);

% calculate mean and standard deviation
mean_a = mean(a)
std_a = std(a)
mean_b = mean(b)
std_b = std(b)

% plot both histograms
close all
hist(a)
print('ex3_fig_a.png', '-dpng')
figure
hist(b)
print('ex3_fig_b.png', '-dpng')
