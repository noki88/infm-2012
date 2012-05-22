pos_initial = [1.5, 2.0, (pi)/2];
c1 = [0.3, 0.3, 3]
c2 = [0.1, -0.1, 1]
c3 = [0.2, 0,  2]
l = 0.5

[p1_x, p1_y, p1_theta] = diffdrive(pos_initial(1), pos_initial(2), pos_initial(3), c1(1), c1(2), c1(3), l)
[p2_x, p2_y, p2_theta] = diffdrive(p1_x, p1_y, p1_theta, c2(1), c2(2), c2(3), l)
[p3_x, p3_y, p3_theta] = diffdrive(p2_x, p2_y, p2_theta, c3(1), c3(2), c3(3), l)

% This is correct!
