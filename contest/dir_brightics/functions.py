import pandas as pd
from datetime import datetime, timedelta


def read_csv(path, filename, encoding='CP949'):
    # CSV 파일 읽기
    data = pd.read_csv(path + '/' + filename, encoding=encoding)

    # 자료형 변경
    data.columns = [d.lower() for d in data.columns]
    data['sell_date'] = [datetime.strptime(d, "%Y-%m-%d") for d in data['sell_date']]

    # 주말 제외
    data['weekday'] = data['sell_date'].dt.dayofweek
    data = data[data['weekday'] < 5]
    return data


def create_table(meal_data):
    data = meal_data.groupby(['sell_date','brand'])
    table = pd.DataFrame({'today': data['quantity'].sum()})
    table = table.reset_index()
    return table


def create_table2(meal_data):  # 하다 버린거
    data = meal_data.groupby(['sell_date','brand'])

    table = pd.DataFrame({'today': data['quantity'].sum()})
    table['after7'] = None
    temp = list()
    for idx, row in enumerate(table.index):
        if idx < 30:
            print((row[0] + timedelta(days=7)).strftime("%Y-%m-%d"), row[1])
            print(row)
            if row[0] + timedelta(days=7) in table.index:
                # table.iloc[idx,1] = (row[0] + timedelta(days=7)).strftime("%Y-%m-%d")
                x = (row[0] + timedelta(days=7))
                table.loc[row, 'after7'] = table.loc[(x, row[1]),'after7']
    table = table.reset_index()
    return table

def test(table):
    for idx in table.index[:-65]:
        nxt = idx + 65
        print(table.iloc[idx, 0], table.iloc[nxt, 0], ' // ', table.iloc[idx, 1], table.iloc[nxt, 1])
        if table.iloc[idx, 0] != table.iloc[nxt, 0] or table.iloc[idx, 1] != table.iloc[nxt, 1]:
            print('idx: ',idx)