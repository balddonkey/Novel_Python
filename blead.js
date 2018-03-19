
var bleno = require('./lib/bleno')

uuid = 'ffff1111-1111-2222-3333-44445555ffff';
major = 5;
minor = 4;
measurePower = -59;

bleno.startAdvertisingIBeacon(uuid, major, minor, measurePower)
