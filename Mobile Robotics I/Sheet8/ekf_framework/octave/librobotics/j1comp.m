%J1COMP First Jacobian of the compound operator.
%   J = J1COMP(XI,XJ) returns the Jacobian matrix of the 2D composition
%   of XI and XJ derived with respect to the first operand. All X's are
%   3x1-vectors, J is a 3x3 matrix.
%
%   See also J2COMP, JINV, COMPOUND, ICOMPOUND.

% v.1.0, 30.11.02, Kai Arras, ASL-EPFL


function J1 = j1comp(xij,xjk);

j13 = -xjk(1)*sin(xij(3)) - xjk(2)*cos(xij(3));
j23 =  xjk(1)*cos(xij(3)) - xjk(2)*sin(xij(3));

J1 = [1, 0, j13;
      0, 1, j23;
      0, 0,  1];
