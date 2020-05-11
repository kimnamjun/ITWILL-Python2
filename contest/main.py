import pandas as pd

def calc_cond(tem_coil, tem_in, hum, cond):
    yes = list()
    no = list()
    diff = tem_coil - tem_in

    for idx, val in enumerate(cond):
        if val > 0.5:
            yes.append(diff.iloc[idx])
        else:
            no.append(diff.iloc[idx])
    return yes, no

path = "../../data/"  # 파일이 들어 있는 디렉토리로 변경
plant1_train = pd.read_csv(path + 'plant1_train.csv', index_col=0, header=0)
plant2_train = pd.read_csv(path + 'plant2_train.csv', index_col=0)
plant_test = pd.read_csv(path + 'plant_test.csv', index_col=0)
temin11 = plant1_train.iloc[:,1]
temco11 = plant1_train.iloc[:,3]
hum11 = plant1_train.iloc[:,2]
cond11 = plant1_train.iloc[:,12]
print(type(cond11))

print(plant1_train.columns)
print(temin11, temco11, hum11, cond11)

yes, no = calc_cond(temco11, temin11, hum11, cond11)
print(len(yes), len(no))
print(sum(yes)/len(yes), sum(no)/len(no))