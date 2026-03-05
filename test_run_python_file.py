from functions.run_python_file import run_python_file


result1 = run_python_file("calculator", "main.py")
result2 = run_python_file("calculator", "main.py", ["3 + 5"])
result3 = run_python_file("calculator", "tests.py")
result4 = run_python_file("calculator", "../main.py")
result5 = run_python_file("calculator", "nonexistent.py")
result6 = run_python_file("calculator", "lorem.txt")


def test():
    print("Result for 'main.py':")
    print(result1)

    print("Result for running the calculator with 3 + 5 input:")
    print(result2)

    print("Result for 'tests.py':")
    print(result3)

    print("Result for '../main.py':")
    print(result4)

    print("Result for 'nonexistent.py':")
    print(result5)

    print("Result for 'lorem.txt':")
    print(result6)


if __name__ == "__main__":
    test()
