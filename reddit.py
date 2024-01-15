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
amount = 0

for submission in reddit.subreddit(subredditName).top(limit = 1):
   submission.comments.replace_more(limit=0)
   for top_level_comment in submission.comments:
      for word in top_level_comment.body.split():
         if word in wordcount:
            wordcount[word] += 1
         else:
            wordcount[word] = 1


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

