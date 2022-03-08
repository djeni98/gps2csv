# gps2csv
Convert GPS nmea file to CSV

## Supported $GP Messages
This project do not support all GPS messages yet.

| Message Type | Used Data |
|---|---|
|RMC|Date, Time, Latitude, Longitude|
|VTG|Heading, Knots, Miles per Hour, Kilometers per Hour|
|GGA|Altitude (m), Altitude (ft)|
|GLL|Status|
