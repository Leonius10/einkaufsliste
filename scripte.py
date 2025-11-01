from flask import Flask, render_template, request, redirect

app = Flask(__name__)

einkaufsliste = []

def einkaufsliste_programm(aktion, artikel):
    # Dein originaler Code, nur ohne input(), wir geben Werte rein
    if aktion == "hinzufügen":
        if artikel in einkaufsliste:
            # hier setzen wir einfach so, dass NICHT erneut gefragt wird
            # (weil input im Web nicht geht)
            einkaufsliste.append(artikel)
            return f"Der Artikel {artikel} wurde hinzugefügt (war schon drin)"
        else:
            einkaufsliste.append(artikel)
            return f"Der Artikel {artikel} wurde hinzugefügt"

    elif aktion == "entfernen":
        if artikel in einkaufsliste:
            einkaufsliste.remove(artikel)
            return f"Der Artikel {artikel} wurde entfernt"
        else:
            return "Diesen Artikel gibt es nicht in der Liste"

    elif aktion == "anzeigen":
        return str(einkaufsliste)

    elif aktion == "ausgeben":
        return " | ".join(einkaufsliste)

    else:
        return "Ungültige Aktion"


@app.route("/", methods=["GET", "POST"])
def home():
    nachricht = ""

    if request.method == "POST":
        aktion = request.form.get("aktion")
        artikel = request.form.get("artikel")

        nachricht = einkaufsliste_programm(aktion, artikel)

        if aktion == "ausgeben":
            return render_template("index.html",
                                   einkaufsliste=einkaufsliste,
                                   nachricht="Liste ausgegeben, Programm beendet")

        return redirect("/")

    return render_template("index.html",
                           einkaufsliste=einkaufsliste,
                           nachricht="")


if __name__ == "__main__":
    app.run(debug=True)
