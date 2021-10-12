/*! Pushy - v0.9.1 - 2013-9-16
* Pushy is a responsive off-canvas navigation menu using CSS transforms & transitions.
* https://github.com/christophery/pushy/
* by Christopher Yee */

$(function() {
	var pushy = $('.menu'), //menu css class
		body = $('body'),
		container = $('#container'), //container css class
		push = $('.push'), //css class to add pushy capability
		siteOverlay = $('.site-overlay'), //site overlay
		pushyClass = "menu-left menu-open", //menu position & menu open class
		pushyActiveClass = "menu-active", //css class to toggle site overlay
		containerClass = "container-push", //container open class
		pushClass = "push-push", //css class to add pushy capability
		menuBtn = $('.menu-btn, .menu a'), //css classes to toggle the menu
		closeMenuBtn = $('.close-menu-btn'),
		menuButton = $('.menu-btn'), //hide menu button when menu active
		menuClass = "menu-hide", //toggle to hide menu button;
		menuSpeed = 200, //jQuery fallback menu speed
		menuPadding = pushy.innerWidth() - pushy.width() ;
		menuWidth = pushy.width() + "px"; //jQuery fallback menu width
		menuTotalWidth = pushy.width() + menuPadding + "px";
	function togglePushy(){
		body.toggleClass(pushyActiveClass); //toggle site overlay
		pushy.toggleClass(pushyClass);
		container.toggleClass(containerClass);
		push.toggleClass(pushClass); //css class to add pushy capability
		menuButton.toggleClass(menuClass); //css class to add pushy capability
	}

	function openPushyFallback(){
		body.addClass(pushyActiveClass);
		pushy.animate({left: "0px"}, menuSpeed);
		container.animate({left: menuTotalWidth}, menuSpeed);
		push.animate({left: menuTotalWidth}, menuSpeed); //css class to add pushy capability
	}

	function closePushyFallback(){
		body.removeClass(pushyActiveClass);
		pushy.animate({left: "-" + menuTotalWidth}, menuSpeed);
		container.animate({left: "0px"}, menuSpeed);
		push.animate({left: "0px"}, menuSpeed); //css class to add pushy capability
	}

	if(Modernizr.csstransforms3d){
		//toggle menu
		menuBtn.click(function() {
			togglePushy();
		});
		//close menu when clicking site overlay
		siteOverlay.click(function(){ 
			togglePushy();
		});
		//close menu button when clicking yellow menu button
		closeMenuBtn.click(function(){ 
			togglePushy();
		});
	}else{
		//jQuery fallback
		pushy.css({left: "-" + menuTotalWidth}); //hide menu by default
		container.css({"overflow-x": "hidden"}); //fixes IE scrollbar issue

		//keep track of menu state (open/close)
		var state = true;

		//toggle menu
		menuBtn.click(function() {
			if (state) {
				openPushyFallback();
				state = false;
			} else {
				closePushyFallback();
				state = true;
			}
		});

		//close menu when clicking site overlay
		siteOverlay.click(function(){ 
			if (state) {
				openPushyFallback();
				state = false;
			} else {
				closePushyFallback();
				state = true;
			}
		});

		//close menu button when clicking yellow menu button
		closeMenuBtn.click(function(){ 
			if (state) {
				openPushyFallback();
				state = false;
			} else {
				closePushyFallback();
				state = true;
			}
		});
	}
});