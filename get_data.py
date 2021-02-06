
import instaloader
import sys
insta_api = instaloader.Instaloader()

# Login or load session
username = sys.argv[1]
password = sys.argv[2]

print("Connecting with Instagram API // If you receive an email that says login from Linux. That's me!")

insta_api.login(username, password) # (login)

# Obtain profile metadata
profile = instaloader.Profile.from_username(insta_api.context, username)

follower_list = []
following_list = []
follower_file = open("followers.txt", "a+")
following_file = open("following.txt", "a+")

for follower in profile.get_followers():
    follower_list.append(follower.username)
    follower_file.write(follower.username + "\n")
follower_file.close()
print("Received all followers data ...")

for following in profile.get_followees():
    following_list.append(following.username)
    following_file.write(following.username + "\n")
following_file.close()
print("Received all following data ...")