import pandas as pd
import pydstk

dstk = pydstk.DSTK()

def geocode_to_df(address_list):
    geocodes = dstk.street2coordinates(address_list)
    clean_geocodes = {k: v for k, v in geocodes.items() if type(v) != type(None)}
    gc_df = pd.DataFrame.from_dict(clean_geocodes,orient='index')
    return gc_df
