(function($) {
    "use strict";

    if ($('[data-toggle="tooltip"]').length > 0) {
        $('[data-toggle="tooltip"]').tooltip();
    }

   var $container = $('#projects .row').isotope({
     itemSelector: '.project-container',
     getSortData: {
       name: '.name',
       category: '[data-category]'
     }
   });

   var current;
   $('.section-title .select1').on('click', function(){
      current = $(this).find('.selection').html();
      var replace = '';

      for (i = 0; i < current.length; i++) {
         replace += '_';
      }
      $(this).find('.selection').html(replace);

      $('.select-options').addClass('open');
   });

   $('.select-options ul li').on('click', function(){
      event.stopPropagation();
      $('.select-options ul li').removeClass('selected');
      $(this).addClass('selected');

      var replace = $(this).html();
      var replace_slug = replace.replace(' ','-').toLowerCase();

      if (replace_slug == 'all') {
         replace_slug = 'project-container';
      }

      $('.section-title .select').find('.selection').html(replace);
      $('.select-options').removeClass('open');

      $container.isotope({ filter: '.' + replace_slug });
   });

   $('.select-options').on('click', function(){
      $('.select-options').removeClass('open');
      $('.section-title .select').find('.selection').html(current);
   });

   if($('.page.project-single').length){
      $('.page.project-single .section.cover').css('margin-top', - $('aside .logo').height());
      $('.page.project-single .section.cover .description').css('margin-top', $('aside .logo').height());
   }

    // name your elements here
    var stickyElement   = '.info-fixed',   // the element you want to make sticky
        bottomElement   = 'footer'; // the bottom element where you want the sticky element to stop (usually the footer)
    // make sure the element exists on the page before trying to initalize
    if($( stickyElement ).length){
        var affix;
        $( stickyElement ).each(function(){
            if ($('.edit-project').length) {
              affix = $(this).offset().top-20;
            } else {
              affix = $("#hero").height()+61;
            }

            // let's save some messy code in clean variables
            // when should we start affixing? (the amount of pixels to the top from the element)
            var fromTop = affix,
                // where is the bottom of the element?
                fromBottom = $( document ).height()-($( this ).offset().top + $( this ).outerHeight()),
                // where should we stop? (the amount of pixels from the top where the bottom element is)
                // also add the outer height mismatch to the height of the element to account for padding and borders
                stopOn = $( document ).height()-( $( bottomElement ).offset().top-125)+($( this ).outerHeight() - $( this ).height());
            // if the element doesn't need to get sticky, then skip it so it won't mess up your layout
            if( (fromBottom-stopOn) > 200 ){
                // let's put a sticky width on the element and assign it to the top
                $( this ).css('width', $( this ).parent().width()).css('top', 0).css('position', '');
                // assign the affix to the element
                $( this ).affix({
                    offset: {
                        // make it stick where the top pixel of the element is
                        top: fromTop,
                        // make it stop where the top pixel of the bottom element is
                        bottom: stopOn
                    }
                // when the affix get's called then make sure the position is the default (fixed) and it's at the top
                }).on('affix.bs.affix', function(){ $( this ).css('top', 0).css('position', ''); });
            }
            // trigger the scroll event so it always activates
            $( window ).trigger('scroll');
        });
    }

    // Feedback

    $(document).on('click', '#submit-feedback', function(){
        event.preventDefault();
        $("#feedback-error, #feedback-success").hide();

        var topic = $('#topic').val();
        var email = $('#feedback-email').val();
        var message = $('#message').val();

        if (topic == '' || email == '' || message == '') {
            $("#feedback-error").html('Please fill in all fields properly.');
            $("#feedback-error").show();
            return false
        }

        if (!validateEmail(email)) {
            $("#feedback-error").html('Please enter a valid email.');
            $("#feedback-error").show();
            return false
        }

        contact(topic,email,message);
    });

    function contact(topic,email,message) {
        $.ajax({
            url : "/contact/",
            type : "POST",
            data : { topic : topic, message: message, email: email },

            success : function(json) {
                if (json == 'error') {
                    $("#feedback-error").html('Error occurred. Please try again later.');
                    $("#feedback-error").show();
                } else if (json == 'success') {
                    $("#feedback-success").html("Thank you for your feedback. We'll be in touch soon :)");
                    $("#feedback-success").show();
                    
                    setTimeout(function(){ 
                        $('#feedback-md').modal('hide');
                    }, 2000);
                }
            },

            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }

    // Login

    $(document).on('click', '#submit-signin', function(){
        event.preventDefault();
        var user = $('#signin-username').val();
        var pass = $('#signin-password').val();
        login(user,pass);
    });

    function login(user,pass) {
        $.ajax({
            url : "/login/",
            type : "POST",
            data : { username : user, password: pass },

            success : function(json) {
                if (json == 'error') {
                    $("#signin-error").show();
                } else if (json == 'success') {
                    window.location = document.URL
                }
            },

            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }

    // Register

    $(document).on('click', '#submit-signup', function(){
        event.preventDefault();
        $("#signup-error").hide();

        var firstname = $('#firstname').val();
        var lastname = $('#lastname').val();
        var username = $('#username').val();
        var email = $('#email').val();
        var password = $('#password').val();
        var password2 = $('#reenterpassword').val();

        if (firstname == '' || lastname == '' || username == '' || email == '' || password == '' || password2 == '') {
            $("#signup-error").html('Please fill in all fields properly.');
            $("#signup-error").show();
            return false
        }

        if (!validateEmail(email)) {
            $("#signup-error").html('Please enter a valid email.');
            $("#signup-error").show();
            return false
        }

        if (password != password2) {
            $("#signup-error").html('Both passwords must match.');
            $("#signup-error").show();
            return false
        }

        register(firstname,lastname,username,email,password);
    });

    function register(firstname,lastname,username,email,password) {
        $.ajax({
            url : "/register/",
            type : "POST",
            data : { firstname : firstname, lastname: lastname, username: username, email: email, password: password, csrfmiddlewaretoken:  $("input[name$='csrfmiddlewaretoken']").val() },

            success : function(json) {
                if (json == 'invalid username') {
                    $("#signup-error").html('Username already in use.');
                    $("#signup-error").show();
                } else if (json == 'invalid email') {
                    $("#signup-error").html('Email already in use.');
                    $("#signup-error").show();
                } else {
                    login(username,password);
                }
            },

            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }

    $(document).on('click', 'a[data-target="#signup-signin-md"]', function(){
        var link = $(this).attr('href');
        if (link == '#signin') {
            $('#signup-signin').find('li').removeClass('active');
            $('#signup-signin').find('li:first-of-type').addClass('active');
            $('#signup').removeClass('active in');
            $('#signin').addClass('active in');
        } else if (link == '#signup') {
            $('#signup-signin').find('li').removeClass('active');
            $('#signup-signin').find('li:last-of-type').addClass('active');
            $('#signin').removeClass('active in');
            $('#signup').addClass('active in');
        }
    });


    function validateEmail(email) {
        var regex = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return regex.test(email);
    }

    // Accept Applications

    $(document).on('submit', '.application-form', function(){
        event.preventDefault();
        var apply = $(this).attr('id');
        var roles = [];

        $('#' + apply + ' input[type="checkbox"]:checked').each(function() {
            roles.push($(this).attr('value'));
            $(this).parent().remove();
        });

        if ($('#' + apply + ' input[type="checkbox"]').length == 0){
            $('#' + apply + '').remove();
        };

        acceptApply(apply, roles);
    });

    function acceptApply(id, roles) {
        $.ajax({
            url : id + "/",
            type : "POST",
            data : { roles: roles, csrfmiddlewaretoken:  $("input[name$='csrfmiddlewaretoken']").val() },

            success : function(json) {
            },

            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }

    //Follow

    $(document).on('click', '#follow-project', function(){
      event.preventDefault();
      var button = $(this);
      $.ajax({
        url : "follow/",
        type : "POST",

        success : function(json) {
          button.html(json);
          if(json == "Follow")
            button.removeClass("btn-following")
          else if(json == "Following")
            button.addClass("btn-following")
        },

        error : function(xhr,errmsg,err) {
          console.log(xhr.status + ": " + xhr.responseText);
        }
      });
    });

    // Vacancies

    $("#add-vacancy").click(function(){
        event.preventDefault();

        var vacancy = '<div class="row form-group vacancy new">';
        vacancy += '<div class="col-xs-2">';
        vacancy += '<div class="input-group">';
        vacancy += '<div class="input-group-addon">0</div>';
        vacancy += '<input type="number" class="form-control number" min="1" value="1" >';
        vacancy += '</div>';
        vacancy += '</div>';
        vacancy += '<div class="col-xs-9">';
        vacancy += '<input type="text" class="form-control name" placeholder="Title" >';
        vacancy += '</div>';
        vacancy += '<div class="col-xs-1 action">';
        vacancy += '<div class="delete-vacancy"><i class="fa fa-times"></i></div>';
        vacancy += '<div class="undo-vacancy hide"><i class="fa fa-undo"></i></div>';
        vacancy += '</div>';
        $("#vacancies").append(vacancy);
    });

    $(document).on('click', '.delete-vacancy', function(){
        event.preventDefault();
        if (!$(this).hasClass('disabled')) {
            if($(this).addClass('hide').parent().parent().hasClass('new')){
                $(this).addClass('hide').parent().parent().remove();
            } else {
                $(this).addClass('hide').parent().parent().addClass('delete').find('.number, .name').attr("disabled", true);
                $(this).parent().find('.undo-vacancy').removeClass('hide');
            }
        }
    });

    $(document).on('click', '.undo-vacancy', function(){
        event.preventDefault();
        $(this).addClass('hide').parent().parent().removeClass('delete').find('.number, .name').attr("disabled", false);;
        $(this).parent().find('.delete-vacancy').removeClass('hide');
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

            var aux = 0;

            $('.vacancy').each(function() {
                if ($(this).hasClass('delete')) {
                    removeVacancy($(this));
                } else if ($(this).hasClass('old')) {
                    updateVacancy($(this));
                } else if ($(this).hasClass('new')) {
                    newVacancy($(this));
                }
                aux++
            });

            if (aux == $('.vacancy').length) {
                window.location = document.URL.replace("vacancies/edit/", "");;
            }
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
        var number = vac.find('.number').val();
        var name = vac.find('.name').val();
        var id = vac.attr('id');

        $.ajax({
            url : "../" + id + "/delete/",
            type : "POST",

            success : function(json) {

            },

            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }

    function updateVacancy(vac) {
        var number = vac.find('.number').val();
        var name = vac.find('.name').val();
        var id = vac.attr('id');

        $.ajax({
            url : "../" + id + "/edit/",
            type : "POST",
            data : { title : name, total: number, csrfmiddlewaretoken:  $("input[name$='csrfmiddlewaretoken']").val() },

            success : function(json) {
            },

            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }

    function newVacancy(vac) {
        var number = vac.find('.number').val();
        var name = vac.find('.name').val();

        $.ajax({
            url : "../new/",
            type : "POST",
            data : { title : name, total: number, csrfmiddlewaretoken:  $("input[name$='csrfmiddlewaretoken']").val() },

            success : function(json) {
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
})(jQuery);
