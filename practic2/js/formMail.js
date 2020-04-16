$("#sendMail").on("click", function(){
	var email = $("#email").val().trim();
	var name = $("#name").val().trim();
	var phone = $("#phone").val().trim();
	var message = $("#message").val().trim();

	if(email == "") {
		$("#errorMess").text("Веддіть email");
		return false;
	} else if(name == "")  {
		$("#errorMess").text("Веддіть імя");
		return false;
	} else if(phone == "")  {
		$("#errorMess").text("Веддіть телефон");
		return false;
	} else if(message.length < 5)  {
		$("#errorMess").text("Веддіть повідомлення не менше 5 символів");
		return false;
	}

	$.ajax({
		url: 'ajax/mail.php',
		type: 'POST',
		cache: false,
		data: { 'name': name, 'email': email, 'phone': phone, 'message': message },
		dataType: 'html',
		beforeSend: function() {
			$("#sendMail").prop("disabled", true);
		},
		success: function(data) {
			if(!data)
				alert("Були помилки, повідомлення не відправлено");
			else
				$("#mailForm").trigger("reset");
			
			$("#sendMail").prop("disabled", false);
		}
	})
});