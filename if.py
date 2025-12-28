current_users=['admin','B','C','D','E']
new_users=['D','e','F','G','H']
current_users_lower=[]
for user in current_users:
    current_users_lower.append(user.lower())
for user in new_users:
    if user.lower() in current_users_lower:
        print(' enter a new username. ')
    else:
        print('username is available.')
    