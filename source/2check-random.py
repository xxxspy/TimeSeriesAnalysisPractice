import pandas as pd 
import os 
import random 
import matplotlib.pyplot as plt
import numpy as np

#设置中文字体
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
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
    from pandas.plotting import autocorrelation_plot
    # get data
    dpath = os.path.join(DATA_DIR, '附录1.1.xls')
    data=pd.read_excel(dpath)
    # plot
    # print(data['黑子数'])
    fig, axes=plt.subplots(nrows=2, ncols=1)
    autocorrelation_plot(data['黑子数'], ax=axes[0])
    axes[0].set_title('真实黑子数')

    # 随机化黑子数
    x=[random.randint(1, 200) for i in range(data.shape[0])]
    autocorrelation_plot(x, ax=axes[1])
    axes[1].set_title('随机黑子数')
    plt.savefig('../imgs/autocorr.png')
    plt.show()

def boxpierce_test():
    '''计算box pierce 和 box ljung统计量'''
    from statsmodels.sandbox.stats.diagnostic import acorr_ljungbox
    dpath = os.path.join(DATA_DIR, '附录1.1.xls')
    data=pd.read_excel(dpath)
    x=data['黑子数']
    qljungbox, pval, qboxpierce, pvalbp=acorr_ljungbox(x, boxpierce=True)
    for i in range(len(pval)):
        print('真实数据：qljungbox, pval, qboxpierce, pvalbp:',qljungbox[i], pval[i], qboxpierce[i], pvalbp[i])
    fig, axes = plt.subplots(2,2)
    axes[0,0].plot(qljungbox, label='qljungbox');axes[0,0].set_ylabel('真实-Q')
    axes[0,0].plot(qboxpierce, label='qboxpierce')

    axes[0,1].plot(pval, label='pval');axes[0,1].set_ylabel('P')
    axes[0,1].plot(pvalbp, label='pvalbp')

    x=[random.randint(1, 200) for i in range(data.shape[0])]
    qljungbox, pval, qboxpierce, pvalbp=acorr_ljungbox(x, boxpierce=True)
    axes[1,0].plot(qljungbox, label='qljungbox');axes[1,0].set_ylabel('随机-Q')
    axes[1,0].plot(qboxpierce, label='qboxpierce')

    axes[1,1].plot(pval, label='pval');axes[1,1].set_ylabel('P')
    axes[1,1].plot(pvalbp, label='pvalbp')
    axes[0,0].legend()
    axes[0,1].legend()
    axes[1,0].legend()
    axes[1,1].legend()
    plt.savefig('../imgs/boxpierce_test.png')
    plt.show()
    print('随机数据：qljungbox, pval, qboxpierce, pvalbp:',qljungbox, pval, qboxpierce, pvalbp)



if __name__=='__main__':
    boxpierce_test()