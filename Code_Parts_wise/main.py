import pandas as pd
from data_processing import startWithDateAndTimeAndroid, getDataPointAndroid
from visualization import plot_top_authors, generate_wordcloud
from analysis import analyze_authors, search_messages

def main():
    parsedData = []
    conversationPath = 'Source.txt'
    with open(conversationPath, encoding='utf-8') as fp:
        first = fp.readline()
        device = 'ios' if '[' in first else 'android'
        fp.readline()
        messageBuffer = []
        date, time, author = None, None, None

        while True:
            line = fp.readline()
            if not line:
                break
            line = line.strip()
            if startWithDateAndTimeAndroid(line) or True:
                data = getDataPointAndroid(line)
                if data is not None:
                    date, time, new_author, message = data
                    if date is None:
                        messageBuffer.append(line)
                    else:
                        if messageBuffer:
                            parsedData.append([date, time, author, ' '.join(messageBuffer)])
                        messageBuffer.clear()
                        date, time, author, message = getDataPointAndroid(line)
                        messageBuffer.append(message)
        
    df = pd.DataFrame(parsedData, columns=['Date', 'Time', 'Author', 'Message'])
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%m/%d/%y')
    df['urlcount'] = df.Message.apply(lambda x: re.findall(r'(https?://\S+)', x)).str.len()

    plot_top_authors(df)
    generate_wordcloud(df)
    analyze_authors(df)

    search_word = input("Enter a word to search for in messages: ").lower()
    search_messages(df, search_word)

if __name__ == "__main__":
    main()
