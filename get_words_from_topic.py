from make_soup import make_soup
from colorama import Fore, Back, Style


def make_url_from_topic(topic):
    return f'https://languagedrops.com/word/en/english/hebrew/topics/{topic}/'


def find_para(para):
    return [i.text for i in para.find_all('a', class_="topic-word-link")]


def get_data_from_soup(url):
    return make_soup(url).find_all('div', class_='topic-row')




def get_topic_words(topic_name, words_set):
    # words_set = {}
    url = make_url_from_topic(topic_name)
    all_words = get_data_from_soup(url)
    print(f'{Fore.RED}{topic_name = }{Fore.RESET}')
    # with open('drop_words.txt', 'a') as text_file:
    #     text_file.write(f'\n{topic_name = }\n\n')
    for para in all_words:
        words = find_para(para)
        words_set[words[0]] = words[1]
        print(words)
        # with open('drop_words.txt', 'a') as text_file:
        #     text_file.write(", ".join(words) + '\n')
    # print(len(words_set))
    return words_set


if __name__ == '__main__':
    topic_name = 'essential_products'
    get_topic_words(topic_name)

