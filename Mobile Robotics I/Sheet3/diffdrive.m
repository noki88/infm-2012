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

