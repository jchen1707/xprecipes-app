from flask_sqlalchemy import SQLAlchemy
from app import create_app

app = create_app()
db = SQLAlchemy(app)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=8000)