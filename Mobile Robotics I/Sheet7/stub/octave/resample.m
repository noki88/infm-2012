function new_particles = resample(particles, weights)
    % Returns a new set of particles obtained by performing
    % stochastic universal sampling.
    %
    % particles (M x D): set of M particles to sample from. Each row contains a state hypothesis of dimension D.
    % weights (M x 1): weights of the particles. Each row contains a weight.
    new_particles = [];

    M = size(particles, 1);
    %% TODO: complete this stub
    
    c = zeros(M,1);

    c(1) = weights(1);
    for i = 2:M
      c(i) = c(i-1) + weights(i);
    endfor

    i = 1;
    u1 = unifrnd(0, 1/M);
    for j = 1:M
      while (u1 > c(i))
        i++;
      endwhile
      new_particles = [new_particles; particles(i,:)];
      u1 = u1 + 1/M;
    endfor
  
end
