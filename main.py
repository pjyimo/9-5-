# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
score = input("점수를 입력하세요: ")

num_score = int(score)

if 71 <= num_score :
    print("A")

elif 41 <= num_score < 71 :
    print("B")
elif 11 <= num_score < 41 :
    print("C")
else :
    print("D")