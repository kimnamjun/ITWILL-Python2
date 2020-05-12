import pandas as pd
import statistics
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

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

loc = [[],[]]
loc[0].append(pd.DataFrame({'tem_in': plant1_train.iloc[:,1], 'tem_coil': plant1_train.iloc[:,3],
                      'hum': plant1_train.iloc[:,2], 'cond': plant1_train.iloc[:,12]}).dropna())
loc[0].append(pd.DataFrame({'tem_in': plant1_train.iloc[:,4], 'tem_coil': plant1_train.iloc[:,6],
                      'hum': plant1_train.iloc[:,5], 'cond': plant1_train.iloc[:,13]}).dropna())
loc[0].append(pd.DataFrame({'tem_in': plant1_train.iloc[:,7], 'tem_coil': plant1_train.iloc[:,9],
                      'hum': plant1_train.iloc[:,8], 'cond': plant1_train.iloc[:,14]}).dropna())
loc[1].append(pd.DataFrame({'tem_in': plant2_train.iloc[:,1], 'tem_coil': plant2_train.iloc[:,3],
                      'hum': plant2_train.iloc[:,2], 'cond': plant2_train.iloc[:,12]}).dropna())
loc[1].append(pd.DataFrame({'tem_in': plant2_train.iloc[:,4], 'tem_coil': plant2_train.iloc[:,6],
                      'hum': plant2_train.iloc[:,5], 'cond': plant2_train.iloc[:,13]}).dropna())
loc[1].append(pd.DataFrame({'tem_in': plant2_train.iloc[:,7], 'tem_coil': plant2_train.iloc[:,9],
                      'hum': plant2_train.iloc[:,8], 'cond': plant2_train.iloc[:,14]}).dropna())

yes = list()
no = list()
for i in range(2):
    for j in range(3):
        a, b = calc_cond(loc[i][j]['tem_in'], loc[i][j]['tem_coil'], loc[i][j]['hum'], loc[i][j]['cond'])
        yes.extend(a)
        no.extend(b)
        print(len(a)+len(b) // len(a))
        print(round(statistics.mean(a), 4), round(statistics.mean(b), 4))
        print(round(statistics.stdev(a), 4), round(statistics.stdev(b), 4))

print()
print(len(yes), len(no))
print(sum(yes), sum(no))
print(statistics.mean(yes), statistics.mean(no))
print(statistics.stdev(yes), statistics.stdev(no))

print('------------------------------------------------------------------------------------------')

for i in range(2):
    print(f'plant {i + 1}')
    for j in range(3):
        print(f'location {j + 1}')
        x_train, x_test, y_train, y_test = train_test_split(loc[i][j].iloc[:,:3], loc[i][j].iloc[:,3], test_size=0.3, random_state=123)
        model = LinearRegression().fit(x_train, y_train)
        y_pred = model.predict(x_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print(mse)
        print(r2)
        print(abs(y_test-y_pred).mean())
        print()