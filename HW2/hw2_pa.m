%% Initialization
clear all;
close all;
clc;
fprintf('Loading data ...\n');

%% Load data
input = load('detroit.mat');
X = input.data(:,1:9);
y = input.data(:,10);
m = length(y);

fprintf('Loaded, program paused. Press enter to continue.\n');
pause;

%% Normalize data

fprintf('Normalizing Features ...\n');

[X mu sigma] = Normalize(X);

% Add intercept term to X
X = [ones(m,1) X];

%% Gradient Descent

fprintf('Running gradient descent...\n');

% Choose some alpha value
alpha = 0.1;
num_iters = 100;

% Initialize theta and run gradient descent
theta = zeros(size(X,2),1);
[theta, J_old] = GDMulti(X, y, theta, alpha, num_iters);

% Plot the convergence graph
figure
plot(1:numel(J_old), J_old, '-b', 'LineWidth', 2);
xlabel('Number of iterations');
ylabel('Cost J');
grid on

% Display gradient descent's result
fprintf('Theta computed from gradient descent:\n');
fprintf(' %f \n', theta);
fprintf('\n');