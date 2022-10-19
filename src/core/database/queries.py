from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from sqlalchemy.exc import IntegrityError, PendingRollbackError

from .models import Currency


async def save_currency(session: AsyncSession, currency_name: str) -> Currency:
    currency = Currency(name=currency_name)
    session.add(currency)
    try:
        await session.commit()
    except IntegrityError:
        pass
    except PendingRollbackError:
        pass
    finally:
        return(currency)

async def get_currency_list(session: AsyncSession) -> list[Currency] | list[None]:
    query = select(Currency)
    response = await session.execute(query)
    return(response.scalars().all())


async def get_target_currency(session: AsyncSession, currency_name: str) -> Currency | None:
    query = select(Currency).where(Currency.name.lower() == currency_name.lower())
    response = await session.execute(query)
    return(response.scalars().first())