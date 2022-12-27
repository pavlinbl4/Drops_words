def write_words_to_file(words_set):
    with open('all_drop_words.txt','a') as text_file:
        for k,v in words_set.items():
            # print(f'{k} ==> {v} \n')
            text_file.write(f'{k} == {v} \n')

if __name__ == '__main__':
    words_set = { 1:'dddd', 2:'ggg'}
    write_words_to_file(words_set)