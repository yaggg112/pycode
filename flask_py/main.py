from flask import Flask
main=Flask(__name__) #代表目前執行的模組

@main.route("/") #函式的裝飾(decorator):以函式為基礎，提供附加的功能
def home():
    return "hello flask 2"

@main.route("/test")
def test():
    return "this is test!!"

if __name__=="__main__": #如果以主程式執行
    main.run() #立刻啟動伺服器
