$( document ).ready(function() {
	$('.submitButton').click(function() {
		var listItem = $('#listItem').val();

		$.ajax({
			url: '/addTodoListItem',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
		$("#listItem").val("");

			getTodoList();
	});

	$('.clearButton').click(function() {
		if (confirm('Are you sure ?')) {
		$.ajax({
			url: '/clearTodoList',
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
			getTodoList();
			}
	});
$(document).on('click', '.todoListItem', function(){
	var postdata = {item: $(this).html(), itemID: $(this).attr("id")};
		$.ajax({
			url: '/clearTodoItem',
			data: postdata,
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
			getTodoList();
	});
	$('.calendarEventButton').click(function() {
		$.ajax({
			url: '/createEvent',
			data: $('#calendarForm').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
				location.reload();

			},
			error: function(error){
				console.log(error);
				console.log(data);
			}
		});
	});
});
