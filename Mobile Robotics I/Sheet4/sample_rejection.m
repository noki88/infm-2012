function x = sample_rejection(mean,var)
  do
    % standard derivation is the square root of the variance
    std=sqrt(var);
    % get a random number in range [-std,std]
    x = unifrnd(-std,std,1,1);
    % get a random number between normpdf(0,0,std)
    y = unifrnd(0,normpdf(0,0,std));
  % recect x if y is below norm(x)
  until y <= normpdf(x);
  % add the value of mean
  x = x + mean;
endfunction