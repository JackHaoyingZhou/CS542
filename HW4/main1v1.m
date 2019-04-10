close all
clear all
clc
load('MNIST_data.mat')

X = train_samples;
T = train_samples_labels;
Xtest = test_samples;
Ttest = test_samples_labels;
Nl = max(T) - min(T) + 1;
Num = Nl*(Nl - 1)/2;


%% calculation

% s = zeros(size(Xtest,1),10);

sigma = 0.4;

K = kernelmtx(X,sigma);

Km = kmtx(X,Xtest,sigma);

%% voting strategy

s = zeros(size(Xtest,1),Num);
sk = zeros(size(Xtest,1),Num);
for l = 1:length(Ttest)
    disp(l);
    sl = 1;
    for i = 0:9
        for j = 0:9
            if i > j
                [sk(l,sl), s(l,sl)] = onevone(T,i,j,K,Km,l);
                sl = sl + 1;
            end
        end
    end
    clc;
end
%% predict


La = zeros(size(s,1),Nl);
for j = 1:size(s,1)
    for i = 0:9
        La(j,i+1) = length(find(s(j,:) == i));
    end
end

L = zeros(size(s,1),1);

for i = 1:size(s,1)
    if length(find(La(i,:)==max(La(i,:)))) > 1
        a = length(find(La(i,:)==max(La(i,:))));
        sa = find(La(i,:)==max(La(i,:)));
        if a == 2
            [L0, L(i)] = onevone(T,sa(1)-1,sa(2)-1,K,Km,i);
        elseif a == 3
            [L1,L12] = onevone(T,sa(1)-1,sa(2)-1,K,Km,i);
            [L2,L13] = onevone(T,sa(1)-1,sa(3)-1,K,Km,i);
            [L3,L23] = onevone(T,sa(2)-1,sa(3)-1,K,Km,i);
            if L12 == L13
                L(i) = L12;
            elseif L12 == L23
                L(i) = L12;
            elseif L13 == L23
                L(i) = L13;
            else
                Lva = [L1,L2,L3];
                Lva = abs(Lva);
                chsnum = find(Lva == max(Lva));
                L(i) = sa(chsnum) - 1;
            end
        else
            chsnum = randi([1,a]);
            L(i) = sa(chsnum) - 1;
        end   
    clc;
    else
        L(i) = find(La(i,:)==max(La(i,:))) - 1;
    end
end


A = (L==Ttest);

accuracy = sum(A)/length(A);

cfmtx = confusionchart(Ttest,L); %Ttest is original and L is predicted


