from brain_games.cli import welcome_user, ask_username, show_error_mistake, congrats_user, ask_user, make_example, compare_answers


def engine(game):
    rounds_won = 0
    welcome_user()
    name = ask_username()
    print(game.RULES)
    while rounds_won < 3:
        task, right_answer = game.get_required_values()
        print(task)
        user_answer = ask_user()
        if compare_answers(user_answer, right_answer):
            rounds_won += 1
            print('Correct!')
        else:
            show_error_mistake(user_answer, right_answer, name)
            break
        if rounds_won == 3:
            congrats_user(name)
