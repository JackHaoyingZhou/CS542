function [theta, J_old] = GDMulti(X, y, theta, alpha, num_iters)
%Performs gradient descent to learn theta
%   theta = GDMulti(x, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_old = zeros(num_iters, 1);
temp = zeros(length(theta),1);

for iter = 1:num_iters



    Jac = zeros(length(theta),1);
    for j = 1:m
        Jac = Jac + (1/m)*(X(j,:)*theta-y(j))*X(j,:)';
    end
    temp = theta;
    theta = theta - alpha*Jac;
    if theta == temp
        break
    end


    % Save the cost J in every iteration    
    J_old(iter) = computeCostMulti(X, y, theta);

end

end
