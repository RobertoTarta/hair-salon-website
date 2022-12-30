from app import db, User, app

with app.app_context():
    db.create_all()

    # Populate database with some entries
    admin = User(username='admin', email='roberto.tarta10@e-uvt.ro', )
    regular_user = User(username='user', email='user@example.com', )

    db.session.add(admin)
    db.session.add(regular_user)

    db.session.commit()