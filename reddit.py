import praw
import credentials
import matplotlib.pyplot as plt

reddit = praw.Reddit(
    client_id= credentials.client_id,
    client_secret=credentials.client_secret,
    user_agent="python3:myapp:0.1 (by u/EmilySelge)"
)

subredditName = "eesti"
wordcount = {}
sortedList = sorted(wordcount, reverse=True)
keywords = []
keyCount = []
count = 0
max = 100
amount = 0
commonwords = {'sest', 'et', 'aga', 'see', 'a', 'the', 'on', 'kui', 'ka', 'is', 'ja', 'ei', 'I', 'you', 'of', 'siis' 'that','this','and','of','the','for','I','it','has','in',
'you','to','was','but','have','they','a','is','','be','on','are','an','or',
'at','as','do','if','your','not','can','my','their','them','they','with',
'at','about','would','like','there','You','from','get','just','more','so',
'me','more','out','up','some','will','how','one','what',"don't",'should',
'could','did','no','know','were','did',"it's",'This','he','The','we',
'all','when','had','see','his','him','who','by','her','she','our','thing','-',
'now','what','going','been','we',"I'm",'than','any','because','We','even',
'said','only','want','other','into','He','what','i','That','thought',
'think',"that's",'Is','much'}


for submission in reddit.subreddit(subredditName).top(limit = 100):
   submission.comments.replace_more(limit=0)
   for top_level_comment in submission.comments:
      count+=1
      if count == max:
         break
      for word in top_level_comment.body.split():
         if not word in commonwords:
            if word in wordcount:
               wordcount[word] += 1
            else:
               wordcount[word] = 1
   if (count == max):
      break



sortedList = sorted(wordcount, key = wordcount.get, reverse=True)


for entry in sortedList:
   keywords.append(entry)
   keyCount.append(wordcount[entry])
   amount += 1
   if amount == 10:
      break
   
labels = keywords
sizes = keyCount

plt.title('top comments for: r/' + subredditName)
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.show()


