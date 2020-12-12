user_titles = {
    1: [271, 318, 491],
    2: [318, 19, 2980, 475],
    3: [475],
    4: [271, 318, 491, 2980, 19, 318, 475],
    5: [882, 91, 2980, 557, 35],
}

def get_user_num_title(titles):
    user_num_title = {}
    for user, title in titles.items():
        user_num_title[user] = len(title)

    return user_num_title
print(get_user_num_title(user_titles))