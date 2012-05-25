function x = sample_rejection(mean,var)
% 
% Can be computed before the loop:
%
std=sqrt(var);

    do
    % standard derivation is the square root of the variance
    % get a random number in range [-std,std]
   
    %
    %
    % The graph from your solution does not look like a gaussian
    % You can obtain better results, if you use a bigger range: 
    % (More about this in the exercise)
    %
    %
    x = unifrnd(-3*std,3*std);
    % get a random number between normpdf(0,0,std)
    y = unifrnd(0,normpdf(0,0,std));
  % recect x if y is below norm(x)
  
  %
  % You need the same parameters here as above!
  %
  until y <= normpdf(x,0,std);
  % add the value of mean
  x = x + mean;
endfunction