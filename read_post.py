import praw
import time
import random

# Set up Reddit API credentials
reddit = praw.Reddit(
    client_id="Lo2_zCPNEBnYxhghn_gQiQ",                 # Your Client ID
    client_secret="PLwoo0YegVibgDLLG86bSzYq-gZiXQ",  # Your Client Secret
    username="QuantamHack",              # Your Reddit bot username
    password="Olafunmi2018!",            # Replace with your Reddit account password
    user_agent="QuantamHackBot by u/QuantamHack - A bot to explore sci-fi threads"  
)

# Manually define the subreddits to target, with "nerdy" subreddits first
subscribed_subreddits = [
    # Nerdy subreddits prioritized first
    "scifi",
    "cyberpunk",
    "technology",
    "futurology",
    "philosophyofscience",
    "worldbuilding",
    "AI",
    "MachineLearning",
    "DataScience",
    "Space",
    "timetravel",
    "computerscience",
    "QuantumComputing",
    "singularity",
    "virtualreality",
    "neuralink",
    "elonmusk",
    "robotics",
    "sciencefiction",
    "SimulationTheory",
    "transhumanism",
    "BlackMirror",
    "StarTrek",
    "StarWars",
    # Other general subreddits like r/AskReddit come last
    "AskReddit"
]

print(f"✨ Targeting {len(subscribed_subreddits)} subreddits: {', '.join(subscribed_subreddits)}")


# Keywords and responses
keywords_and_responses = {
    "AI": "AI is literally reshaping the world, and it’s such a vibe! I dive deep into AI, consciousness, and dystopian futures in my story *Bytes of the Matrix*. Check it out here on Wattpad: https://www.wattpad.com/story/377895934-bytes-of-the-matrix or Substack: https://substack.com/@codedvision. Pick what works for you!",
    "artificial intelligence": "Artificial intelligence is taking over, and honestly, it’s such a mood. If you’re into sci-fi and all things futuristic, you’d love my story *Bytes of the Matrix*. Dive in on Substack: https://substack.com/@codedvision or Wattpad: https://www.wattpad.com/story/377895934-bytes-of-the-matrix.",
    "cyberpunk": "Cyberpunk is like *chef's kiss*! It’s such an aesthetic. My story *Bytes of the Matrix* blends cyberpunk vibes with a dystopian twist. Peep it here: https://substack.com/@codedvision or if Wattpad is your thing: https://www.wattpad.com/story/377895934-bytes-of-the-matrix.",
    "dystopia": "Dystopian futures hit different, right? My story *Bytes of the Matrix* explores a world where AI might just cross the line. Give it a read on Wattpad: https://www.wattpad.com/story/377895934-bytes-of-the-matrix or Substack: https://substack.com/@codedvision. Let me know if you vibe with it!",
    "futurism": "Futurism? More like future-is-now-ism! My sci-fi story *Bytes of the Matrix* is packed with AI, consciousness, and dystopian vibes. Substack fam: https://substack.com/@codedvision or Wattpad crew: https://www.wattpad.com/story/377895934-bytes-of-the-matrix. Let me know what you think!",
    "elon musk": "Elon Musk always has everyone talking, right? Speaking of futuristic vibes, I write about AI and dystopian futures in my story *Bytes of the Matrix*. You can check it out here: https://substack.com/@codedvision or here: https://www.wattpad.com/story/377895934-bytes-of-the-matrix.",
    "neuralink": "Neuralink is wild when you think about it—next-level tech. If you’re into futuristic, mind-blowing stories, check out *Bytes of the Matrix*. Wattpad vibes: https://www.wattpad.com/story/377895934-bytes-of-the-matrix or Substack feels: https://substack.com/@codedvision. Let’s chat about it!"
}

# Create or open a log file
log_file = open("bot_activity_log.txt", "a")

# Rate limiting variables
comments_made = 0
MAX_COMMENTS_PER_HOUR = 3  # Maximum comments per hour

# Loop through the manually defined subreddits
for sub in subscribed_subreddits:
    subreddit = reddit.subreddit(sub)
    print(f"🌌 Searching for relevant posts in r/{sub}...")
    
    for submission in subreddit.new(limit=10):  # Fetch the 10 newest posts
        # Check if the post title or selftext contains any of the keywords
        matched_keyword = next(
            (keyword for keyword in keywords_and_responses if keyword.lower() in submission.title.lower() or keyword.lower() in submission.selftext.lower()),
            None
        )
        
        if matched_keyword:
            print(f"🎯 Found a relevant post: {submission.title} (Keyword: {matched_keyword})")
            
            # Check if the bot has already commented on this post
            submission.comments.replace_more(limit=0)  # Ensure we load all top-level comments
            already_commented = any(comment.author == "QuantamHack" for comment in submission.comments)
            
            if not already_commented:
                try:
                    # Rate limit: Pause if the bot reaches the hourly limit
                    if comments_made >= MAX_COMMENTS_PER_HOUR:
                        print("⏳ Rate limit reached. Pausing for 1 hour.")
                        time.sleep(3600)  # Wait 1 hour
                        comments_made = 0  # Reset counter
                    
                    # Get the response for the matched keyword
                    comment_text = keywords_and_responses[matched_keyword]

                    # Post the comment
                    submission.reply(comment_text)
                    print(f"✅ Commented on the post: {submission.title}")
                    
                    # Increment comment counter
                    comments_made += 1

                    # Log the activity
                    log_file.write(f"Commented on: {submission.title} (URL: {submission.url})\n")

                    # Add a randomized delay
                    delay = random.randint(60, 180)  # Wait between 1 to 3 minutes
                    print(f"⏳ Waiting {delay} seconds before next comment...")
                    time.sleep(delay)
                except Exception as e:
                    print(f"❌ Error posting comment: {e}")
                    log_file.write(f"Error commenting on: {submission.title} (Error: {e})\n")
            else:
                print("🤖 Bot has already commented on this post.")
        else:
            print(f"🚫 No relevant keywords found in: {submission.title}")
            log_file.write(f"Skipped: {submission.title} (URL: {submission.url})\n")

# Close the log file
log_file.close()
print("✅ Bot has finished running.")

# Test for GitHub :)






















