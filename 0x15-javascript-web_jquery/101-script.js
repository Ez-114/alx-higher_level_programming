$(function () {
  // Add item to the list when #add_item is clicked
  $('DIV#add_item').click(() => { $('UL.my_list').append('<li>Item</li>'); });

  // Remove the last item from the list when #remove_item is clicked
  $('DIV#remove_item').click(() => { $('UL.my_list li:last').remove(); });

  // Clear all items from the list when #clear_list is clicked
  $('DIV#clear_list').click(() => { $('UL.my_list').empty(); });
});
