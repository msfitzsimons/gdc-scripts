// Snippet to convert JSURL URL back to Percent Encoded URL
var JSURL = require("jsurl");
var URL = process.argv[2];
var Result = escape(JSON.stringify(JSURL.parse(unescape(URL))));
console.log(Result);