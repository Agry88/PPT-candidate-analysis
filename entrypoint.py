import pandas as pd
from src.types import RawDataDict
from src.process_data import getPrincipalProcessedData
from src.draw_data import drawPrincipalVolumeBar, drawPrincipalVolumeLine, drawPrincipalSentimentBar, drawPrincipalSentimentLine

# 取得處理過的資料
def getProcessedData():
    # 讀取 csv 檔案，並將資料儲存至 dataframe
    df: RawDataDict = pd.read_csv('static/crawl_data.csv')

    # 呼叫 showRowData 函式，顯示第一筆資料
    # print(showRowData(df[:1]))

    # 候選人(品牌)名單
    principals = ["柯文哲","侯友宜","賴清德"]

    # 建立一個空的 dataframe，用來儲存處理過的資料
    dataframe = pd.DataFrame(columns=['author', 'content', 'time', 'sentiment', 'principal'])
    for principal in principals:
        # 呼叫 getPrincipalProcessedData 函式，取得特定候選人的資料
        principalDataframe = getPrincipalProcessedData(df, principal)

        # Log讓開發人員知道進度
        print(f'{principal}的資料有{len(principalDataframe)}筆')

        # 將處理過的資料合併成一個 dataframe
        dataframe = pd.concat([dataframe, principalDataframe], ignore_index=True)

    # 去除掉重複的資料
    dataframe = dataframe.drop_duplicates()

    dataframe.to_csv('static/processed_data.csv', index=False)

# 取得處理過的資料生成的圖表
def getProcessedDataChart():
    # 讀取 csv 檔案，並將資料儲存至 dataframe
    # 欄位有 author,content,time,sentiment,principal
    df = pd.read_csv('static/processed_data.csv', parse_dates=['time'], date_format="%m/%d")

    # 各候選人聲量長條圖
    #drawPrincipalVolumeBar(df)

    # 各候選人聲量折線圖(趨勢圖)
    #drawPrincipalVolumeLine(df)

    # 各候選人情緒長條圖
    #drawPrincipalSentimentBar(df)

    # 各候選人情緒折線圖(趨勢圖)
    drawPrincipalSentimentLine(df)

if __name__ == '__main__':
  getProcessedDataChart()