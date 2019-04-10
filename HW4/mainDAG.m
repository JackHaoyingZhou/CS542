close all
clear all
clc
load('MNIST_data.mat')

X = train_samples;
T = train_samples_labels;
Xtest = test_samples;
Ttest = test_samples_labels;
% Nl = max(T) - min(T) + 1;
% Num = Nl*(Nl - 1)/2;


%% calculation

% s = zeros(size(Xtest,1),10);

sigma = 0.4;

K = kernelmtx(X,sigma);

Km = kmtx(X,Xtest,sigma);

%% voting strategy

s = zeros(size(Xtest,1),1);
sn = zeros(size(Xtest,1),1);
for kn = 1:size(Ttest)
    i = 0;
    j = 9;
    while i ~= j
        sn(kn) = onevone(T,i,j,K,Km,kn);
        if sn(kn) > 0
            j = j - 1;
        else
            i = i + 1;
        end
    end
    s(kn) = i;
    clc;
    disp(kn);
end
%% predict

A = (s==Ttest);

accuracy = sum(A)/length(A);

cfmtx = confusionchart(Ttest,s); %Ttest is original and L is predicted


