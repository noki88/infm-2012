function x = sample_summing(mean, var)
  x = 1/2 * sum(unifrnd(-sqrt(var),sqrt(var),1,12) + mean);
endfunction
