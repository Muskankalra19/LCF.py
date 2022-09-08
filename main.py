from instapy import InstaPy

session = InstaPy(username="your username",password="your password")
session.login()


#like bu tags

session.like_by_tags(["dance", "mercedes"], amount=10, interact=True)


#don't like

session.set_dont_like(["naked", "murder", "nsfw"])

#set comment

session.set_do_comment(True, percentage=100)
session.set_comments(["Nice", "Amazing", "Super"])

#set  follow

session.set_do_follow(enabled=True, percentage=100)

#set interaction

session.set_user_interact(amount=1, randomize=True, percentage=100)

#end

session.end()
