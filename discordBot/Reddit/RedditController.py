from discordBot.Reddit import RedditCredentials
import pprint

class RedditController():

    reddit = RedditCredentials.acquireRedditInstance()

    def __init_(self):
        pass

#Fetch submissions
    def acquireSubredditTopSubmissions(self,subredditName):
        subreddit = self.reddit.subreddit(subredditName)
        topSubredditResults = []
        for submission  in subreddit.top(limit=5):
            topSubredditResults.append(self.createSubmissionDictionary(submission))

        return topSubredditResults

    def acquireSubredditHotSubmissions(self,subredditName):
        subreddit = self.reddit.subreddit(subredditName)
        hotSubredditResults = []
        for submission in subreddit.hot(limit=5):
            hotSubredditResults.append(self.createSubmissionDictionary(submission))

        return hotSubredditResults

    def acquireSubRedditNewSubmissions(self,subredditName):
        subreddit = self.reddit.subreddit(subredditName)
        newSubredditResults = []
        for submission in subreddit.hot(limit=5):
            newSubredditResults.append(self.createSubmissionDictionary(submission))

        return newSubredditResults

#extract submissions
    def acquireSubredditTopSubmissionsURL(self,subredditName):
        topSubredditResults = self.acquireSubredditTopSubmissions(subredditName)
        submissionURLList = []
        for submission in topSubredditResults:
            submissionURLList.append(submission['url'])
        return submissionURLList

    def createSubmissionDictionary(self,submission):
        submissionDict = {}
        submissionDict['title'] = submission.title
        submissionDict['score'] = submission.score
        submissionDict['id'] = submission.id
        submissionDict['author'] = submission.author
        submissionDict['url'] = submission.url
        submissionDict['num_comments'] = submission.num_comments
        submissionDict['thumbnail'] = submission.thumbnail
        submissionDict['spoiler'] = submission.spoiler
        submissionDict['visited'] = submission.visited
        return submissionDict

def main():
    subredditName = 'anime'
    reddit = RedditController()
    topResults = reddit.acquireSubredditTopSubmissions(subredditName)
    for submission in topResults:
        print (submission['thumbnail'])

if __name__ == "__main__":
    main()
