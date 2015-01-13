(function($) {
    "use strict";

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
            console.log($(this));

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
              console.log($(this));
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
        var number = vac.find('.number').val();
        var name = vac.find('.name').val();
        var id = vac.attr('id');

        $.ajax({
            url : "../" + id + "/delete/",
            type : "POST",

            success : function(json) {
                console.log("success"); // another sanity check
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
                console.log("success");
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
})(jQuery);