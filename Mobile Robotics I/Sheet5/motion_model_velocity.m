function p = motion_model_velocity(x_t2, u_t2, x_t1, alpha)
  u = 0.5  * ((x_t1(1) - x_t2(1)) * cos(x_t1(3)) + (x_t1(2) - x_t2(2)) * sin(x_t1(3))) / ((x_t1(2) - x_t2(2)) * cos(x_t1(3)) + (x_t1(1) - x_t2(1)) * sin(x_t1(3)))
  x_star = 0.5 * (x_t1(1) + x_t2(1)) + u * (x_t1(2) - x_t2(2))
  y_star = 0.5 * (x_t1(2) + x_t2(2)) + u * (x_t2(1) - x_t1(1))
  r_star = sqrt((x_t1(1)-x_star)*(x_t1(1)-x_star) + (x_t1(2)-y_star)*(x_t1(2)-y_star))
  delta_omega = atan2(x_t2(2) - y_star, x_t2(1) - x_star) - atan2(x_t1(2) - y_star, x_t1(1) - x_star)
  v_noise = delta_omega / u_t2(3) * r_star
  w_noise = delta_omega / u_t2(3)
  gamma_noise = (x_t2(3) - x_t1(3)) / u_t2(3) - w_noise
  p1 = normpdf(u_t2(1) - v_noise, 0, alpha(1)*abs(u_t2(1)) + alpha(2)*abs(u_t2(2)))
  p2 = normpdf(u_t2(2) - w_noise, 0, alpha(3)*abs(u_t2(1)) + alpha(4)*abs(u_t2(2)))
  p3 = normpdf(gamma_noise, 0, alpha(5)*abs(u_t2(1)) + alpha(6)*abs(u_t2(2)))
  p = p1*p2*p3
endfunction