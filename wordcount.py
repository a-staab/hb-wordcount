
def importing_words(file_name):
    log_file = open(file_name)
    all_words = []

    for line in log_file:
        words = line.rstrip().split()
        all_words.extend(words)

    log_file.close()

    print clean_list

importing_words("test.txt")
