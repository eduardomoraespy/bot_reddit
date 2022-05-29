import praw

# Criação de instância reddit
reddit = praw.Reddit(
    client_id="WluufyHLR3ERQrin5EbRhQ",
    client_secret="XHZkGjaq4Uir3Gt_aN6VqhtPOmXr5Q",
    user_agent="bot python",
)

#print(reddit.user.me())

subreddit = reddit.subreddit("television")

# for post in subreddit.hot(limit=10):
#     print(post.title)

for submission in subreddit.hot(limit=10):

    print('******************')
    print(submission.title)

    for comment in submission.comments:
        if hasattr(comment, "body"):
            # Responder comentário
            comment_lower = comment.body.lower()

            if " sad " in comment_lower:
                pass
            print('-------')
            print(comment.body)


