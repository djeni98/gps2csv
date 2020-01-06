import datetime

columns = {
    'RMC': ['Date/time UTC', 'Date/time BR', 'X', 'Y',
            'Latitude', 'Longitude'],
    'VTG': ['Knots', 'M/H', 'KM/H'],
    'GGA': ['Altitude (m)', 'Altitude (ft)'],
    'GLL': ['Valid?']
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
    try:
        knot = float(msg.spd_over_grnd_kts)
        knot2mh = 1.15078
        miles = knot2mh * knot

        return [knot, miles, msg.spd_over_grnd_kmph]
    except:
        return ['', '', '']

def GGAData(msg):
    '''
    Altitude (m), Altitude (ft)
    '''
    meter2feet = 3.28084
    try:
        feet = meter2feet * msg.altitude
        return [msg.altitude, feet]
    except:
        return ['', '']

def GLLData(msg):
    '''
    Valid?
    '''
    status = False
    if msg.status == 'A':
        status = True

    return [status]

functions = {
    'RMC': RMCData,
    'VTG': VTGData,
    'GGA': GGAData,
    'GLL': GLLData,
}

