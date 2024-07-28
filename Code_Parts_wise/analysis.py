import pandas as pd

def analyze_authors(df):
    author_message_counts = df['Author'].value_counts()
    print("Authors with more than 100 messages:")
    print(author_message_counts[author_message_counts > 100].index.tolist())

def search_messages(df, search_word):
    messages_containing_word = df[df['Message'].str.lower().str.contains(search_word)]['Message']
    print(f"Number of messages containing the word '{search_word}': {len(messages_containing_word)}")
    for message in messages_containing_word:
        print(message)
