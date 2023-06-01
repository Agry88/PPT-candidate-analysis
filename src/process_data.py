import pandas as pd
from typing import List
from src.types import CommentDict

# 顯示每個欄位的資料
def showRowData(dataframe: pd.DataFrame):
    for col in dataframe.columns:
        print(f'{col}：{dataframe[col].iloc[0]}\n')

# #資料清理，無意義字元去除
def removeWords(content: str):
    removeword = ['span','class','f3','https','imgur','h1','_   blank','href','rel',
                'nofollow','target','cdn','cgi','b4','jpg','hl','b1','f5','f4',
                'goo.gl','f2','email','map','f1','f6','__cf___','data','bbs'
                'html','cf','f0','b2','b3','b5','b6','原文內容','原文連結','作者'
                '標題','時間','看板','<','>','，','。','？','—','閒聊','・','/',
                ' ','=','\"','\n','」','「','！','[',']','：','‧','╦','╔','╗','║'
                ,'╠','╬','╬',':','╰','╩','╯','╭','╮','│','╪','─','《','》','_'
                ,'.','、','（','）','　','*','※','~','○','”','“','～','@','＋','\r'
                ,'▁',')','(','-','═','?',',','!','…','&',';','『','』','#','＝'
                ,'\l']
    for word in removeword:
        content = content.replace(word,'')
    return content
        

# 將每個文章的留言物件陣列轉成一個字串陣列
def transferCommentToArrayStr(postCommentsArray: List[List[str]]):
    
    # 檢查留言是否有效
    def checkCommentValid(comment: CommentDict):
        return (
            (comment['content'] != '' or comment['content'] != None) and
            (len(comment['ipdatetime'].split(' ')) > 1)
        )
    
    # 移除留言中的 ip
    def removeIpInComment(ipdatetime: str):
        splitArray = ipdatetime.split(' ')
        return splitArray[1]

    allComment = []
    for postComment in postCommentsArray:
        for comment in eval(postComment):
            typedComment: CommentDict = comment
            if checkCommentValid(typedComment):
              allComment.append({
                "author": typedComment['user'],
                "content": removeWords(typedComment['content']),
                "time": removeIpInComment(typedComment['ipdatetime'])
              })


    # 根據時間排序
    allComment.sort(key=lambda x: x['time'])

    return allComment


# 將每個文章的標題加上內文變成一個字串
def transferPostContentToArrayStr(postAuthors ,postTitles: List[str], postContents: List[str], postDates: List[str]):
    allPost = []
    for postAuthor, postTitle, postContent, postDate in zip(postAuthors, postTitles, postContents, postDates):
        
        month = monthConverter(postDate.split(' ')[1])
        day = postDate.split(' ')[2]

        allPost.append({
            "author": postAuthor,
            "content": removeWords(postTitle + postContent),
            "time": f'{month}/{day}'
        })

    return allPost

# 將月份轉成數字
def monthConverter(month):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(month) + 1

def sentimentAnalysis(str: str):
    from snownlp import SnowNLP
    s = SnowNLP(str)
    return s.sentiments
    

    