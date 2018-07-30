# coding:utf-8
import sys
sys.path.append('/Users/ayako/python/') #tweetpy.pyのパスを指定
import twitter_key #.pyは書かなくてもimportできた

api = twitter_key.api # apiと打つだけでtweetpy.apiを指示できる
#api.update_status(status='pythonからツイートしてます') # 連続で同じ内容のツイートはできない

# リツイート処理
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

        print("###リツイート判定###")
        try:
            api.retweet(tweet_id) #リツイート
            print(user_name)
            print("をリツイートしました")
            rt_count = rt_count + 1
            print("##################")
        except:
            print("もうすでにリツイートしてます")
        print("##################")
    return rt_count

# フォロー処理
def followAndUnfollow(api):
    followersIds = api.followers_ids()
    friendsIds = api.friends_ids()

    #フォロアーにそのユーザが存在しなければアンフォロー
    for friendId in friendsIds:
        count = 0
        for followerId in followersIds:
            if friendId==followerId:
                break
            count+=1
        if count == len(followersIds):
            try:
                api.destroy_friendship(friendId)
                print ('Destoroyed friendship with %s' %friendId)
            except tweepy.error.TweepError:
                print ('I could not destroy this friendship.:(')

    #フォローしていないフォロアーがいればフォロー
    for followerId in followersIds:
        count=0
        for friendId in friendsIds:
            if followerId == friendId:
                break
            count += 1
        if count == len(friendsIds):
            try:
                api.create_friendship(followerId, True)
                print ('Created friendship with %s :)' %followerId)
            except tweepy.error.TweepError:
                print ('I could not create this friendship.:(')

#本処理
if __name__ == '__main__':
    #無双フォトかつ法正をRTする
    print(rt_func("#無双フォト 法正",10))
    print("回リツイートしました。")

    #フォトモード乱舞かつ法正かつ無双フォトではないものをRTする
    print(rt_func("#フォトモード乱舞 法正 -#無双フォト",10))
    print("回リツイートしました。")

    #フォロー処理をする
    followAndUnfollow(api)
