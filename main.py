from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

data = pickle.load(open('data.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommendation(domain):
    if domain not in data['Area_of_Interest_1'].values:
        return f"Domain '{domain}' not found in the dataset."

    domain_data = data[data['Area_of_Interest_1'] == domain]
    domain_indices = domain_data.index
    idx = domain_indices[0]
    similarity_scores = similarity[idx]
    similar_indices = np.argsort(similarity_scores)[::-1]

    recommended_employees = [
        {"Ename": data.loc[i, 'Ename']} for i in similar_indices[:20]
    ]

    return recommended_employees

@app.route('/recommend', methods=['POST'])
def recommend_api():

    request_data = request.get_json()
    domain = request_data.get('domain')
    result = recommendation(domain)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
