var Blynk = require('blynk-library');

var AUTH = 'QlvbwgyTZXh74m8dz5E6MUNAFpFKmQ3W';

var blynk = new Blynk.Blynk(AUTH);

var v1 = new blynk.VirtualPin(1);
var v9 = new blynk.VirtualPin(9);

v1.on('write', function(param) {
  console.log('V1:', param[0]);
});

v9.on('read', function() {
  v9.write(new Date().getSeconds());
});
