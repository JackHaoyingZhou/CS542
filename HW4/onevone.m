function [st, sn] = onevone(T,m,n,K,Kt,k)
%% find alpha
No = find(T == m | T == n);
Tt = T(No);
M = zeros(size(Tt));

Ko = K(No,No);

% one vs rest classifier
for i  = 1: length(Tt)
    if Tt(i) == m
        M(i) = 1;
    else
        M(i) = -1;
    end
end
% set the parameters of quadratic programming
Td = diag(M);
H = Td*Ko*Td;
f = -ones(size(M));
lb = zeros(size(M));
Aeq = M';
beq = 0;

% solve for alpha
alpha = quadprog(H,f,[],[],Aeq,beq,lb,[]);

%% classification 
% find support vectors
Nu = find(alpha>1e-9);
% % calculate b

Ks = zeros(length(Nu),1);
Kr = K(Nu,Nu);
alphaNu = alpha(Nu);
MNu = M(Nu);
for j = 1:length(Nu)
    Ks(j) = M(Nu(j)) - sum(alphaNu.*MNu.*Kr(:,j));
end

b = sum(Ks)/length(Ks);

%% calculate y, AKA sn

% for i = 1:m
%         Kt(i) = gaussianKernel(X(i,:),Xt,sigma);
% end
Kp = Kt(No,:);
st = sum(alpha.*M.*Kp(:,k)) + b;
if st > 0
    sn = m;
else
    sn = n;
end

end




