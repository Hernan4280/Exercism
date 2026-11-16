from datetime import datetime, timedelta

GIGASEGUNDO = timedelta(seconds=1e9)

def add(moment):
    
    return datetime.fromisoformat(str(moment + GIGASEGUNDO))
