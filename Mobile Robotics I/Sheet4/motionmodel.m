function x_t1 = motionmodel(x_t, u_t, alpha)
  delta_rot1 = u_t(1) + sample_boxmuller(0, alpha(1)*abs(u_t(1)) + alpha(2)*u_t(3));
  delta_trans = u_t(3) + sample_boxmuller(0, alpha(3)*u_t(3) + alpha(4)*(abs(u_t(1))+abs(u_t(2))));
  delta_rot2 = u_t(2) + sample_boxmuller(0, alpha(1)*abs(u_t(2)) + alpha(2)*u_t(3));
  
  x = x_t(1) + delta_trans * cos(x_t(3)+delta_rot1);
  y = x_t(2) + delta_trans * sin(x_t(3)+delta_rot1);
  theta = x_t(3) + delta_rot1 + delta_rot2;
  
  x_t1 = [x, y, theta];
endfunction
  