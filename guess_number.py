import random
from colorama import Fore, Style


def get_input_num():
    while True:
        try:
            length = int(input("How many numbers do you want (1-6)? "))
            if 1 <= length <= 6:
                break
            print("Invalid number")
        except ValueError:
            print("Only numbers")

    return length


def get_random_num(length):
    digits = []

    for _ in range(length):
        digits.append(str(random.randint(1, 9)))

    return ''.join(digits)


def compare_guess(secret, guess, length):
    used_secret = [False] * length
    used_guess = [False] * length
    colored_result = [''] * length

    for i in range(length):
        if guess[i] == secret[i]:
            colored_result[i] = Fore.GREEN + guess[i] + Style.RESET_ALL
            used_secret[i] = True
            used_guess[i] = True

    for i in range(length):
        if used_guess[i]:
            continue

        for j in range(length):
            if not used_secret[j] and guess[i] == secret[j]:
                colored_result[i] = Fore.YELLOW + guess[i] + Style.RESET_ALL
                used_secret[j] = True
                used_guess[i] = True
                break

    for i in range(length):
        if not colored_result[i]:
            colored_result[i] = guess[i]

    print(' '.join(colored_result))

    return guess == secret


def search(secret, length):
    print(f"You have {length + 2} chances of success")

    for chances in range(length + 2, 0, -1):
        guess = input(f"{length} digit: ")
        print(f"You have {chances} chans")

        if len(guess) == length and guess.isdigit():
            print(f"{chances} chances left")

            if compare_guess(secret, guess, length):
                print("Congratulations!!!")
                break

        elif guess.isalpha():
            print("Only numbers")

        elif len(guess) != length:
            print("Wrong length")

    else:
        print("Loss")
        print(f"The correct option {secret}")

        answer = input("Do you want continue (Y/N)? ").lower()
        if answer == "y":
            search(secret, length)


def main():
    length = get_input_num()
    secret = get_random_num(length)

    search(secret, length)


if __name__ == "__main__":
    main()