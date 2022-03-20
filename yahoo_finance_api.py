import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
from datetime import datetime


class YahooFinanceAPI():
  def __init__(self) -> None:
    return

  def get_historical(self, name, period_type, period_time, frequency_type, frequency_time):
    my_share = share.Share(name)
    symbol_data = None
    _period_type = None
    _frequency_type = None
    if period_type == "DAY":
      _period_type = share.PERIOD_TYPE_DAY
    
    if frequency_type == "DAY":
      _frequency_type = share.FREQUENCY_TYPE_DAY

    try:
      symbol_data = my_share.get_historical(_period_type,
                                            period_time,
                                            _frequency_type,
                                            frequency_time)
    except YahooFinanceError as e:
      print(e.message)
      sys.exit(1)
  
    return self.convert_historical_data(symbol_data)

  def convert_historical_data(self, symbol_data):
    data = {}
    data['data'] = []
    for i in range(len(symbol_data["timestamp"])):
      record = {}
      record['timestamp'] = datetime.fromtimestamp(symbol_data["timestamp"][i]/1000)
      record['open'] = symbol_data["open"][i]
      record['high'] = symbol_data["high"][i]
      record['low'] = symbol_data["low"][i]
      record['close'] = symbol_data["close"][i]
      record['volume'] = symbol_data["volume"][i]
      data['data'].append(record)
    return data
