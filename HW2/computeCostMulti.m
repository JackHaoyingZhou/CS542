function J = computeCostMulti(X, y, theta)
%Compute cost for linear regression with multiple variables
%   J = COMPUTECOSTMULTI(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;


for i=1:m
    J = J +(1/(2*m))*(X(i,:)*theta-y(i))'*(X(i,:)*theta-y(i));
end



end
