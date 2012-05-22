function [x_n, y_n, theta_n]=diffdrive(x, y, theta, v_l, v_r, t, l)
  omega = (v_r - v_l) / l;
  v=(v_r + v_l) / 2;
  delta_x = v*t*cos(theta);
  delta_y = v*t*sin(theta);
  delta_theta = omega*t;
  x_n = x + delta_x;
  y_n = y + delta_y;
  theta_n = theta + delta_theta;
endfunction

% The proposed solution is not complete and correct. Few things to consider:
% You need to calculate the radius R, as shown in the slides, namely R = (l /  2)* ((v_l + v_r)/ (v_r - v_l))
% Also, one needs to explicitely consider the case when v_l = v_r This case might lead to
% a "division by 0" error and so needs to be modeled. The robot must walk in a straight path when v_l=v_r
% Additionaly, once all the above have been defined you can implement the function by simply
% following the formulas given in Slide 5, Lecture 03


