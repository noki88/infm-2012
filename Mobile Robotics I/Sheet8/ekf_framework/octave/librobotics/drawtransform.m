%DRAWTRANSFORM Illustrates a spatial relationship.
%   DRAWTRANSFORM(XS,XE,SHAPE,LABEL,COLOR) draws a nice looking
%   curved arrow from location XS (3x1) to XE (3x1) and labels
%   it with LABEL (Matlab text syntax). COLOR is a [r g b]-vector
%   or a Matlab color string such as 'r' or 'g'. SHAPE controls
%   the shape of the curve: '/' for a S-shape, '\' for a Z-shape,
%   '(' for a left arc and ')' for a right arc.
%
%   H = DRAWTRANSFORM(...) returns a column vector of handles to
%   all graphic objects of the drawing. Remember that not all
%   graphic properties apply to all types of graphic objects.
%
%   See also DRAWREFERENCE, PLOT.

% v.1.0, 09.11.02, Kai Arras, ASL-EPFL
% v.1.1, 04.12.03, Kai Arras, CAS-KTH: shapes introduced

function h = drawtransform(x1,x2,shape,label,color);

% Constants
FILLED = 1;           % filled arrow head by default
ASIZE  = 0.08;        % default arrow head size
FSIZE  = 13;          % label font size
NPTS   = 50;          % number of points for the spline
TPFRAC = 0.2;         % fractional dist. of tangential points
TPADEV = pi/20;       % angle deviation of tang. points from phi
OFFST  = 0.12;        % default offset for spline start and end

% Draw spline
xs  = x1(1); ys = x1(2);      % orientation not used
xe  = x2(1); ye = x2(2);      % orientation not used
phi = atan2(ye-ys, xe-xs);
d   = norm([ye-ys, xe-xs]);
xs = xs + OFFST*cos(phi);
ys = ys + OFFST*sin(phi);
xe = xe - OFFST*cos(phi);
ye = ye - OFFST*sin(phi);

switch shape
  case '/',
    xst = xs + d*TPFRAC*cos(phi+TPADEV);
    yst = ys + d*TPFRAC*sin(phi+TPADEV);
    xet = xe - d*TPFRAC*cos(phi+TPADEV);
    yet = ye - d*TPFRAC*sin(phi+TPADEV);
  case '\',
    xst = xs + d*TPFRAC*cos(phi-TPADEV);
    yst = ys + d*TPFRAC*sin(phi-TPADEV);
    xet = xe - d*TPFRAC*cos(phi-TPADEV);
    yet = ye - d*TPFRAC*sin(phi-TPADEV);
  case '(',
    xst = xs + d*TPFRAC*cos(phi+TPADEV);
    yst = ys + d*TPFRAC*sin(phi+TPADEV);
    xet = xe - d*TPFRAC*cos(phi-TPADEV);
    yet = ye - d*TPFRAC*sin(phi-TPADEV);
  case ')',
    xst = xs + d*TPFRAC*cos(phi-TPADEV);
    yst = ys + d*TPFRAC*sin(phi-TPADEV);
    xet = xe - d*TPFRAC*cos(phi+TPADEV);
    yet = ye - d*TPFRAC*sin(phi+TPADEV);
  otherwise
    error('drawtransform: Unsupported shape');
end;

% Turn to k*45 deg since spline must have distinct values in x,y
p  = [xs xst xet xe; ys yst yet ye];
R  = [cos(pi/4-phi) -sin(pi/4-phi); sin(pi/4-phi) cos(pi/4-phi)];
p  = R*p;
xx = min(p(1,:)):(max(p(1,:))-min(p(1,:)))/NPTS:max(p(1,:));
yy = spline(p(1,:),p(2,:),xx);
p  = inv(R)*[xx; yy];
h1 = plot(p(1,:),p(2,:),'Color',color);

% Draw arrow head
h2 = drawarrow(p(1:2,end-1),p(1:2,end),FILLED,ASIZE,color);

% Display text
h3 = text(mean(p(1,:)),mean(p(2,:)),label,'FontSize',FSIZE,'Color',color);
h = cat(1,h1,h2,h3);