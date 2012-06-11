function weight = measurement_model(z, x, l)
    % Computes the observation likelihood of all particles.
    %
    % The employed sensor model is range only.
    %
    % z: set of landmark observations. Each observation contains the id of the landmark observed in z(i).id and the measured range in z(i).range.
    % x: set of current particles
    % l: map of the environment composed of all landmarks
    sigma = [0.2];
    weight = ones(size(x, 1), 1);

    if size(z, 2) == 0
        return
    endif 
    
    for i = 1:size(z, 2)
        landmark_position = [l(z(i).id).x, l(z(i).id).y];
        measurement_range = [z(i).range];
        
        for j = 1:size(x, 1)
	  dist = sqrt((x(j,1)-landmark_position(1))*(x(j,1)-landmark_position(1)) + (x(j,2)-landmark_position(2))*(x(j,2)-landmark_position(2)));
	  prob = normpdf(dist - measurement_range, 0, sigma(1));
	  weight(j) = weight(j) * prob;
	endfor

        %% TODO: use matrix operations
    endfor

    weight = weight ./ size(z, 2);
end
