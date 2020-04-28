import argparse
import json
import os
import textwrap


def generate_diff(path_to_file1, path_to_file2):
    dir = os.path.dirname(__file__)
    file1_name = os.path.join(dir, path_to_file1)
    file2_name = os.path.join(dir, path_to_file2)
    file1 = json.load(open(file1_name))
    file2 = json.load(open(file2_name))
    '''convert dict keys to sets and comparing them'''
    setfile1 = set(file1.keys())
    setfile2 = set(file2.keys())
    '''#get new keys in the second file '+'''
    new_strings = setfile2-setfile1
    new_keys = ''
    for i in new_strings:
        new_keys = new_keys + f'+ {i}: {file2.get(i)}\n'
    '''#completely deleted from the 1st file, -'''
    delete_strings = setfile1-setfile2
    delete_keys = ''
    for i in delete_strings:
        delete_keys = delete_keys + f'- {i}: {file1.get(i)}\n'
    left_strings = setfile1 & setfile2
    '''#strings in both files, need to check for change'''
    change_keys = ''
    same_keys = ''
    for i in left_strings:
        if file1.get(i) == file2.get(i):
            '''#equal values, just print'''
            same_keys = same_keys + f' {i}: {file2.get(i)}\n'
        else:
            '''#print new values'''
            change_keys = change_keys + f'+ {i}: {file2.get(i)}\n' + \
                f'- {i}: {file1.get(i)}\n'
    result = (
        f'{{\n{textwrap.indent(new_keys, "   ")}'
        f'{textwrap.indent(delete_keys,"   ")}'
        f'{textwrap.indent(same_keys, "    ")}'
        f'{textwrap.indent(change_keys, "   ")}}}'
    )
    return result


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
