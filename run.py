from app import create_app
from app.data.schemas import init_db
from config.settings import Config

# Create Flask application
app = create_app()

# Initialize database
db_session = init_db(app.config['SQLALCHEMY_DATABASE_URI'])

@app.shell_context_processor
def make_shell_context():
    return {
        'app': app,
        'db_session': db_session
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
