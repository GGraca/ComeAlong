
    $("#add-vacancy").click(function(){
        event.preventDefault();
        var vacancy = '<div class="input-group vacancy new">';
        vacancy += '<div class="col-xs-2">';
        vacancy += '<input type="number" class="form-control number" placeholder="0" >';
        vacancy += '</div>';
        vacancy += '<div class="col-xs-9">';
        vacancy += '<input type="text" class="form-control name" placeholder="Name" >';
        vacancy += '</div>';
        vacancy += '<div class="col-xs-1 action">';
        vacancy += '<div class="delete-vacancy">x</div>';
        vacancy += '<div class="undo-vacancy hide"><-</div>';
        vacancy += '</div>';
        $("#vacancies").append(vacancy);
    });

    $(".delete-vacancy").click(function(){
        event.preventDefault();
        $(this).addClass('hide').parent().parent().addClass('delete');
        $(this).parent().find('.undo').removeClass('hide');
    });

    $(".undo-vacancy").click(function(){
        event.preventDefault();
        $(this).addClass('hide').parent().parent().removeClass('delete');
        $(this).parent().find('.delete').removeClass('hide');
    });

    $("#submit-vacancy").click(function(){
        event.preventDefault();
        var error = false;

        // validate fields
        $('.error').remove();
        $('.vacancy').each(function() {
            
            if (!validateVacancy($(this))) {
                error = true;
            }
            
        });

        // if validation errors
        if (!error) {

            $('.vacancy').each(function() {
                if ($(this).hasClass('delete')) {
                    console.log('remove');
                    removeVacancy($(this));
                } else if ($(this).hasClass('old')) {
                    console.log('update');
                    updateVacancy($(this));
                } else if ($(this).hasClass('new')) {
                    console.log('novo');
                    newVacancy($(this));
                }
            });

        }
    });

    function validateVacancy(vac) {
        var number = vac.find('.number');
        var name = vac.find('.name');
        var error = false;

        if(name.val() == '' || name.val().length < 3) {
            name.parent().append('<span class="error">Erro</span>');
            error = true;
        }

        if(number.val() == '' || number.val() <= 0) {
            number.parent().append('<span class="error">Erro</span>');
            error = true;
        }

        if (error) {
            return false
        } else {
            return true; 
        }  
    }

    function removeVacancy(vac) {
        var number = vac.find('.number');
        var name = vac.find('.name');
        var id = vac.attr('id');

        // $.ajax({
        //     url : id + "/delete",

        //     success : function(json) {
        //         console.log("success"); // another sanity check
        //     },

        //     error : function(xhr,errmsg,err) {
        //         console.log(xhr.status + ": " + xhr.responseText);
        //     }
        // });
    }

    function updateVacancy(vac) {
        var number = vac.find('.number');
        var name = vac.find('.name');
        var id = vac.attr('id');

        // $.ajax({
        //     url : id + "/edit",
        //     type : "POST",
        //     data : { title : name, total: number },

        //     success : function(json) {
        //         console.log("success");
        //     },

        //     error : function(xhr,errmsg,err) {
        //         console.log(xhr.status + ": " + xhr.responseText);
        //     }
        // });
    }

    function newVacancy(vac) {
        var number = vac.find('.number').val();
        var name = vac.find('.name').val();

        $.ajax({
            url : "http://localhost:8000/projects/1/vacancies/new/",
            type : "POST",
            data : { title : name, total: number, available: number, csrfmiddlewaretoken:  $("input[name$='csrfmiddlewaretoken']").val() },

            success : function(json) {
                console.log("success");
            },

            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }

	$.ajaxSetup({ 
	     beforeSend: function(xhr, settings) {
	         function getCookie(name) {
	             var cookieValue = null;
	             if (document.cookie && document.cookie != '') {
	                 var cookies = document.cookie.split(';');
	                 for (var i = 0; i < cookies.length; i++) {
	                     var cookie = jQuery.trim(cookies[i]);
	                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
	                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                     break;
	                 }
	             }
	         }
	         return cookieValue;
	         }
	         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
	             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
	         }
	     } 
	});