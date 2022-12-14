from sqlalchemy.ext.asyncio import AsyncSession

from bot.core.db.base.repo import BaseRepo
from bot.core.db.repository.user import UserRepo


class Repo(BaseRepo):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self.user = UserRepo(session)
