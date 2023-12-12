#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.filter(e => e === searchElement).length;
  // list.forEach(e => {if (e === searchElement) count++})
  // return count;
};
