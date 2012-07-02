% grid resolution
grid_resolution=10;

% map length
map_length=200;

% measurements
measurements=[101, 82, 91, 112, 99, 151, 96, 85, 99, 105];

% initial belief values
m=0.5*ones(1,21);

% prior
prior=0.5;

% probability that the cell is occupied if the cell distance is smaller than the measured distance
p_free = 0.3;

% probability that the cell is occupied if the cell is behind the measured distance
p_occ = 0.6;

% do not update cells behind the measured + this distance
dist_behind=20;

% cell coordinates
c=[0:grid_resolution:map_length];

% loop over all measurements
for i = 1:size(measurements,2)
  % p: probability that a cell is occupied given the measurement
  p = zeros(1,21);
  % loop over all cells
  for j = 1:21
  disp("cell:"), disp(c(j))
  disp("measurement:"), disp(measurements(i))
    if c(j) < measurements(i)
      % cell is free if measured distance is greater than the cell distance
      p(j) = p_free;
      disp("--> free")
    elseif measurements(i) > c(j) - dist_behind 
      % cell is meant to be occupied
      p(j) = p_occ;
      disp("--> occ")
    else
      % cell is more than 20cm behind the measurement, i.e. no update
      disp("--> not updated")
      continue;
    endif
    m(j) = 1/(1 + (1-p(j))/p(j) * prior/(1-prior) * (1-m(j))/m(j) );
  endfor
endfor

plot(c,m);