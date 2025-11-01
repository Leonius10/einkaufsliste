from flask import Flask, render_template, request, redirect

app = Flask(__name__)
einkaufsliste = []

@app.route("/", methods=["GET", "POST"])
def home():
    nachricht = ""
    if request.method == "POST":
        aktion = request.form.get("aktion")
        artikel = request.form.get("artikel")
        if aktion == "hinzufügen":
            einkaufsliste.append(artikel)
            nachricht = f"{artikel} hinzugefügt"
        elif aktion == "entfernen":
            if artikel in einkaufsliste:
                einkaufsliste.remove(artikel)
                nachricht = f"{artikel} entfernt"
            else:
                nachricht = f"{artikel} nicht in Liste"
        elif aktion == "anzeigen":
            nachricht = ", ".join(einkaufsliste)
        elif aktion == "ausgeben":
            nachricht = " | ".join(einkaufsliste)
        return redirect("/")
    return render_template("index.html", einkaufsliste=einkaufsliste, nachricht=nachricht)

if __name__ == "__main__":
    app.run(debug=True)
