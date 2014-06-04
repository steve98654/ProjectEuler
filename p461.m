
n = 200;

objfun = @(k)(f(n,k(1)) + f(n,k(2)) + f(n,k(3)) + f(n,k(4)) - pi)^2;
%fungrd = @(k)(2*(f(n,k(1)) + f(n,k(2)) + f(n,k(3)) + f(n,k(4)) - pi));

x0 = [226 89 75 6.4];

x = fminsearch(objfun,x0)

%x0 = [226, 89, 75, 6.3];
%fmincon(objfun, x0, [], [], [], [], [0 0 0 0], [1e4 1e4 1e4 1e4])