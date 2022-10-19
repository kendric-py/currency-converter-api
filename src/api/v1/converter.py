from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.utils.central_bank_rate import ParserXmlRatesBank
from core.schema import currency_schema
from core.database.connect import create_async_connection

from core.utils.calculate import calculate_currencies
from core.database import queries


router = APIRouter(prefix='/converter')


@router.post('/update_currencies_list')
async def updater_currencies_list(
    central_bank: ParserXmlRatesBank = Depends(),
    session: AsyncSession = Depends(create_async_connection)
):
    all_currencies = central_bank.get_all_currencies()
    for currency in all_currencies:
        await queries.save_currency(session, currency.get('var_code'))
    return({'status': 'OK'})


@router.get('/currencies')
async def get_currencies_list(session: AsyncSession = Depends(create_async_connection)):
    """
    <b>This endpoint, returned list currencies from database!

    No arguments</b>
    """
    currencies = await queries.get_currency_list(session)
    return(currencies)


@router.get('/rates')
async def calculate_rate(
    from_currency: str, 
    to_currency: str, 
    value: float | int,
    central_bank: ParserXmlRatesBank = Depends()
):
    """
    <b>This endpoint, returned convert currency value result</b>
    
    <code>from_currency - the currency from which we convert</code>

    <code>to_currency - the currency to convert to</code>

    <code>value - the value to convert</code>
    """

    from_currency_values = central_bank.get_currency_rate(from_currency)
    to_currency_values = central_bank.get_currency_rate(to_currency)
    result = calculate_currencies(
        from_currency, to_currency, value, 
        from_currency_values, to_currency_values
    )
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found currency')
    return(currency_schema.Result(result=result))
    

    
