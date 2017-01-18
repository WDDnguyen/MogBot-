from discordBot.Reddit import RedditCredentials
import pprint
from random import randint

class RedditController():

    reddit = RedditCredentials.acquireRedditInstance()

    def __init_(self):
        pass

#Fetch submissions
    def acquireSubredditTopSubmissions(self,subredditName):
        subreddit = self.reddit.subreddit(subredditName)
        topSubredditResults = []
        for submission  in subreddit.top(limit=15):
            topSubredditResults.append(self.createSubmissionDictionary(submission))

        return topSubredditResults

    def acquireSubredditHotSubmissions(self,subredditName):
        subreddit = self.reddit.subreddit(subredditName)
        hotSubredditResults = []
        for submission in subreddit.hot(limit=15):
            hotSubredditResults.append(self.createSubmissionDictionary(submission))

        return hotSubredditResults

    def acquireSubredditNewSubmissions(self,subredditName):
        subreddit = self.reddit.subreddit(subredditName)
        newSubredditResults = []
        for submission in subreddit.new(limit=15):
            newSubredditResults.append(self.createSubmissionDictionary(submission))

        return newSubredditResults

#extract submissions

    def extractSubmissionsByUpvotes(self,submissionList):
        submissionsSortedByHighestUpvotesList = sorted(submissionList, key=lambda k: k['score'])
        return submissionsSortedByHighestUpvotesList

    def pickRandomSubmission(self,submissionList):
        randomPickedSubmission = submissionList[randint(0, len(submissionList) - 1)]
        return randomPickedSubmission

#Top submissions
    def acquireSubredditRandomTopSubmissionsURL(self,subredditName):
        topSubredditResults = self.acquireSubredditTopSubmissions(subredditName)
        randomTopSubmissionURL = self.pickRandomSubmission(topSubredditResults)['url']
        return randomTopSubmissionURL

    def acquireSubredditTopSubmissionsURL(self,subredditName):
        topSubredditResults = self.acquireSubredditTopSubmissions(subredditName)
        submissionURLList = []
        for submission in topSubredditResults:
            submissionURLList.append(submission['url'])
        return submissionURLList

#Hot submissions
    def acquireSubredditRandomHotSubmissionsURL(self,subredditName):
        hotSubredditResults = self.extractSubmissionsByUpvotes(self.acquireSubredditHotSubmissions(subredditName))
        randomHotSubmissionURL = self.pickRandomSubmission(hotSubredditResults)['url']
        return randomHotSubmissionURL

    def acquireSubredditHotSubmissionsURL(self,subredditName):
        hotSubredditResults = self.extractSubmissionsByUpvotes(self.acquireSubredditHotSubmissions(subredditName))
        submissionURLList = []
        for submission in hotSubredditResults:
            submissionURLList.append(submission['url'])
        return submissionURLList

#new submissions

    def acquireSubredditRandomNewSubmissionsURL(self,subredditName):
        newSubredditResults = self.extractSubmissionsByUpvotes(self.acquireSubredditNewSubmissions(subredditName))
        randomNewSubmissionURL = self.pickRandomSubmission(newSubredditResults)['url']
        return randomNewSubmissionURL

    def acquireSubredditNewSubmissionsURL(self, subredditName):
        newSubredditResults = self.extractSubmissionsByUpvotes(self.acquireSubredditNewSubmissions(subredditName))
        submissionURLList = []
        for submission in newSubredditResults:
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
    subredditName = 'games'
    reddit = RedditController()
    topResults = reddit.acquireSubredditTopSubmissions(subredditName)
    submissionList = []
    submission1 = { 'title' : 'title1', 'score' : 60}
    submission2 = {'title': 'title2', 'score': 20}
    submission3 = {'title': 'title3', 'score': 40}
    submissionList.append(submission1)
    submissionList.append(submission2)
    submissionList.append(submission3)

    sortedByHighestUpvoteList = sorted(submissionList, key=lambda k: k['score'])
    print(sortedByHighestUpvoteList)

if __name__ == "__main__":
    main()
