from make_soup import make_soup
from get_words_from_topic import get_topic_words
from dict_to_file import write_words_to_file


def get_main_topics_from_soup(url):
    return make_soup(url).find_all('div', class_='category-title-container')


def get_topics(url):
    return make_soup(url).find_all('a', class_='linkable-word-box-container')


if __name__ == '__main__':
    words_set = {}
    url = 'https://languagedrops.com/word/en/english/hebrew/'
    # url = 'https://languagedrops.com/word/en/english/russian/'
    for topic in get_topics(url):
        topic_name = topic.text.lower().replace(' ', '_')
        get_topic_words(topic_name, words_set)
    print(len(words_set))
    write_words_to_file(words_set)
