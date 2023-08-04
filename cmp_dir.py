from __future__ import print_function
import filecmp
import os.path
import sys

def print_help():
    print("Use : python cmp_dir.py <dir_1> <dir_2> [-a] [-s <file>]")
    print("dir_1 and dir_2 : directories to compare")
    print("-a : also compare data inside files")
    print("-s : save results inside <file>")

def compare_dir_trees(dir1, dir2, compare_file_data, output):

    def compare_dirs(dir1, dir2):
        dirs_cmp = filecmp.dircmp(dir1, dir2)
    
        if dirs_cmp.left_only:
            print("files or subdirs only in %s : %s " % (dir1, dirs_cmp.left_only),
                  file=output)

        if dirs_cmp.right_only:
            print("files or subdirs only in %s : %s " % (dir2, dirs_cmp.right_only),
                  file=output)

        if compare_file_data and dirs_cmp.diff_files:
            print("different files in %s : %s " % (dir1, dirs_cmp.diff_files),
                  file=output)
        
        for common_dir in dirs_cmp.common_dirs:
            new_dir1 = os.path.join(dir1, common_dir)
            new_dir2 = os.path.join(dir2, common_dir)
            compare_dir(new_dir1, new_dir2)

    compare_dirs(dir1, dir2)

def main(argv):
    compare_file_data = False
    file_to_save_results = None

    if '-s' in argv:
        pos = argv.index('-s')
        if pos + 1 < len(argv):
            file_to_save_results = argv[pos + 1]
            del argv[pos:pos+2]

    if '-a' in argv:
        argv.remove('-a')
        compare_file_data = True

    if len(argv) != 3:
        print_help()
        return
    
    dir_a = argv[1]
    dir_b = argv[2]
    
    print("Compare dirs %s and %s" % (dir_a, dir_b))
    print("Start compare")

    if file_to_save_results:
        with open(file_to_save_results, "w") as file:
            compare_dir_trees(dir_a, dir_b, compare_file_data, file)
    else:
        compare_dir_trees(dir_a, dir_b, compare_file_data, sys.stdout)

    print("End compare")
    

if __name__ == '__main__':
    main(sys.argv)