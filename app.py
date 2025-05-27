from flask import Flask, request, jsonify, render_template
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Crea una carpeta 'static' si no existe, donde irán tus subcarpetas de imágenes
# (Esto es si decides seguir la convención de Flask más adelante, pero por ahora...)
# NO ES NECESARIO CREARLA SI static_folder=BASE_DIR

# Tu app.py actual:
app = Flask(__name__,
            template_folder=BASE_DIR,
            static_folder=BASE_DIR) # <--- Aquí le dices que la raíz es el estático
                                    # Esto significa que él espera "/static/MessiRecords/Messi5.jpg"
                                    # Aunque físicamente estén en BASE_DIR/MessiRecords/Messi5.jpg

COMENTARIOS_FILE = os.path.join(BASE_DIR, 'comentarios.txt')

@app.route('/')
def messi_page():
    return render_template('Messi.html')

@app.route('/guardar_comentario', methods=['POST'])
def guardar_comentario():
    try:
        data = request.get_json()
        comentario = data.get('comentario')
        if not comentario:
            return jsonify({'success': False, 'message': 'El comentario no puede estar vacío.'}), 400
        with open(COMENTARIOS_FILE, 'a', encoding='utf-8') as f:
            f.write(comentario + '\n')
        return jsonify({'success': True, 'message': '¡Comentario guardado exitosamente!'}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error al guardar el comentario: {e}'}), 500

@app.route('/ver_comentarios', methods=['GET'])
def ver_comentarios():
    comments = []
    try:
        with open(COMENTARIOS_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line:
                    comments.append(stripped_line)
    except FileNotFoundError:
        pass
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error al leer comentarios: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)