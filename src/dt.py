from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta

def get_now_text():
    dtn = datetime.now(timezone.utc)
    dtn_kst = dtn + relativedelta(hours=9)
    fmt = '%Y-%m-%d %H:%M:%S'
    return dtn_kst.strftime(fmt)