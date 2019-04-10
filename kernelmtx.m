function K = kernelmtx(X,sigma)
%% calculate the kernel matrix for input X

%% preset
%sigma = 1;  % take the sigma of gaussian kernel to be 1
m = size(X,1);
K = zeros(m,m);
%% calculate the matrix

for i = 1:m
    for j = 1:m
        K(i,j) = gaussianKernel(X(i,:),X(j,:),sigma);
    end
end

end





