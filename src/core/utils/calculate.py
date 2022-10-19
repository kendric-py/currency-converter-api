def calculate_currencies(
    from_currency: str,
    to_currency: str,
    value: int,
    from_currency_values: dict, 
    to_currency_values: dict
) -> float | None:
    from_currency_value = from_currency_values.get('value')
    from_currency_nominal = from_currency_values.get('nominal')
    to_currency_value = to_currency_values.get('value')
    to_currency_nominal = to_currency_values.get('nominal')
    
    if not(from_currency_values) and from_currency.lower() != 'ru':
        return None
    if not(to_currency_values) and to_currency.lower() != 'ru':
        return None
    if (from_currency.lower() != 'ru' and from_currency_value) and (to_currency.lower() != 'ru' and to_currency_value):
       result = ((from_currency_value/from_currency_nominal) / (to_currency_value/to_currency_nominal))*value
    else:
        result = from_currency_value*value if to_currency.lower() == 'ru' else value/to_currency_value
    
    return(result)