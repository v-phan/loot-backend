from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def item():
    return jsonify({
    'imgs': [
      'https://bykallevig.com/no/wp-content/uploads/2018/03/dsw-chair-plastic-black-front.jpg',
    ],
    'nameOfSeller': 'Kari Normann',
    'title': 'Stol',
    'description':
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum',
    'category': 'furniture',
    'price': 50,
    'annotation': 'kr',
    'lat': 59.9436653,
    'lng': 10.7532038,
  })

if __name__ == '__main__':
    app.run(debug=True)
