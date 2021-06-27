#!/usr/bin/env python
#coding=utf-8
  
def read_del_list(path):
    del_list = list()
    with open(path, 'r') as file_handle:
        for row in file_handle:
            del_list.append(row.strip())
    return del_list
  
def filte_file(from_file, to_file, del_list):
    with open(from_file, 'r') as file_handle_from:
        with open(to_file, 'w') as file_handle_to:
            for row in file_handle_from:
                if not any(key_word in row for key_word in del_list):
                    file_handle_to.write(row)
  
if __name__ == '__main__':
    del_list = read_del_list(r"failed.txt")
    filte_file(r"ad.txt", "output.txt", del_list)
