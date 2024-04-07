from flask import Flask, render_template, request
from WordPredict import generate_next_words
from GrammCheck import grammar
from SpellCheck import spellcheck


app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def index():
    prompt = request.form.get('prompt', '') if request.method == 'POST' else ''
    generated_text = None
    spelling_errors = None
    grammar_errors = None

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'generate':
            generated_text = generate_next_words(prompt,1)
        elif action == 'spell':
            spelling_errors = spellcheck(prompt)
        elif action == 'grammar':
            grammar_errors = grammar(prompt)

    return render_template('index.html', prompt=prompt, generated_text=generated_text, spelling_errors=spelling_errors, grammar_errors=grammar_errors)

if __name__ =="__main__":
    app.run(debug=True)
