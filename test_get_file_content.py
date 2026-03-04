from functions.get_file_content import get_file_content
from config import MAX_CHARS

print("Testing lorem.txt")
result1 = get_file_content("calculator", "lorem.txt")
print(f"Length: {len(result1)}")
if "truncated" in result1:
    print("Truncation message found!")
else:
    print("Truncation message missing!")

result2 = get_file_content("calculator", "main.py")
result3 = get_file_content("calculator", "pkg/calculator.py")
result4 = get_file_content("calculator", "/bin/cat")
result5 = get_file_content("calculator", "pkg/does_not_exist.py")


def test():
    print("Result for main.py:")
    print(result2)

    print("Result for 'pkg/calculator.py':")
    print(result3)

    print("Result for '/bin/cat':")
    print(result4)

    print("Result for 'pkg/does_not_exist':")
    print(result5)


if __name__ == "__main__":
    test()
