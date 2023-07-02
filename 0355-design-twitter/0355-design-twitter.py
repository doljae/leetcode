#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import *


class Twitter:
    def __init__(self):
        self.tweets = collections.defaultdict(list)
        self.follows = collections.defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append((tweetId, self.timestamp))

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.follows[userId].union(set([userId]))
        feeds = []
        for userId in self.tweets:
            if userId in followers:
                feeds += self.tweets[userId]

        feeds.sort(key=lambda x: x[-1], reverse=True)

        return [x[0] for x in feeds[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
