function mean_pos = mean_position(particles, weights)
    % Returns a single estimate of filter state based on the particle cloud.
    %
    % particles (M x 3): set of M particles to sample from. Each row contains a state hypothesis of dimension 3 (x, y, theta).
    % weights (M x 1): weights of the particles. Each row contains a weight.

    % initialize
    mean_pos = zeros(1,3);

    %% TODO: compute mean_pos    
    mean_pos(1) = sum(particles(:,1) .* weights);
    mean_pos(2) = sum(particles(:,2) .* weights);
    mean_pos(3) = average_angle(particles(:,3) .* weights);
end
