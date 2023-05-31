import pandas as pd
from src.types import RawDataDict, ProcessedCommentDict
from src.process_data import showRowData, transferCommentToArrayStr

def main():
    
    # 讀取 csv 檔案，並將資料儲存至 dataframe
    df: RawDataDict = pd.read_csv('static/crawl_data.csv')

    # 呼叫 showRowData 函式，顯示第一筆資料
    # print(showRowData(df[:1]))

    # 呼叫 transferCommentToArrayStr 函式，將每個文章的留言物件陣列轉成一個字串陣列
    comments: list[ProcessedCommentDict] = transferCommentToArrayStr(df['所有留言'])
    print(comments)

main()