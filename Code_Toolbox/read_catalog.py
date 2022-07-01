import collections
from datetime import datetime

EQ = collections.namedtuple("EQ", ["mag", "depth", "lon", "lat", "date", "eventID"])


def read_file(file_name):
    print(f"Reading file: {file_name}")

    # open file as read only
    with open(file_name, "r") as f:
        EQ_data = f.readlines()[15:]

    EQ_catalog = []

    for data in EQ_data:
        date = datetime.strptime(data[0:10], "%Y/%m/%d").date()
        mag = data[53:58]
        depth = data[45:52]
        lon = data[33:44]
        lat = data[24:33]
        eventID = data[89:99]

        # print(f"Date: {date}\nMagnitude: {mag}\nDepth: {depth}\nLongitude: {lon}\nLatitude: {lat}\nEvent ID: {eventID}")

        my_EQ = EQ(mag, depth, lon, lat, date, eventID)
        EQ_catalog.append(my_EQ)

    print(f"Returning Earthquake Catalog of length {len(EQ_catalog)}")
    return EQ_catalog