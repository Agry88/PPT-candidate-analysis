import pandas as pd
from src.types import RawDataDict, ProcessedTextDict
from src.process_data import transferCommentToArrayStr, transferPostContentToArrayStr, sentimentAnalysis

# 取得處理過的資料
def getProcessedData():
    # 讀取 csv 檔案，並將資料儲存至 dataframe
    df: RawDataDict = pd.read_csv('static/crawl_data.csv')

    # 呼叫 showRowData 函式，顯示第一筆資料
    # print(showRowData(df[:1]))

    # 呼叫 transferPostContentToArrayStr 函式，將每個文章的標題加上內文變成一個字串
    posts: list[ProcessedTextDict] = transferPostContentToArrayStr(df['作者'],df['標題'], df['內文'], df['日期'])

    # 呼叫 transferCommentToArrayStr 函式，將每個文章的留言物件陣列轉成一個字串陣列
    comments: list[ProcessedTextDict] = transferCommentToArrayStr(df['所有留言'])

    texts = posts + comments
    print(len(texts))
    #sentiments = [sentimentAnalysis(text['content']) for text in texts]
    #print(sentiments)

    #processedDataframe = pd.DataFrame({
    #    "author": [text['author'] for text in texts],
    #    'content': [text['content'] for text in texts],
    #    'time': [text['time'] for text in texts],
    #    'sentiment': sentiments
    #})


    # processedDataframe.to_csv('static/processed_data.csv', index=False)

# 取得處理過的資料生成的圖表
def getProcessedDataChart():
    pass

getProcessedData()