from typing import TypedDict, List

# 宣告原本的留言型態
class CommentDict(TypedDict):
    author: str
    type: str
    user: str
    content: str
    ipdatetime: str

# 剛爬下來只有基本處理的資料型態
class RawDataDict(TypedDict):
    Unnamed: int
    文章編碼: str
    作者: str
    版名: str
    分類: str
    標題: str
    內文: str
    日期: str
    IP位置: str
    總留言數: int
    噓: int
    推: int
    中立: int
    文章分數: int
    所有留言: List[CommentDict]

# 處理完後的文字型態
class ProcessedTextDict(TypedDict):
    content: str
    time: str

# 處理完後的資料型態
# 將留言物件陣列轉成一個字串陣列
# 標題加上內文變成一個字串
class ProcessedDataDict(TypedDict):
    所有文: List[str]
    情緒分數: List[int]