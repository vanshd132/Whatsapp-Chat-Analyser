import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_top_authors(df):
    author_message_counts = df['Author'].value_counts()
    top_authors = author_message_counts.head(5)
    top_authors_df = top_authors.reset_index()
    top_authors_df.columns = ['Author', 'MessageCount']

    fig = px.bar(top_authors_df, x='Author', y='MessageCount', title='Top 5 Senders and Their Message Counts')
    fig.show()

def generate_wordcloud(df):
    all_messages = ' '.join(df['Message'].tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_messages)

    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
