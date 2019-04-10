close all
clear all
clc
load('MNIST_data.mat')

X = train_samples;
T = train_samples_labels;
Xtest = test_samples;
Ttest = test_samples_labels;


%% calculation

s = zeros(size(Xtest,1),10);

sigma = 0.4;

K = kernelmtx(X,sigma);

Km = kmtx(X,Xtest,sigma);

for j = 1:length(Ttest)
    for i = 0:9
        s(j,i+1) = onevrest(T,K,Km,j,i);
        clc;
        disp(i);
        disp(j);
    end
end


%% predict

L = zeros(size(s,1),1);

for i = 1:size(s,1)
    L(i) = find(s(i,:)==max(s(i,:)))-1; 
end

A = (L==Ttest);

accuracy = sum(A)/length(A);

cfmtx = confusionchart(Ttest,L);