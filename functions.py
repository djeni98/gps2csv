import datetime

columns = {
    'RMC': ['Date/time UTC', 'Date/time BR', 'X', 'Y',
            'Latitude', 'Longitude'],
    'VTG': ['Knots', 'M/H', 'KM/H'],
    'GGA': ['Latitude', 'Longitude', 'Altitude (m)',
            'Altitude (ft)'],
    'GLL': ['Latitude', 'Longitude', 'Valid?']
}

def RMCData(msg):
    '''
    Date/time UTC, Date/time BR, X, Y, Latitude, Longitude
    '''
    UTC = datetime.datetime.combine(msg.datestamp, msg.timestamp)
    BR = UTC - datetime.timedelta(hours=3)

    return [UTC.isoformat(' '), BR.isoformat(' '), msg.longitude,
            msg.latitude, msg.latitude, msg.longitude]

def VTGData(msg):
    '''
    Knots, M/H, KM/H
    '''
    knot = float(msg.spd_over_grnd_kts)
    knot2mh = 1.15078
    miles = knot2mh * knot

    return [knot, miles, msg.spd_over_grnd_kmph]

def GGAData(msg):
    '''
    Latitude, Longitude, Altitude (m), Altitude (ft)
    '''
    meter2feet = 3.28084
    feet = meter2feet * msg.altitude

    return [msg.latitude, msg.longitude, msg.altitude, feet]

def GLLData(msg):
    '''
    Latitude, Longitude, Valid?
    '''
    status = False
    if msg.status == 'A':
        status = True

    return [msg.latitude, msg.longitude, status]

functions = {
    'RMC': RMCData,
    'VTG': VTGData,
    'GGA': GGAData,
    'GLL': GLLData,
}

