# Compare the following and follower lists
from collections import Counter

def get_data(filename):
    data = []
    with open(filename) as file:
        for line in file:
            data.append(line.rstrip("\n"))
    return data

def pretty_output(data_list):
    count = 0
    for data in data_list:
        if count >= 2:
            count = 0
            print(data)
        else:
            count += 1
            print(data, end=", ")
    print("\n")
    
def main():
    followers = get_data("followers.txt")
    following = get_data("following.txt")
    data_list = followers + following
    count_data = dict(Counter(data_list))

    users_not_following_me = []
    users_i_dont_follow = []
    for key, value in count_data.items():
        if value == 1:
            if key in following:
                users_not_following_me.append(key)
            elif key in followers:
                users_i_dont_follow.append(key)

    print("\n==== Results of Analysis ====")
    print("People who don't follow you:")
    pretty_output(users_not_following_me)

    print("People you are not following:")
    pretty_output(users_i_dont_follow)

    print("\nThank you!\nI would recommend changing your password after this.")

main()