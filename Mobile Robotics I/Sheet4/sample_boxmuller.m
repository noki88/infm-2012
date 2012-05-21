function x = sample_boxmuller(mean,var)
  % get first random number between [0,1] (unifromly distributed)
  u1 = unifrnd(0,1,1,1);
  % get second random number between [0,1] (unifromly distributed)
  u2 = unifrnd(0,1,1,1);
  % calculate x
  x = cos(2*(pi)*u1)*sqrt(-2*log(u2));
  % add the value of mean
  x = x + mean;
endfunction 
