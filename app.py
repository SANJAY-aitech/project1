from flask import Flask, request, redirect, render_template, url_for, session,jsonify
import random
from collections import Counter
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


allNames=''' abirami anbarasu anusiya boobesh darshankrishnakumar darshwana deepika devdharsan dhanuja dharani dharsan dhayalini gopikashri gowtham gowthaman hareini harikishore harish hayagirivan hemaprakash jayadharshini karthikraja kishore kowsigashri madhavan manjari manjuparkavi marikarkuvelraj mathavan mohammedthanseem moniha monish nihash nisanth nithish nivethika parthiban praveen priyadharshini rejinavinnarasi sabinaparveen sanjayraj sanjay sanjeev saran sathyasri shanmugapriya sivanesh sivikshaa sowmiya sridharshan subishclarie sujith surya tharaneesh tharanitharan tulsidevi vimalraj vishnukarthik vishnukumar viswanathan yasvand yogeshkanna devadharshini dhanasekar harish naveenkumar vasanth'''
allNames = allNames.split(' ')


def initialize_game():
    name = random.choice(allNames)
    session["name"] = name
    session["letterGuessed"] = ''
    session["chances"] = len(name)+2
    session["correct"] = 0
    session["flag"] = 0
    session["message"] = "Guess the name of your classmate."
    session["game_state"] = "playing"

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/gamepage")
def gamepage():
    player_name = request.args.get("player_name","Guest")
    session["player_name"] = player_name

    if "name" not in session:
        initialize_game()

    word = session["name"]
    display_word = ["_" for _ in word]

    return render_template("gamepage.html",player_name = player_name,display_word=' '.join(display_word),chances = session["chances"],message=session["message"])

@app.route("/guess",methods=["POST"])
def guess():
    if "name" not in session:
        return redirect(url_for("gamepage"))
    guess_letter = request.form.get("guess","").lower()
    word = session["name"]
    letterGuessed = session["letterGuessed"]
    chances = session["chances"]
    game_state = session["game_state"]

    if game_state != "playing":
        return jsonify({"display_word": word if game_state == "won" else "_ " * len(word),"chances": chances,"message": session["message"],"game_state": game_state
})
    message = ""

    if not guess_letter:
        message = "Please enter a letter!"
    elif not guess_letter.isalpha():
        message = "Enter only a letter!"
    elif len(guess_letter) > 1:
        message = "Enter only a Single letter!"
    elif guess_letter in letterGuessed:
        message = "You have already guessed that letter!"
    else:
        chances -=1
        session["chances"] = chances

        if guess_letter in word:
            letterGuessed += guess_letter
            session["letterGuessed"] = letterGuessed
            message = f"Good guess! '{guess_letter}' is in the name."
        else:
            message = f"Sorry, '{guess_letter}' is not in the name."

        if all(letter in letterGuessed for letter in word):
            message = f"Congratulations, you won! The name was: {word}"
            game_state = "won"
        elif chances == 0:
            message = f"You lost! The name was: {word}"
            game_state = "lost"
    
    session["message"] = message
    session["game_state"] = game_state
    

    display_word = []
    for char in word:
        if char in letterGuessed:
            display_word.append(char)
        else:
            display_word.append('_')
    
    return jsonify({
        "display_word": ' '.join(display_word) if game_state == "playing" else (word if game_state == "won" else ' '.join(display_word)),
        "chances": chances,
        "message": message,
        "game_state": game_state,
    })

@app.route("/reset", methods=["POST"])
def reset():
    word = initialize_game()
    word = session["name"]
    display_word = ['_' for _ in word]
    
    return jsonify({
        "display_word": ' '.join(display_word),
        "chances": session["chances"],
        "message": session["message"],
        "game_state": "playing",
    })

if __name__ == "__main__":
    app.run(debug=True,port=5002)