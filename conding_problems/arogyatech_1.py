"""
Design a simplified version of a blogging platform where authors can publish blog posts
 follow/unfollow other authors, and view the most 10 recent blog posts from the authors 
 they follow. Implement the BlogPlatform class with the following functionalities:
 
Implement the BlogPlatform class:  
 
	BlogPlatform() Initializes your object.  
 
	void follow(int followerId, int followeeId) The author with followerId starts
      following the author with followeeId.  
 
	void unfollow(int followerId, int followeeId) The author with ID followerId started
      unfollowing the author with ID followeeId.
 
	void publishPost (int authorId, int postId) Composes a new post with ID postId by the 
    author authorId. Each call to this function will be made with a unique postId.  
 
	List<Integer> getFeed (int authorId) Retrieves the 10 most recent blog post IDs in 
    the author 's feed. The feed should contain posts from authors they follow, as well as their 
    own posts. Posts must be ordered from most recent to least recent.

"""

from collections import defaultdict
from datetime import datetime

class BlogPlatform:
    def __init__(self, users=None):
        self.users = defaultdict(list) if not users else users
        self.post = []
    
    def follow(self, followerId :int, followeeId: int)-> None: #-->O(1)
        if followerId not in self.users:
            raise Exception("follower user_id doesn't exist")
        
        if followeeId not in self.users:
            raise Exception("followee user_id doesn't exist")
        

        self.users[followerId].append(followeeId)
    
    
    def unfollow(self, followerId :int, followeeId: int)-> None:# -->O(n)
        if followerId not in self.users:
            return "follower user_id doesn't exist"

        if followeeId not in self.users:
            return "followee user_id doesn't exist"

        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId) #--not optimize
        else:
            return f"user_id {followerId} does't follow user_id {followeeId}"
            
    
    def publishPost(self, authorId: int, postId: int)-> None: #-->O(1)
        self.post.append({"authorId": authorId, "postId": postId, "datetime": datetime.now()})

    
    def getFeed(self, authorId: int)-> list[int]: #--> O(m*n)
        author_follower_ids = self.users[authorId]

        data =  list(filter(self.post, key=lambda x: x["authorId"] in (author_follower_ids+[authorId])))

        data = sorted(data, key=lambda x: x["datetime"], reverse=True)[:10]

        return data

    