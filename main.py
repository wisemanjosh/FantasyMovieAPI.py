from flask import Flask, request, jsonify

app = Flask(__name__)

fantasy_movies_list = [
    {
        "id": 0,
        "director": "Tarsem",
        "language": "English",
        "title": "The Fall",
    },
    {
        "id": 1,
        "director": "Michael J. Bassett",
        "language": "English",
        "title": "Solomon Kane",
    },
    {
        "id": 2,
        "director": "John Milius",
        "language": "English",
        "title": "Conan The Barbarian",
    },
    {
        "id": 3,
        "director": "Rob Minkoff",
        "language": "English",
        "title": "The Forbidden Kingdom",
    },
    {
        "id": 4,
        "director": "Terry Gilliam",
        "language": "English",
        "title": "The Imaginarium Of Doctor Parnassus",
    },
    {
        "id": 5,
        "director": "Andrew Adamson",
        "language": "English",
        "title": "The Chronicles Of Narnia: Prince Caspian",
    },
    {
        "id": 6,
        "director": "Peter Jackson",
        "language": "English",
        "title": "The Hobbit: An Unexpected Journey",
    },
    {
        "id": 7,
        "director": "Tim Burton",
        "language": "English",
        "title": "Miss Peregrine's Home for The Peculiar CHildren",
    },
    {
        "id": 8,
        "director": "Wolfgang Petersen",
        "language": "English",
        "title": "The Neverending Story",
    },
    {
        "id": 9,
        "director": "Luc Besson",
        "language": "English",
        "title": "The Extraordinary Adventures Of Adele Blanc-Sec Story",
    },
    {
        "id": 10,
        "director": "Gore Verbinski",
        "language": "English",
        "title": "Pirates Of The Caribbean: The Curse Of The Black Pearl",
    }]

@app.route('/movies', methods=["GET", "POST", "PUT", "DELETE"])
def movies():
    if request.method == "GET":
        if len(fantasy_movies_list) > 0:
            return jsonify(fantasy_movies_list)
        else:
            "Nothing Found", 404

    if request.method == "POST":
         new_director = request.form["director"]
         new_lang = request.form["language"]
         new_title = request.form["title"]
         iD = fantasy_movies_list[-1]["id"]+1

         new_obj = {
             "id": iD,
             "director": new_director,
             "language": new_lang,
             "title": new_title
         }
         fantasy_movies_list.append(new_obj)
         return jsonify(fantasy_movies_list), 201

if __name__ == "__main__":
    app.run()
