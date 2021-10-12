(function($, document, window){
	
	$(document).ready(function(){

		// Cloning main navigation for mobile menu
		$(".mobile-navigation").append($(".main-navigation .menu").clone());

		// Mobile menu toggle 
		$(".menu-toggle").click(function(){
			$(".mobile-navigation").slideToggle();
		});

		$("[data-bg-color]").each(function(){
			var color = $(this).data("bg-color");
			$(this).css("background-color",color);
		});

		if( $(".map").length ){
			$('.map').gmap3({
				map: {
					options: {
						maxZoom: 14 
					}  
				},
				marker:{
					address: "40 Sibley St, Detroit",
					options: {
						icon: new google.maps.MarkerImage(
							"images/map-marker.png",
							new google.maps.Size(43, 53, "px", "px")
						)
					}
				}
			},
			"autofit" );
	    }
	    
	});

	$(window).load(function(){

	});

})(jQuery, document, window);