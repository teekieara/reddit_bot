import praw

# Simplified credentials
reddit = praw.Reddit(
    client_id="Lo2_zCPNEBnYxhghn_gQiQ",  # Replace with your Client ID
    client_secret="PLwoo0YegVibgDLLG86bSzYq-gZiXQ",  # Replace with your Client Secret
    username="QuantamHack",  # Replace with your Reddit username
    password="Olafunmi2018!",  # Replace with Reddit App Password if 2FA is enabled
    user_agent="TestBot/0.1 by u/QuantamHack"  # Custom user agent
)

try:
    print("Testing Reddit login...")
    user = reddit.user.me()
    if user:
        print(f"Success! Logged in as: {user}")
    else:
        print("Login failed: Could not authenticate user.")
except Exception as e:
    print(f"Error: {e}")
