# sample_data.py
from app import db, app, Donor, Recipient

donors = [
    {"name": "John Doe", "blood_group": "A+", "contact": "9876543210", "email": "john@example.com", "city": "Bangalore"},
    {"name": "Jane Smith", "blood_group": "B+", "contact": "9876543211", "email": "jane@example.com", "city": "Mumbai"},
    {"name": "Mike Johnson", "blood_group": "O-", "contact": "9876543212", "email": "mike@example.com", "city": "Delhi"},
    {"name": "Emily Davis", "blood_group": "AB+", "contact": "9876543213", "email": "emily@example.com", "city": "Chennai"},
    {"name": "David Wilson", "blood_group": "A-", "contact": "9876543214", "email": "david@example.com", "city": "Kolkata"}
]

recipients = [
    {"name": "Alice Brown", "blood_group": "A+", "contact": "8765432101", "email": "alice@example.com", "city": "Bangalore"},
    {"name": "Bob Martin", "blood_group": "B+", "contact": "8765432102", "email": "bob@example.com", "city": "Mumbai"},
    {"name": "Carol White", "blood_group": "O-", "contact": "8765432103", "email": "carol@example.com", "city": "Delhi"},
    {"name": "Eve Thompson", "blood_group": "AB+", "contact": "8765432104", "email": "eve@example.com", "city": "Chennai"},
    {"name": "Frank Harris", "blood_group": "A-", "contact": "8765432105", "email": "frank@example.com", "city": "Kolkata"}
]

with app.app_context():
    # Insert donors if not exist
    for d in donors:
        existing = Donor.query.filter_by(name=d['name'], contact=d['contact']).first()
        if not existing:
            donor = Donor(**d)
            db.session.add(donor)

    # Insert recipients if not exist
    for r in recipients:
        existing = Recipient.query.filter_by(name=r['name'], contact=r['contact']).first()
        if not existing:
            recipient = Recipient(**r)
            db.session.add(recipient)

    db.session.commit()
    print("Sample data inserted successfully (duplicates skipped)!")