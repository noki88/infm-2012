i=1000;

% generate samples by summing up
disp("normal distributed samples by summing up:");
samples=[];
tic
for j=1:i
  samples = [samples, sample_summing(0,1)];
end
seconds = toc
figure
hist(samples)
title("summing up")

% generate samples by rejection
disp("normal distributed samples by rejection:");
samples=[];
tic
for j=1:i
  samples = [samples, sample_rejection(0,1)];
end
seconds = toc
figure
hist(samples)
title("rejection")

% generate samples by box-muller
disp("normal distributed samples by box-muller:");
samples=[];
tic
for j=1:i
  samples = [samples, sample_boxmuller(0,1)];
end
seconds = toc
figure
hist(samples)
title("box-muller")

% generate samples by build-in function
disp("normal distributed samples by build-in function:");
samples=[];
tic
for j=1:i
  samples = [samples, normrnd(0,1,1,1)];
end
seconds = toc
figure
hist(samples)
title("build-in function")

