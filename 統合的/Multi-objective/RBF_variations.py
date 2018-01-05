#■□■□ 応答曲面ネットワーク出力計算 □■□■#

global RBF_num

if RBF_num == 1: #f(x)-max_dataをネットワーク出力
        sample_point_fill = current_sample_point
        teacher_num =np.arange(1,current_sample_point+1)
        teacher_data = zeros(func_num,current_sample_point) 
        for func in range(func_num):
            max_data = max(sample_x_value[func,:])
            teacher_data[func,:] = sample_x_value[func,:]-max_data
        end
        
elif RBF_num == 2: #レンジを決めてネットワーク出力
        sample_point_fill = current_sample_point
        teacher_num =np.arange(1,current_sample_point+1)
        teacher_data = zeros(func_num,current_sample_point) 
        for func in range(func_num):
            max_data = max(sample_x_value[func,:])
            min_data = min(sample_x_value[func,:])
            teacher_data[func,:] = (sample_x_value[func,:]-max_data).*100./(max_data-min_data)
        end
        
elif RBF_num == 3: #制約を満たしている点のみ有効,f(x)-max_data
        [temp teacher_num] = find(total_subj_judge==0)
        sample_point_fill  = size(teacher_num,2)
        if sample_point_fill == 0
            sample_point_fill =1
            teacher_data =0
            teacher_num = 1
            r           = 1 
        else
            teacher_data   = zeros(func_num,sample_point_fill) 
            for i in range(sample_point_fill):
                teacher_data[:,i] = sample_x_value(:,teacher_num[1,i])
            end
            for func in range(func_num):
                max_data = max(teacher_data[func,:])
                teacher_data[func,:] = teacher_data[func,:]-max_data
            end
        end
        
elif RBF_num == 4: #制約を満たしていない点はプラス出力,レンジを決める
        max_data = max(sample_x_value')
        max_data = max_data'
        min_data = min(sample_x_value')
        min_data = min_data'
        max_subj_deviancy = max(sum(subj_gx,2))
        min_subj_deviancy = min(sum(subj_gx,2))
        sample_point_fill = current_sample_point
        teacher_num =np.arange(1,current_sample_point+1)
        teacher_data   = zeros(func_num,sample_point_fill) 
        for i in range(sample_point_fill):
            if total_subj_judge(1,i) == 0
                teacher_data[:,i] = (sample_x_value(:,teacher_num[1,i])-max_data).*10./(max_data-min_data)
            else
                teacher_data[:,i] = (sum(subj_gx(teacher_num[1,i],:),2)-min_subj_deviancy)*20/(max_subj_deviancy-min_subj_deviancy)
            end
        end
        
elif RBF_num == 5: #制約を満たしている点のみ有効,f(x)-max_data,レンジを決める
        [temp teacher_num] = find(total_subj_judge==0)
        sample_point_fill  = size(teacher_num,2)
        if sample_point_fill == 0
            sample_point_fill =1
            teacher_data =0*ones(func_num,1)
            teacher_num = 1
        elseif sample_point_fill == 1
            teacher_data = -10*ones(func_num,1)
            teacher_num = 1
        else
            teacher_data   = zeros(func_num,sample_point_fill) 
            for i in range(sample_point_fill):
                teacher_data[:,i] = sample_x_value(:,teacher_num[1,i])
            max_data = max(teacher_data')
            min_data = min(teacher_data')
            for func in range(func_num):
                teacher_data[func,:] = (teacher_data[func,:]-max_data[1,func])*10/(max_data[1,func]-min_data(1,func))

