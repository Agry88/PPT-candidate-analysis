import pandas as pd
from src.types import RawDataDict
from src.process_data import getPrincipalProcessedData

# 取得處理過的資料
def getProcessedData():
    # 讀取 csv 檔案，並將資料儲存至 dataframe
    df: RawDataDict = pd.read_csv('static/crawl_data.csv')

    # 呼叫 showRowData 函式，顯示第一筆資料
    # print(showRowData(df[:1]))

    # 候選人(品牌)名單
    principals = ["柯文哲","侯友宜","賴清德"]

    # 建立一個空的 dataframe，用來儲存處理過的資料
    dataframe = pd.DataFrame(columns=['author', 'content', 'time', 'sentiment'])
    for principal in principals:
        # 呼叫 getPrincipalProcessedData 函式，取得特定候選人的資料
        principalDataframe = getPrincipalProcessedData(df, principal)

        # 將處理過的資料合併成一個 dataframe
        dataframe = pd.concat([dataframe, principalDataframe], ignore_index=True)

    dataframe.to_csv('static/processed_data.csv', index=False)

# 取得處理過的資料生成的圖表
def getProcessedDataChart():
    pass

if __name__ == '__main__':
  getProcessedData()