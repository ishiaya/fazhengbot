# coding:utf-8
import sys
sys.path.append('/Users/ayako/python/') #tweetpy.pyのパスを指定
import twitter_key #.pyは書かなくてもimportできた

api = twitter_key.api # apiと打つだけでtweetpy.apiを指示できる
#api.update_status(status='pythonからツイートしてます') # 連続で同じ内容のツイートはできない

# 検索ワードと検索数をセット
#k_word1 = "#無双フォト 法正"
#k_word2 = "#フォトモード乱舞 法正 -#無双フォト"
#count = 5

# 検索実行
#search_results = api.search(q=k_word1, count=count)


#q = "#無双フォト 法正" #ここに検索キーワードを設定
#count = 30
#search_results = api.search(q=q, count=count)

def rt_func(q,count):
    search_results = api.search(q=q, count=count)
    rt_count = 0
    for result in search_results:
        username = result.user._json['screen_name']
        tweet_id = result.id #ツイートのstatusオブジェクトから、ツイートidを取得
        print(tweet_id)
        user_id = result.user.screen_name #ツイートした人のID（＠〜〜〜）を取得する
        print(user_id)
        user_name = result.user.name #ツイートのstatusオブジェクトから、userオブジェクトを取り出し、名前を取得する
        print(user_name)
        tweet = result.text
        print(tweet)
        time = result.created_at
        print(time)
        print("ーーーーーーーーーーーー")

        if user_id == "otashi4":
                print("###ファボ判定###")
                try:
                    api.retweet(tweet_id) #ふぁぼる
                    print(user_name)
                    print("をリツイートしました")
                    rt_count = rt_count + 1
                    print("##################")
                except:
                    print("もうすでにふぁぼしてますわ")
                print("##################")
    return rt_count

#本処理
if __name__ == '__main__':
    #無双フォトかつ法正をRTする
    print(rt_func("#無双フォト 法正",50))
    print("回リツイートしました。")

    #フォトモード乱舞かつ法正かつ無双フォトではないものをRTする
    print(rt_func("#フォトモード乱舞 法正 -#無双フォト",50))
    print("回リツイートしました。")
