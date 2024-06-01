from flask import Flask, render_template, request
from bataille import Player, WarGame

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    condition = {
        'Ace': int(request.form.get('aces', 0)),
        'King': int(request.form.get('kings', 0)),
        'Jack': int(request.form.get('jacks', 0)),
        'Queen': int(request.form.get('queens', 0)),
        '7': int(request.form.get('sevens', 0)),
        '8': int(request.form.get('eights', 0)),
        '9': int(request.form.get('nines', 0)),
        '10': int(request.form.get('tens', 0))
    }
    total_cards = sum(condition.values())

    if total_cards > 16:
        error_message = "The total number of cards must not exceed 16."
        return render_template('index.html', error_message=error_message)





    player1 = Player('Player1')
    player2 = Player('Player2')

    game = WarGame(player1, player2,condition)

    probabilities = game.calculate_probabilities()

    return render_template('result.html', probabilities=probabilities)

if __name__ == '__main__':
    app.run(debug=True)

