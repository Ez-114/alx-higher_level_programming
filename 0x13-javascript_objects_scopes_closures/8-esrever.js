#!/usr/bin/node
exports.esrever = function (list) {
  // Check if list is valid and has elements
  if (!list || list.length === 0) {
    return [];
  }

  // Initialize an empty array to store reversed elements
  const reversedList = [];

  // Iterate through the original list in reverse order
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]); // Add each element to the reversedList array
  }

  return reversedList; // Return the reversed list
};
