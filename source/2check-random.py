import pandas as pd 
import os 
import random 
import matplotlib.pyplot as plt

#设置中文字体
plt.rcParams['font.sans-serif']=['SimHei']

DATA_DIR='../data/sample/'
#固定随机数， 以便每次生成相同的随机数
random.seed(10)
def random_sequence_chart():
    dpath = os.path.join(DATA_DIR, '附录1.1.xls')
    data=pd.read_excel(dpath)
    for i in range(data.shape[0]):
        data.iloc[i, 1]=random.randint(20, 200)

    print(data)
    fig, ax = plt.subplots()
    ax.plot(data['年份'], data['黑子数'])
    ax.set(xlabel='年份', ylabel='黑子数', title='随机生成的黑子数')
    plt.savefig('../imgs/random-sunspots.png')

    plt.show()

def sequence_chart():
    dpath = os.path.join(DATA_DIR, '附录1.1.xls')
    data=pd.read_excel(dpath)
    fig, ax = plt.subplots()
    ax.plot(data['年份'], data['黑子数'])
    ax.set(xlabel='年份', ylabel='黑子数', title='黑子数')
    plt.savefig('../imgs/sunspots.png')
    plt.show()

if __name__=='__main__':
    random_sequence_chart()