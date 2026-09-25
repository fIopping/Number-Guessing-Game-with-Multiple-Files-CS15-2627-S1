import utils
import score

Number_score = 100

secret_number = utils.generate_secret_number()

while True:
    if utils.check_user_guess(secret_number):
        break
    else:
        Number_score = score.lose_points(Number_score)

secret_number = utils.generate_secret_number()

while True:
    if utils.check_user_guess(secret_number):
        break

from root.utils import generate_secret_number, check_user_guess

secret_number = generate_secret_number()

while True:
    if check_user_guess(secret_number):
        break

