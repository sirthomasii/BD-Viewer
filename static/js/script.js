$( document ).ready(function() {

// 	$('#CallListItem').keydown(function(event) {
//          if (event.keyCode == 13) {
// 					 $('.CallListsubmitButton').trigger('click');
// 					 return false;
//           }
//      });
// 		 $('#FriendCallListItem').keydown(function(event) {
// 	          if (event.keyCode == 13) {
// 	 					 $('.FriendCallListsubmitButton').trigger('click');
// 	 					 return false;
// 	           }
// 	      });
//
//
// 		 	$('#listItem').keydown(function(event) {
// 		          if (event.keyCode == 13) {
// 					 $('.ToDosubmitButton').trigger('click');
// 					  return false;
// 		           }
// 		      });
//
// 	 	$('#WorklistItem').keydown(function(event) {
// 	          if (event.keyCode == 13) {
// 				 $('.WorkToDosubmitButton').trigger('click');
// 				  return false;
// 	           }
// 	      });
//
// 	$('.ToDosubmitButton').click(function() {
// 		var listItem = $('#listItem').val();
//
// 		$.ajax({
// 			url: '/addTodoListItem',
// 			data: $('#ToDoListForm').serialize(),
// 			type: 'POST',
// 			success: function(response){
// 				console.log(response);
// 			},
// 			error: function(error){
// 				console.log(error);
// 			}
// 		});
// 		$("#listItem").val("");
//
// 			getTodoList();
// 	});
//
// 	$('.WorkToDosubmitButton').click(function() {
// 		var listItem = $('#WorklistItem').val();
//
// 		$.ajax({
// 			url: '/addWorkTodoListItem',
// 			data: $('#WorkToDoListForm').serialize(),
// 			type: 'POST',
// 			success: function(response){
// 				console.log(response);
// 			},
// 			error: function(error){
// 				console.log(error);
// 			}
// 		});
// 		$("#WorklistItem").val("");
//
// 			getWorkTodoList();
// 	});
//
//
// 	$('.CallListsubmitButton').click(function() {
// 		var listItem = $('#CallListItem').val();
// 		$.ajax({
// 			url: '/addCallListItem',
// 			data: $('#CallListForm').serialize(),
// 			type: 'POST',
// 			success: function(response){
// 				console.log(response);
// 			},
// 			error: function(error){
// 				console.log(error);
// 			}
// 		});
// 		$("#CallListItem").val("");
//
// 			getCallList();
// 	});
// 	$('.FriendCallListsubmitButton').click(function() {
// 			var listItem = $('#FriendCallListItem').val();
// 			$.ajax({
// 				url: '/addFriendCallListItem',
// 				data: $('#FriendCallListForm').serialize(),
// 				type: 'POST',
// 				success: function(response){
// 					console.log(response);
// 				},
// 				error: function(error){
// 					console.log(error);
// 				}
// 			});
// 			$("#FriendCallListItem").val("");
//
// 				getFriendCallList();
// 		});
//
// 	$('.TodoClearButton').click(function() {
// 		if (confirm('Are you sure ?')) {
// 		$.ajax({
// 			url: '/clearTodoList',
// 			type: 'POST',
// 			success: function(response){
// 				console.log(response);
// 			},
// 			error: function(error){
// 				console.log(error);
// 			}
// 		});
// 			getTodoList();
// 			}
// 	});
// 	$('.CallListClearButton').click(function() {
// 		if (confirm('Are you sure ?')) {
// 		$.ajax({
// 			url: '/clearCallList',
// 			type: 'POST',
// 			success: function(response){
// 				console.log(response);
// 			},
// 			error: function(error){
// 				console.log(error);
// 			}
// 		});
// 			getCallList();
// 			}
// 	});
// $(document).on('click', '.todoListItem', function(){
// 	var postdata = {item: $(this).html(), itemID: $(this).attr("id")};
// 		$.ajax({
// 			url: '/clearTodoItem',
// 			data: postdata,
// 			type: 'POST',
// 			success: function(response){
// 				console.log(response);
// 			},
// 			error: function(error){
// 				console.log(error);
// 			}
// 		});
// 			getTodoList();
// 	});
//
// 	$(document).on('click', '.WorktodoListItem', function(){
// 		var postdata = {item: $(this).html(), itemID: $(this).attr("id")};
// 			$.ajax({
// 				url: '/clearWorkTodoItem',
// 				data: postdata,
// 				type: 'POST',
// 				success: function(response){
// 					console.log(response);
// 				},
// 				error: function(error){
// 					console.log(error);
// 				}
// 			});
// 				getWorkTodoList();
// 		});
//
//
// 	$(document).on('click', '.addNoteButton', function(){
// 		var postdata = {noteName: $("#noteName").val(), noteContent: $("#noteContent").val()};
// 			$.ajax({
// 				url: '/addNote',
// 				data: postdata,
// 				type: 'POST',
// 				success: function(response){
// 					console.log(response);
// 				},
// 				error: function(error){
// 					console.log(error);
// 				}
// 			});
// 				getNotes();
// 		});
//
//
// 		$(document).on('click', '.CallListItem', function(){
// 			var postdata = {item: $(this).html(), itemID: $(this).attr("id")};
// 				$.ajax({
// 					url: '/sendCallListItemToBottom',
// 					data: postdata,
// 					type: 'POST',
// 					success: function(response){
// 						console.log(response);
// 					},
// 					error: function(error){
// 						console.log(error);
// 					}
// 				});
// 					getCallList();
// 			});
//
// 			$(document).on('click', '.FriendCallListItem', function(){
// 				var postdata = {item: $(this).html(), itemID: $(this).attr("id")};
// 					$.ajax({
// 						url: '/sendFriendCallListItemToBottom',
// 						data: postdata,
// 						type: 'POST',
// 						success: function(response){
// 							console.log(response);
// 						},
// 						error: function(error){
// 							console.log(error);
// 						}
// 					});
// 						getFriendCallList();
// 				});
//
// 	$('.calendarEventButton').click(function() {
// 		$.ajax({
// 			url: '/createEvent',
// 			data: $('#calendarForm').serialize(),
// 			type: 'POST',
// 			success: function(response){
// 				console.log(response);
// 				location.reload();
//
// 			},
// 			error: function(error){
// 				console.log(error);
// 				console.log(data);
// 			}
// 		});
// 	});



});
