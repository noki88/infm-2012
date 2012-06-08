function x_t2 = motion(u_t2, x_t1)
  x_t2 = motion_noisefree(u_t2, x_t1);
endfunction

function x_t2 = motion_noisefree(u_t2, x_t1)
  v = u_t2(1);
  w = u_t2(2);
  t = u_t2(3);
  x = x_t1(1) - v/w * sin(x_t1(3)) + v/w * sin(x_t1(3) + w*t);
  y = x_t1(2) + v/w * cos(x_t1(3)) - v/w * cos(x_t1(3) + w*t);
  omega = x_t1(3) + t*w;
  x_t2 = [x, y, omega];
endfunction

% octave:5> motion([0.1,0.1,3],[0,0,(pi)/2])
% ans =
%
%  -0.044664   0.295520   1.870796