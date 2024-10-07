# run.py
from app import create_app
from database import create_database, create_users_table


app = create_app()
create_database()
create_users_table()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
