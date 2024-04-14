from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta

def get_now_text(fmt = '%Y-%m-%d %H:%M:%S'):
    dtn = datetime.now(timezone.utc)
    dtn_kst = dtn + relativedelta(hours=9)
    return dtn_kst.strftime(fmt)