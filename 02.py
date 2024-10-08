from collections import deque


def is_palindrome(passed_string: str):
    if len(passed_string) == 0:
        return True
    d = deque(list(passed_string.replace(' ', '').lower()))

    while True:
        if len(d) in (0, 1):
            return True
        if d.pop() != d.popleft():
            return False


palindrome_list = [
    'ababagalamaga',
    'abba',
    'qwertyytrewq',
    'sq32ffdsgsdgsdg',
]

for item in palindrome_list:
    res = 'Is palindrome' if is_palindrome(item) else 'Is not palindrome'
    print(f"'{item}': {res}")
