import pandas as pd
from typing import List
from src.types import CommentDict
import json

# 顯示每個欄位的資料
def showRowData(dataframe: pd.DataFrame):
    for col in dataframe.columns:
        print(f'{col}：{dataframe[col].iloc[0]}\n')

def transferCommentToArrayStr(postCommentsArray: List[List[CommentDict]]):
    allComment = []
    for postComment in postCommentsArray:
        for comment in eval(postComment):
            allComment.append(comment['content'])
    return allComment