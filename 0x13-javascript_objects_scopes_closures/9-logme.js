#!/usr/bin/node

let logNum = 0;

exports.logMe = function (item) {
	console.log(`${logNum}: ${item}`);
	logNum++;
}
