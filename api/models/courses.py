from ..utils import db

class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    teacher = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"<Course {self.name}>"
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)