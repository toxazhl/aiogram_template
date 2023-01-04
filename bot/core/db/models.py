from aiogram.utils.markdown import hlink
from sqlalchemy import BigInteger, Column, DateTime, func

from bot.core.db.base.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True)
    creation_date = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self) -> str:
        return f"User(id={self.id}, phone_number={self.phone_number})"

    def hyperlink(self, name: str) -> str:
        return hlink(name, f"tg://user?id={self.id}")
