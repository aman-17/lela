$(document).ready(function() {
	$('input, textarea').placeholder();
     $('.slider-').bxSlider({
        mode:'fade',
        speed:1000,
        touchEnabled: false,
        controls: false,
        auto: true
    });
      jQuery(document).on('click', ".menu_trigger", function (e) {
        e.preventDefault()
        window.setTimeout(function() {
            if(jQuery('#nav').hasClass('clicked')){
                jQuery('#nav').stop(true,true).animate({height:'hide'},100);
                jQuery('#nav').removeClass('clicked');
            }else{
                jQuery('#nav').stop(true,true).animate({height:'show'},400);
                jQuery('#nav').addClass('clicked');
            }
        }, 400);
        return false;
    });
    jQuery("#nav").on('click', '.drops', function () {
        if (jQuery(this).hasClass("active")) {
            jQuery(this).removeClass("active").parent().next().slideUp();
        } else {
            jQuery(this).addClass("active").parent().next().slideDown();
        }
        return false;
    });
	$(".event-calendar td").mouseenter(function(){  
        $(this).find($('.event-calendar td .tooltip')).stop(true, true).fadeIn(600);
        return false;
     });
      $('.event-calendar td').mouseleave(function(){  
        $(this).find($('.event-calendar td .tooltip')).stop(true, true).fadeOut(400);
        return false;
     });

  // Filterable/sortable gallery
  var $container = $('.sortable-grid').imagesLoaded( function() {
    $container.isotope({
      itemSelector: '.grid-item'
    });
  });

  $('.filter-controls a').click(function(e){
    $(this).addClass("selected");
    $(this).parent().siblings().children().removeClass("selected");
      var selector = $(this).attr('data-filter');
      $container.isotope({ filter: selector });
     e.preventDefault();
  });

      
}); 
$(window).resize(function() {
    if($(document).width() > 768){
      $( "#nav" ).addClass("active");
      $( "#nav ul" ).attr('style','');
      $( "#nav" ).attr('style','');
      $( "#nav" ).removeClass("clicked");
      $( "#nav .active" ).removeClass('active');
    }
    else {
        $( "#nav" ).removeClass("active");
    }
});