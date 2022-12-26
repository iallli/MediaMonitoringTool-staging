from datetime import datetime

from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey


class users(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=True, unique=True)
    creation_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    last_login = Column(DateTime, nullable=True)
    password = Column(String(200), nullable=True)


class brands(Base):
    __tablename__ = "brands"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    brand_name = Column(String(100), nullable=True, unique=True)
    competitor_name = Column(String(100), nullable=True, unique=True)
    hashtag = Column(String(100), nullable=True)
    reddit_mentions = Column(JSON, nullable=True)
    news_mentions = Column(JSON, nullable=True)
    creation_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    account_type = Column(String(50), nullable=True, default='trial')
    user_id = Column(Integer, ForeignKey(users.id, ondelete="CASCADE"),
                     nullable=False)
    users = relationship(users)
