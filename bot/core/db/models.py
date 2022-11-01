from aiogram.utils.markdown import hlink
from sqlalchemy import func, Column, BigInteger, DateTime, String

from bot.core.db.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True)
    phone_number = Column(String(16))
    creation_date = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self) -> str:
        return f"<User(id={self.id}, name={self.name})>"

    @property
    def hyperlink(self) -> str:
        return hlink(self.name, f"tg://user?id={self.id}")
