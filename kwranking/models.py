import db
from sqlalchemy import Column, Integer, String, Float


class Keywords(db.Base):

    __tablename__ = 'keywords'
    id = Column(Integer, primary_key=True)
    keyword = Column(String, nullable=False)
    position = Column(Integer, nullable=True)

    def __init__(self, keyword, position):
        self.keyword = keyword
        self.position = position

    def __repr__(self):
        return f'Keywords({self.keyword}, {self.position})'

    def __str__(self):
        return self.keyword
