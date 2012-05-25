function x = sample_boxmuller(mean,var)
  % get first random number between [0,1] (unifromly distributed)
  
  %
  %You get a twice as fast implementation if you draw a u vector
  u = unifrnd(0,1,2,1);
  %
  % (You could also use rand(), which is even faster than unifrand)
  %
  % u = [rand() rand()];
  
  x = cos(2*(pi)*u(1))*sqrt(-2*log(u(2)));
  % add the value of mean
  
  %
  % Need to consider the variance:
  %  
  x = x*sqrt(var) + mean;
endfunction 
