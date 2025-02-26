# todo zrobic strone glowna flask
# strona glowna ktora zawiera przycisk start i to co zostalo napisane
# strona glowna
import time

# todo zrobic strone gry
# strona zawiera tytul , licznik czasu, pole na tekst
# pelta ktora porownuje to co jest napisane w inpucie z tym co jest w zapisane
# jesli   jest takie samo to odpala licznik na 10 sekund
# jesli nie jest takie samo to zeruje licznik
# jesli czas sie skonczy to wyrzuca na glowna strone z przyciskiem start i pokazuje to co zostalo napisane, czysci liste

from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap5
from forms import AddWordForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '123123'
bootstrap = Bootstrap5(app)

STORY_POPRZEDNIE = 'start'
STORY_TERAZ = ''
TIME = 10



@app.route('/')
def home():
    return render_template('start.html')


@app.route('/game', methods=['POST', 'GET'])
def game():
    print(TIME)
    while TIME > 0:
        global STORY_POPRZEDNIE
        global STORY_TERAZ
        add_form = AddWordForm(word='')
        if add_form.validate_on_submit():
            STORY_POPRZEDNIE = STORY_TERAZ
            STORY_TERAZ = f'{request.form['statement']}'
            return redirect(url_for('game'))
        return render_template('game.html', form=add_form, story_previous=STORY_POPRZEDNIE, story_now=STORY_TERAZ,
                               time_left=TIME)
    else:
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
