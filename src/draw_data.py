import pandas as pd
import matplotlib.pyplot as plt

# Mac plt 中文字體
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

# Windows plt 中文字體
# plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 各候選人聲量長條圖
def drawPrincipalVolumeBar(dataframe: pd.DataFrame):
    dataframe['principal'].value_counts().plot(kind='bar',title='各品牌聲量長條圖', xlabel='品牌', ylabel='聲量')
    plt.show()


# 各候選人聲量折線圖(趨勢圖)
def drawPrincipalVolumeLine(dataframe: pd.DataFrame):
    # 柯文哲
    dataframe[dataframe['principal'] == '柯文哲']['time'].value_counts().sort_index().plot(kind='line', color='red')

    # 侯友宜
    dataframe[dataframe['principal'] == '侯友宜']['time'].value_counts().sort_index().plot(kind='line', color='blue')

    # 賴清德
    dataframe[dataframe['principal'] == '賴清德']['time'].value_counts().sort_index().plot(kind='line', color='green')

    plt.legend(['柯文哲', '侯友宜', '賴清德'])
    plt.title('各品牌聲量折線圖(趨勢圖)')
    plt.xlabel('日期')
    plt.ylabel('聲量')
    plt.show()

# 各候選人情緒長條圖
def drawPrincipalSentimentBar(dataframe: pd.DataFrame):
    principleSentiments = dataframe.groupby(['principal'])['sentiment'].sum()
    principleSentiments.plot(kind='bar',title='各品牌情緒長條圖', xlabel='品牌', ylabel='情緒')
    plt.show()

# 各候選人情緒折線圖(趨勢圖)
def drawPrincipalSentimentLine(dataframe: pd.DataFrame):
    # 柯文哲
    dataframe[dataframe['principal'] == '柯文哲'].groupby(['time'])['sentiment'].sum().sort_index().plot(kind='line', color='red')

    # 侯友宜
    dataframe[dataframe['principal'] == '侯友宜'].groupby(['time'])['sentiment'].sum().sort_index().plot(kind='line', color='blue')

    # 賴清德
    dataframe[dataframe['principal'] == '賴清德'].groupby(['time'])['sentiment'].sum().sort_index().plot(kind='line', color='green')

    plt.legend(['柯文哲', '侯友宜', '賴清德'])
    plt.title('各品牌情緒折線圖(趨勢圖)')
    plt.xlabel('日期')
    plt.ylabel('情緒')
    plt.show()

# 各候選人聲量與情緒比較圖(象限圖)
def drawPrincipalVolumeAndSentimentScatter(dataframe: pd.DataFrame):
    # 取得各候選人聲量與情緒
    principleSentiments = dataframe.groupby(['principal'])['sentiment'].sum().sort_index()
    principleVolumes = dataframe['principal'].value_counts().sort_index()

    # 取得x軸與y軸最大值
    minx = min(principleVolumes-100)
    maxx = max(principleVolumes+100)
    miny = min(principleSentiments-100)
    maxy = max(principleSentiments+100)

    # 繪製x軸與y軸
    plt.axhline(miny + (maxy - miny) / 2, color='black')
    plt.axvline(minx + (maxx - minx) / 2, color='black')

    # 設定x軸與y軸範圍
    plt.xlim(minx, maxx)
    plt.ylim(miny, maxy)

    # 繪製象限圖
    plt.scatter(principleVolumes, principleSentiments)
    for i in range(len(principleVolumes)):
        plt.annotate(principleVolumes.index[i], (principleVolumes[i], principleSentiments[i]))
    plt.title('各品牌聲量與情緒比較圖(象限圖)')
    plt.xlabel('聲量')
    plt.ylabel('情緒')
    plt.show()