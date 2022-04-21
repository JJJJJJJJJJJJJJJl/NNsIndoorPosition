for noise=10:10:90
    n = 360;
    k=200;
    
    data = [];
    j=1;
    for i=1:1:n
        d=genDataset(k,i,noise);
        data = [data; d];
    endfor
    file = ["train_data_" num2str(noise) "noise.csv"];
    csvwrite(file,data);

    data = [];
    j=1;
    for i=1:1:n
        d=genDataset(k,i,noise);
        data = [data; d];
    endfor
    file = ["test_data_" num2str(noise) "noise.csv"];
    csvwrite(file,data);
    disp(file);
endfor