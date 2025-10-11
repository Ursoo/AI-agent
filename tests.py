from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


def test():
    print("Results for current directory:")
    print(get_files_info("calculator", "."))

    print("Results for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))

    print("Results for '/bin' directory:")
    print(get_files_info("calculator", "/bin"))

    print("Results for '../' directory:")
    print(get_files_info("calculator", "../"))

def test_file_content():
    #print("result for lorem ipsum file: ")
    #print(get_file_content("calculator", "lorem.txt"))
    print("result for main file: ")
    print(get_file_content("calculator", "main.py"))
    print("result for 'calculator.py': ")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("result for '/bin/cat' file: ")
    print(get_file_content("calculator", "/bin/cat"))
    print("result for 'pkg/does_not_exist.py' file: ")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    #test()
    test_file_content()