"use strict";
const merge = require("webpack-merge");
const prodEnv = require("./prod.env");

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  // urlVGI: '"http://localhost:3001"',
  urlVGI: '"https://pauliceia.unifesp.br/api/vgi"',
  // urlGeoserverPauliceia: '"http://localhost:9021/geoserver/pauliceia"',
  urlGeoserverPauliceia: '"http://geoserver:8080/geoserver/pauliceia"',
  urlGeoserveOther: '"http://geoserver:8080/geoserver/other"',
  urlGeocoding: '"geocoding_api:3000/api/geocoding"',
  keyCripto: '"keytest"',
});
