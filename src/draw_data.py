import pandas as pd
import matplotlib.pyplot as plt

# Mac plt 中文字體
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

# Windows plt 中文字體
# plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 各候選人聲量長條圖
def drawPrincipalVolumeBar(dataframe: pd.DataFrame):
    dataframe['principal'].value_counts().plot(kind='bar',title='各候選人聲量長條圖', xlabel='候選人', ylabel='聲量')
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
    plt.title('各候選人聲量折線圖(趨勢圖)')
    plt.xlabel('日期')
    plt.ylabel('聲量')
    plt.show()

# 各候選人情緒長條圖
def drawPrincipalSentimentBar(dataframe: pd.DataFrame):
    principleSentiments = dataframe.groupby(['principal'])['sentiment'].mean()
    principleSentiments.plot(kind='bar',title='各候選人情緒長條圖', xlabel='候選人', ylabel='情緒')
    plt.show()

# 各候選人情緒折線圖(趨勢圖)
def drawPrincipalSentimentLine(dataframe: pd.DataFrame):
    # 柯文哲
    dataframe[dataframe['principal'] == '柯文哲'].groupby(['time'])['sentiment'].mean().sort_index().plot(kind='line', color='red')

    # 侯友宜
    dataframe[dataframe['principal'] == '侯友宜'].groupby(['time'])['sentiment'].mean().sort_index().plot(kind='line', color='blue')

    # 賴清德
    dataframe[dataframe['principal'] == '賴清德'].groupby(['time'])['sentiment'].mean().sort_index().plot(kind='line', color='green')

    plt.legend(['柯文哲', '侯友宜', '賴清德'])
    plt.title('各候選人情緒折線圖(趨勢圖)')
    plt.xlabel('日期')
    plt.ylabel('情緒')
    plt.show()

# 各候選人聲量與情緒比較圖(象限圖)
def drawPrincipalVolumeAndSentimentScatter(dataframe: pd.DataFrame):
    # 取得各候選人聲量與情緒
    principleSentiments = dataframe.groupby(['principal'])['sentiment'].mean().sort_index()
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
    plt.title('各候選人聲量與情緒比較圖(象限圖)')
    plt.xlabel('聲量')
    plt.ylabel('情緒')
    plt.show()

# 各候選人與關鍵字聲量比較折現圖
def drawPrincipalCustomKeywordLine(dataframe: pd.DataFrame):
    
    # 複製資料避免影響原資料
    copyDataframe = dataframe.copy()

    # 自訂關鍵字
    customKeywords = ["賄選", "台獨", "民調", "造勢", "連任", "總統大選", "黨內聲量", "民意聲量", "網路聲量"]

    # 為每列標註是否包含自訂關鍵字，有的話標註含有的關鍵字
    for customKeyword in customKeywords:
        copyDataframe[customKeyword] = copyDataframe['content'].str.contains(customKeyword)

    # 取得各候選人與關鍵字聲量
    principleCustomKeywordVolumes = copyDataframe.groupby(['principal'])[customKeywords].sum().sort_index()

    # 候選人名單
    principles = ['柯文哲', '侯友宜', '賴清德']

    # 繪製折線圖
    for principal in principles:
        plt.plot(customKeywords, principleCustomKeywordVolumes.loc[principal], marker='o')
    plt.legend(principles)
    plt.title('各候選人與關鍵字聲量比較折線圖')
    plt.xlabel('候選人')
    plt.ylabel('聲量')
    plt.show()

# 各候選人與關鍵字情緒之知覺圖
def drawPrincipalCustomKeywordSentimentScatter(dataframe: pd.DataFrame):
    
    # 需要先將資料複製出來，避免影響原資料
    copyDataframe = dataframe.copy()

    # 自訂關鍵字
    customKeywords = ["賄選", "台獨", "民調", "造勢", "連任", "總統大選", "黨內聲量", "民意聲量", "網路聲量"]

    # 需要做一個新的dataFrame，列出每個候選人與關鍵字的情緒分數
    principleCustomKeywordSentiments = pd.DataFrame(columns=['principal', 'keyword', 'sentiment'])
    for customKeyword in customKeywords:
        principleCustomKeywordSentiments = pd.concat([principleCustomKeywordSentiments, copyDataframe[copyDataframe['content'].str.contains(customKeyword)][['principal', 'sentiment']].assign(keyword=customKeyword)], ignore_index=True)

    # 取得各候選人與關鍵字情緒
    principleCustomKeywordSentiments = principleCustomKeywordSentiments.groupby(['principal', 'keyword'])['sentiment'].mean().sort_index().unstack()

    # 填補NaN值
    principleCustomKeywordSentiments = principleCustomKeywordSentiments.fillna(0)
    print(principleCustomKeywordSentiments)

    # 繪製象限圖
    for customKeyword1 in principleCustomKeywordSentiments.columns:
        for customKeyword2 in principleCustomKeywordSentiments.columns:
            if(customKeyword1 == customKeyword2):
                continue
            # 取得x軸與y軸最大值
            minx = min(principleCustomKeywordSentiments[customKeyword1]-100)
            maxx = max(principleCustomKeywordSentiments[customKeyword1]+100)
            miny = min(principleCustomKeywordSentiments[customKeyword2]-100)
            maxy = max(principleCustomKeywordSentiments[customKeyword2]+100)

            # 繪製x軸與y軸
            plt.axhline(miny + (maxy - miny) / 2, color='black')
            plt.axvline(minx + (maxx - minx) / 2, color='black')

            plt.scatter(principleCustomKeywordSentiments[customKeyword1], principleCustomKeywordSentiments[customKeyword2])
            for i in range(len(principleCustomKeywordSentiments)):
                plt.annotate(principleCustomKeywordSentiments.index[i], (principleCustomKeywordSentiments[customKeyword1][i], principleCustomKeywordSentiments[customKeyword2][i]))
            plt.title(f'各候選人與關鍵字{customKeyword1}與{customKeyword2}情緒之知覺圖')
            plt.xlabel(customKeyword1)
            plt.ylabel(customKeyword2)
            plt.show()

def drawPrincipalCustomKeywordSegimentsGroupLine(dataframe: pd.DataFrame):
    
    # 需要先將資料複製出來，避免影響原資料
    copyDataframe = dataframe.copy()

    # 自訂關鍵字
    customKeywords = ["賄選", "台獨", "民調", "造勢", "連任", "總統大選", "黨內聲量", "民意聲量", "網路聲量"]

    # 計算每一個關鍵字的聲量
    for keyword in customKeywords:
      # 如果留言內容含keyword字詞，就計數１
      copyDataframe[keyword] = copyDataframe['content'].apply(lambda x: 1 if keyword in x else 0)
    
    #將聲量欄位名加入特徵值list，以利後續讀取資料使用
    copyDataframe['聲量'] = 1
    customKeywords.append("聲量") 

    # 計算每一使用者的聲量
    volume_cluster = copyDataframe.groupby(['author'], as_index=False)[customKeywords].sum()

    volume_cluster = volume_cluster.set_index(['author', '聲量'])

    # 機器學習自動分群
    # 方法一：肘部法則
    from sklearn.cluster import KMeans
    distortions = []
    for k in range(1,15):
      kmeanModel = KMeans(n_clusters=k,random_state=1, n_init='auto').fit(volume_cluster)
      distortions.append(kmeanModel.inertia_) #Inertia計算群內所有點到該群的中心的距離的總和。

    plt.figure(figsize=(16,8))
    plt.plot(range(1,15), distortions, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Distortion')
    plt.title('The Elbow Method showing the optimal k')
    plt.show()

    # 方法二：輪廓分析法
    # silhouette_score，越大越好
    from sklearn.metrics import silhouette_score

    for k in range(2,15):
        kmeanModel = KMeans(n_clusters=k,random_state=1, n_init='auto').fit(volume_cluster)
        silhouette_avg = silhouette_score(volume_cluster,kmeanModel.labels_)
      
        print('Silhouette Score for %i Clusters: %0.4f' % (k, silhouette_avg))


    # 最後決定分成4群
    clustering = KMeans(n_clusters=4,random_state=1, n_init='auto').fit(volume_cluster)  

    # 將分群結果加入原始資料
    volume_cluster['cluster'] = clustering.labels_

    # 設定過渡參數【人數】，後續用來統計每一群的市場人數
    volume_cluster['人數'] = 1

    # 找出每一個群體的特徵加總
    volume_cluster_group= volume_cluster.groupby(['cluster'], as_index=False).sum()
    print(volume_cluster_group)

    # 繪製群體人數圖
    plt.bar(volume_cluster_group['cluster'], volume_cluster_group['人數'])
    plt.title('各群體人數')
    plt.xlabel('群體')
    plt.ylabel('人數')
    plt.show()

    # 繪製群體各關鍵字聲量圖
    for keyword in customKeywords:
        if keyword not in volume_cluster_group.columns:
            continue
        plt.plot(volume_cluster_group['cluster'], volume_cluster_group[keyword], label=keyword)
    plt.legend()
    plt.title(f'各群體關鍵字聲量')
    plt.xlabel('群體')
    plt.ylabel('聲量')
    plt.show()