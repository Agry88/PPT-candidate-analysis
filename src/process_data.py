import pandas as pd
from typing import List
from src.types import CommentDict

# 顯示每個欄位的資料
def showRowData(dataframe: pd.DataFrame):
    for col in dataframe.columns:
        print(f'{col}：{dataframe[col].iloc[0]}\n')

# 將每個文章的留言物件陣列轉成一個字串陣列
def transferCommentToArrayStr(postCommentsArray: List[List[str]]):
    
    def checkCommentValid(comment: CommentDict):
        return (
            (comment['content'] != '' or comment['content'] != None) and
            (len(comment['ipdatetime'].split(' ')) > 1)
        )
    
    def removeIpInComment(ipdatetime: str):
        splitArray = ipdatetime.split(' ')
        return splitArray[1]

    allComment = []
    for postComment in postCommentsArray:
        for comment in eval(postComment):
            typedComment: CommentDict = comment
            if checkCommentValid(typedComment):
              allComment.append({
                "content": typedComment['content'],
                "time": removeIpInComment(typedComment['ipdatetime'])
              })


    # 根據時間排序
    allComment.sort(key=lambda x: x['time'])

    return allComment