from flask import Flask, request, jsonify, render_template
import os # Necesitamos el módulo os para rutas de archivos

# Obtiene la ruta del directorio actual donde se encuentra app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Crea una instancia de la aplicación Flask.
# Le indicamos a Flask dónde buscar templates y static files.
# La ruta actual (BASE_DIR) será el root para ambos.
app = Flask(__name__,
            template_folder=BASE_DIR, # Flask buscará templates en el directorio base
            static_folder=BASE_DIR)   # Flask buscará archivos estáticos en el directorio base

# Define el nombre del archivo donde se guardarán los comentarios
COMENTARIOS_FILE = os.path.join(BASE_DIR, 'comentarios.txt') # Asegura la ruta completa

@app.route('/')
def messi_page():
    """
    Renderiza la página HTML principal (Messi.html).
    Flask lo buscará directamente en el directorio base.
    """
    return render_template('Messi.html')

@app.route('/guardar_comentario', methods=['POST'])
def guardar_comentario():
    """Recibe y guarda un comentario."""
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
    """Lee y devuelve los comentarios."""
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
    app.run(debug=True)