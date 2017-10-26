import pandas as pd 
import os 
import random 
import matplotlib.pyplot as plt
import numpy as np

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

def autocorr():
    # get data
    dpath = os.path.join(DATA_DIR, '附录1.1.xls')
    data=pd.read_excel(dpath)
    # plot
    # print(data['黑子数'])
    plt.subplot(2,1,1)
    plt.acorr(data['黑子数'].astype('float'), maxlags=40)
    plt.title('真实黑子数自相关')

    # 随机化黑子数
    # for i in range(data.shape[0]):
    #     data.iloc[i, 1]=random.randint(0, 200)
    # x = np.random.randn(data.shape[0])
    x=[np.random.rand() for i in range(data.shape[0])]
    print(x)
    random.shuffle(x)
    plt.subplot(2,1,2)
    plt.acorr(x, maxlags=40)
    plt.title('随机黑子数自相关')
    plt.savefig('../imgs/autocorr.png')
    plt.show()

# def autocorr():
#     # get data
#     dpath = os.path.join(DATA_DIR, '附录1.1.xls')
#     data=pd.read_excel(dpath)
#     # plot
#     # print(data['黑子数'])
#     plt.subplot(2,1,1)
#     plt.acorr(data['黑子数'].astype('float'), maxlags=40)
#     plt.title('真实黑子数自相关')

#     # 随机化黑子数
#     data2=[]
#     for i in range(data.shape[0]*10):
#         data2.append(float(random.random()))
#     plt.subplot(2,1,2)
#     plt.acorr(data2, maxlags=40)
#     plt.title('随机黑子数自相关')
#     plt.savefig('../imgs/autocorr.png')
#     plt.show()

if __name__=='__main__':
    autocorr()