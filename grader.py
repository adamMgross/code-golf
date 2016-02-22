import os
import filecmp
import subprocess

problem_weights = [1, 2, 2, 2, 2, 3]
submitters_directory = os.getcwd() + '/submissions/'
code_submissions_dir = os.getcwd() + '/code-submissions/'
output_submissions_dir = os.getcwd() + '/output-submissions/'
correct_outputs_dir = os.getcwd() + '/correct-outputs/'
submitters = {}
PENALTY = 1000


# make a map containing the names of all of the submitters
def create_contestant_repo():
    for dirName, subdirList, fileList in os.walk(submitters_directory):
        for filename in fileList[1:]:
            name = filename.split('.')[0]
            submitters[name] = {}


# sort output and code submissions into their respective folders
def sort_submissions():
    for dirName, subdirList, fileList in os.walk(submitters_directory):
        for fname in fileList[1:]:
            extension = fname.split('.')[2]
            if extension == 'txt':
                bash_args = ['cp', submitters_directory + fname, output_submissions_dir + fname]
                subprocess.call(bash_args)
            else:
                bash_args = ['cp', submitters_directory + fname, code_submissions_dir + fname]
                subprocess.call(bash_args)


# count the characters in a file
def count_file_chars(filename):
    res = subprocess.check_output(['wc', '-c', filename])
    space_count = 0
    while res[space_count] == ' ':
        space_count += 1
    return int(res[space_count:].split(' ')[0])


# compare submitted output to official correct output
# assumes output file only contains one number
def compare(file1, file2):
    try:
        diff = subprocess.check_output(['diff', file1, file2, '--strip-trailing-cr'])
        return True
    except:
        subprocess.CalledProcessError
        return False


# finds number in filename
def parse_for_num(filename):
    return filename.split('.')[1]


# determine submitter's score for each problem, return a list of their scores for each problem
def score_submitter(submitter_name):
    overall_scores = [0, 0, 0, 0, 0, 0]
    correctness_scores = [0, 0, 0, 0, 0, 0]
    character_counts = [0, 0, 0, 0, 0, 0]
    for dirName, subdirList, fileList in os.walk(output_submissions_dir):
        for filename in fileList:
            if filename.split('.')[0] == submitter_name:
                problem_number = parse_for_num(filename)
                if problem_number != '5':
                    submit_file = output_submissions_dir + filename
                    correct_output_file = correct_outputs_dir + 'official' + '.' + problem_number + '.txt'
                    if compare(submit_file, correct_output_file):
                        correctness_scores[int(problem_number)-1] = problem_weights[int(problem_number)-1]
                    else:
                        correctness_scores[int(problem_number)-1] = 0

    for dirName, subdirList, fileList in os.walk(code_submissions_dir):
        for filename in fileList:
            if filename.split('.')[0] == submitter_name:
                problem_number = int(parse_for_num(filename)) - 1
                character_count = count_file_chars(code_submissions_dir + filename)
                character_counts[problem_number] = character_count

    run_problem_five(submitter_name)
    if compare(os.getcwd() + '/problem5generated/' + submitter_name + '.txt', 'problem5input.txt'):
        correctness_scores[4] = 2
    character_counts[4] += count_file_chars(output_submissions_dir + submitter_name + '.5.txt')

    for problem_num in range(0, len(overall_scores)):
        if correctness_scores[problem_num] == 0:
            overall_scores[problem_num] = PENALTY/problem_weights[problem_num]
        else:
            overall_scores[problem_num] = character_counts[problem_num]/problem_weights[problem_num]

    submitters[submitter_name]['char_count'] = character_counts
    submitters[submitter_name]['correctness'] = correctness_scores
    submitters[submitter_name]['overall_score'] = sum(overall_scores)

    return submitters[submitter_name]['overall_score']


def solve_first_problem(s):
    num=0
    for c in s:
        if c=='a':
            num+=2
        if c=='d':
            num-=1
        if c=='m':
            num*=2
        if c=='o':
            return num


def run_problem_five(submitter_name):
    i=open(output_submissions_dir + '/' + submitter_name + '.5.txt', 'r')
    o=open(os.getcwd() + '/problem5generated/' + submitter_name + '.txt', 'w')
    s=i.readline()
    while s!='':
        o.write(str(solve_first_problem(s))+'\n')
        s=i.readline()
    o.close()
    i.close()

# associate all names of the submitters with a list containing their score
def score_all():
    for name in submitters:
        score_submitter(name)

def grade():

    #cleanup folders in case they have contents
    subprocess.call(['rm', '-r', os.getcwd() + '/code-submissions'])
    subprocess.call(['rm', '-r', os.getcwd() + '/problem5generated'])
    subprocess.call(['rm', '-r', os.getcwd() + '/output-submissions'])
    subprocess.call(['mkdir', 'code-submissions'])
    subprocess.call(['mkdir', 'output-submissions'])
    subprocess.call(['mkdir', 'problem5generated'])

    print '\nGrading...'
    scores = {}
    create_contestant_repo()
    sort_submissions()
    score_all()
    out = open('scores.txt', 'w')
    for player in submitters:
        out.write('\n' + player)
        print '\n' + player
        for score in submitters[player]:
            out.write('\n\t' + score + ': ' + str(submitters[player][score]))
            print '\t' + score + ': ' + str(submitters[player][score])
    out.write('\n')

    for player in submitters:
        scores[submitters[player]['overall_score']] = player

    ordered_scores = []
    for key in scores:
        ordered_scores.append((key, scores[key]))
        ordered_scores = sorted(ordered_scores)

    out.write('\n\nResults:\n------------------------\n')
    count = 1
    for elem in ordered_scores:
        out.write(str(count) + '. ' + elem[1] + '-' + str(elem[0]) +'\n')
        count += 1
    out.close()

grade()
