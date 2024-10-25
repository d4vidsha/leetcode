
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.usersFollowees = defaultdict(set)
        self.usersPosts = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # O(1)
        self.usersPosts[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        pq = []
        self.usersFollowees[userId].add(userId)
        for uid in self.usersFollowees[userId]:
            if uid in self.usersPosts:
                i = len(self.usersPosts[uid]) - 1
                count, tid = self.usersPosts[uid][i]
                heapq.heappush(pq, (count, tid, uid, i - 1))
        self.usersFollowees[userId].remove(userId)
        
        while pq and len(res) < 10:
            _, tid, uid, i = heapq.heappop(pq)
            res.append(tid)
            if i >= 0:
                count, tid = self.usersPosts[uid][i]
                heapq.heappush(pq, (count, tid, uid, i - 1))

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.usersFollowees[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.usersFollowees[followerId]:
            self.usersFollowees[followerId].remove(followeeId)
        
