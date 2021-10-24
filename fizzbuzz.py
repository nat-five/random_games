def banner_text(text: str = " ", width: int = 80) -> None:
    """
    Print a centered string with ** on each side.

    :param text: The string to print.
        Asterisk ("*") will result in row of asterisks.
        Whitespace default will result in blank line with ** on each side.
    :param width: The maximum width of the print.
    :raise ValueError: if string larger than specified width.
    """
    if len(text) > width - 4:
        raise ValueError("String '{}' is larger than specified width {}"
                         .format(text, width))
    if text == "*":
        print("*" * width)
    else:
        output_string = "**{}**".format(text.center(width - 4))
        print(output_string)


def fizz_buzz(number: int) -> str:
    """
    Play the game 'fizz buzz'.

    :param number: The number to respond to.
    :return: Return the number that comes after the passed `number`, unless:
    The next number is divisible by 3, then return the word 'fizz'.
    The next number is divisible by 5, then return the word 'buzz'.
    The next number is divisible by both 3 and 5, then return the words
    'fizz buzz'.
    """
    answer = ""
    if number % 3 == 0 and number % 5 == 0:
        answer = "fizz buzz"
    elif number % 3 == 0:
        answer = "fizz"
    elif number % 5 == 0:
        answer = "buzz"
    else:
        answer = str(number)
    return answer


# Introduction to game:
banner_text("*")
banner_text("Let's play Fizz Buzz!")
banner_text("It's a game where you and me take turns in counting from 1 to 100.")
banner_text("You win if we get to 100 without you making any mistake.")
banner_text("Here are the rules:")
banner_text("I start by saying '1'")
banner_text("and then we take turns in answering according to the following rules:")
banner_text("If the number that comes next is divisible by 3,")
banner_text("the answer should be 'fizz'.")
banner_text("If the number that comes next is divisible by 5,")
banner_text("the answer should be 'buzz'.")
banner_text("If the number that comes next is divisible by 3 and 5,")
banner_text("the answer should be 'fizz buzz'.")
banner_text("Otherwise just answer with the next number.")
banner_text("You got it? I'll start!")
banner_text("*")

# computer answer:
# if player answers a number, run function with number + 1
# if player answers with fizz, buzz or fizz buzz, first convert, and then run function with + 1
# player input:
# check if computer + 1 is == to player input
players_number = 96
computers_number = 97
while players_number and computers_number < 100:
    print(fizz_buzz(computers_number))
    players_number += 2
    correct_answer = fizz_buzz(players_number)
    player_answer = input("~ ")
    if correct_answer == str(player_answer):
        computers_number += 2
    else:
        print("GAME OVER")
        break

if players_number or computers_number == 100:
    print("You made it!!! Congratulations!!!")


