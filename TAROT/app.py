from flask import Flask, render_template, request
from cards import drawMajor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        card1_img = f"static/IMG/default_1.jpg",
        card2_img = f"static/IMG/default_2.jpg",
        card3_img = f"static/IMG/default_3.jpg"
        )


@app.route('/draw', methods=['POST'])
def process():
    my_deck = drawMajor(3)
    card1 = my_deck[0]
    card1_title, card1_description, card1_standing, card1_laying = card1[0], card1[1], card1[2], card1[3]
    card1_img = card1[4]
    card1_img = f"static/IMG/{card1_img}"
    card2 = my_deck[1]
    card2_title, card2_description, card2_standing, card2_laying = card2[0], card2[1], card2[2], card2[3]
    card2_img = card2[4]
    card2_img = f"static/IMG/{card2_img}"
    card3 = my_deck[2]
    card3_title, card3_description, card3_standing, card3_laying = card3[0], card3[1], card3[2], card3[3]
    card3_img = card3[4]
    card3_img = f"static/IMG/{card3_img}"

    return render_template(
        'index.html',
        button_pressed = True,
        card1_title = card1_title + " - " + card1_description,
        card1_standing = card1_standing,
        card1_laying = card1_laying,
        card1_img = card1_img,
        card2_title = card2_title + " - " + card2_description,
        card2_description = card2_description,
        card2_standing = card2_standing,
        card2_laying = card2_laying, 
        card2_img = card2_img, 
        card3_title = card3_title + " - " + card3_description,
        card3_description = card3_description,
        card3_standing = card3_standing,
        card3_laying = card3_laying,
        card3_img = card3_img
        )

if __name__ == '__main__':
    app.run(debug=True)