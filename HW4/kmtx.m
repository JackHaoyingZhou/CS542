function Km = kmtx(X,Xt,sigma)
%% calculate the kernel matrix for input X

%% preset
% sigma = 1;  % take the sigma of gaussian kernel to be 1
m = size(X,1);
n = size(Xt,1);
Km = zeros(m,n);
%% calculate the matrix

for i = 1:m
    for j = 1:n
        Km(i,j) = gaussianKernel(X(i,:),Xt(j,:),sigma);
    end
end

end