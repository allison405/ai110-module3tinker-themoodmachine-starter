"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    "hopeful",
    "finished",
    "proud",
    "grateful",
    "friday",
    "finished"
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    "late",
    "missed",
    "spilled",
    ":(",
    "stuck",
    "empty",
    "traffic",
    "failed",
    "cry",
    "💀",
    "😭",
]

NEUTRAL_WORDS = [
    "idk",
    "fine",
]

MIXED_WORDS = [
    "but",
    "at least",
]



# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "lowkey having the best day no cap 😂",
    "I absolutely love being stuck in traffic for two hours :(",
    "highkey obsessed with this new song 🥲",
    "not sure how I feel about this tbh",
    "failed the quiz but at least it's Friday 💀",
    "this is fine everything is fine :)",
    "so stressed I could cry but I finished the project 😭",
    "woke up late, missed breakfast, spilled coffee — amazing morning honestly",
    "honestly feeling kind of empty today idk",
    "life is weird but I'm here for it 😂",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    "positive",  # "lowkey having the best day no cap 😂"
    "negative",  # "I absolutely love being stuck in traffic for two hours :(" — sarcasm
    "positive",  # "highkey obsessed with this new song 🥲"
    "neutral",   # "not sure how I feel about this tbh"
    "mixed",     # "failed the quiz but at least it's Friday 💀"
    "neutral",   # "this is fine everything is fine :)" — edge case, could read as sarcasm
    "mixed",     # "so stressed I could cry but I finished the project 😭"
    "negative",  # "woke up late, missed breakfast, spilled coffee — amazing morning honestly" — sarcasm
    "negative",  # "honestly feeling kind of empty today idk"
    "positive",  # "life is weird but I'm here for it 😂"
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
