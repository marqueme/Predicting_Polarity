"""Computes the scores of all TXT files located in the txt_sentoken/pos and
txt_sentoken/neg folders"""
import os
import csv


def run():
    """top-level function"""
    pos_review_folder = "txt_sentoken/pos"
    neg_review_folder = "txt_sentoken/neg"
    result_pos_folder = {}
    result_neg_folder = {}

    negative_words_path = "negative-words.txt"
    positive_words_path = "positive-words.txt"
    negative_words = get_reference_words(negative_words_path)
    positive_words = get_reference_words(positive_words_path)

    # browse the folders and process each file
    for myfile in os.listdir(pos_review_folder):
        if myfile.endswith(".txt"):
            file_path = pos_review_folder + "/" + str(myfile)
            file_score = compute_score(file_path, positive_words, negative_words)
            result_pos_folder[myfile] = file_score

    for myfile in os.listdir(neg_review_folder):
        if myfile.endswith(".txt"):
            file_path = neg_review_folder + "/" + str(myfile)
            file_score = compute_score(file_path, positive_words, negative_words)
            result_neg_folder[myfile] = file_score

    gen_stats(result_neg_folder, result_pos_folder)


def gen_stats(result_neg_folder, result_pos_folder):
    # generate some stats
    counter = 0
    for score in result_pos_folder.values():
        if score >= 0:
            counter += 1
    accuracy_pos = counter * 100 / len(result_pos_folder.values())
    counter = 0
    for score in result_neg_folder.values():
        if score <= 0:
            counter += 1
    accuracy_neg = counter * 100 / len(result_neg_folder.values())

    # write results to files
    output_pos = "positive_results.csv"
    with open(output_pos, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Filename", "Score"])
        writer.writerows(result_pos_folder.items())

    output_neg = "negative_results.csv"
    with open(output_neg, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Filename", "Score"])
        writer.writerows(result_neg_folder.items())

    print "Positive folder results: Accuracy = " + str(accuracy_pos)
    print str(result_pos_folder)
    print "Negative folder results: Accuracy = " + str(accuracy_neg)
    print str(result_neg_folder)


def get_reference_words(myfile):
    """turns the reference words from the given file into a list for faster access"""
    result = []
    with open(myfile) as f:
        reference_words = f.readlines()
        for reference_word in reference_words:
            if ";" not in reference_word:
                result.append(reference_word.rstrip())
    return result


def compute_score(myfile, positive_words, negative_words):
    """computes the score of file against the positive_words and negative_words lists"""
    score = 0
    with open(myfile) as f:
        content = f.readlines()  # array of all the lines
        for line in content:
            words = line.split()
            for word in words:
                if check_word(word, negative_words):
                    score -= 1
                if check_word(word, positive_words):
                    score += 1
    return score


def check_word(word, reference_list):
    """"check if word belongs to reference_list """
    if word in reference_list:
        return True
    return False


if __name__ == '__main__':
    run()
