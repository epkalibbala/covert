from datetime import datetime
import pandas as pd

datetime_object = datetime.strptime('Mar 2022', '%b %Y')

date_time = pd.to_datetime(datetime_object, format='%m/%Y')

period = date_time.to_period('m')

print(period)
