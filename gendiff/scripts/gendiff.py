import argparse
import json
from gendiff import loader


def generate_diff(file1, file2):
    inner_diff = {}
    '''convert source files' dict keys to sets and compare them'''
    setfile1 = set(file1.keys())
    setfile2 = set(file2.keys())
    '''#get new keys in the second file '+'''
    new_strings = setfile2-setfile1
    for i in new_strings:
        inner_diff['+ ' + i] = file2.get(i)
    '''#completely deleted from the 1st file, -'''
    delete_strings = setfile1-setfile2
    for i in delete_strings:
        inner_diff['- ' + i] = file1.get(i)
    '''#strings in both files, need to check for change'''
    left_strings = setfile1 & setfile2
    for i in left_strings:
        if file1.get(i) == file2.get(i):
            '''#equal values, just print'''
            inner_diff['  ' + i] = file2.get(i)
    for i in left_strings:
        if file1.get(i) != file2.get(i):
            if type(file1.get(i)) == dict and type(file2.get(i)) == dict:
                inner_diff['  ' + i] = generate_diff(
                    file1.get(i), file2.get(i)
                    )
            else:
                inner_diff['+ ' + i] = file2.get(i)
                inner_diff['- ' + i] = file1.get(i)
    return inner_diff


def formatter(inner_diff):
    result = str(json.dumps(inner_diff, indent=2, sort_keys=True))
    return result.replace('"', "").replace(',', "")


def main():
    file1 = "1"
    file2 = "2"
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    file1, file2 = loader.load_file(args.first_file, args.second_file)
    diff = formatter(generate_diff(file1, file2))
    print(diff)


if __name__ == '__main__':
    main()
