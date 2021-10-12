(function($){ 
    
    "use strict";
    
    $.fn.fullWidth = function(options) {
        var defaults = {
            maxHeight   :    1040,
            minHeight   :    1040,
            delay       :    5000,
            transition  :    1000,
            maxFont     :    36,
            minFont     :    20
        }, settings = $.extend(defaults, options);
        
        var cssTrans  = (function() {
            var elem = document.createElement('p').style,
                prefix = ['Webkit','Moz','O','ms','Khtml'];
        
            if( elem['transition'] == '' ){
                return true;
            }
            while( prefix.length ){
                if( prefix.pop() + 'Transition' in elem ){
                    return true;
                }
            }
            return false;
        }());
        
        return this.each( function() {
        
            var full    =    $(this),
            inner       =    full.find('.inner'),
            slides      =    inner.find('.slide'),
            images      =    slides.find('img'),
            nav         =    full.find('.slide-nav'),
            controls    =    full.find('.controls a'),
            navCircles  =    '',
            smallest    =    9999,
            status      =    {current : 0, previous : 0, max : slides.length - 1},
            timers      =    {slides : '', resize : ''},
            
            move = function(direction, current){
                if(inner.is(':animated')) return;
            
                stop();
            
                status.previous = status.current;
            
                if(direction === 'right'){
                    status.current = status.current+1 > status.max ? 0 : status.current+1;
                }else if(direction === 'left'){
                    status.current = status.current-1 < 0 ? status.max : status.current-1;
                }else{
                    status.current = current || 0;
                }
            
                navCircles.removeClass('current').eq(status.current).addClass('current');
                full.trigger( 'fws.start', { 'status' : status, 'direction' : direction } );
                
                if(cssTrans){
                    inner.css({ 'margin-left' : '-' + 100 * status.current + '%' });
                    setTimeout(function(){ start(); }, settings.transition);
                }else{
                    inner.animate({ 'margin-left' : '-' + 100 * status.current + '%' }, settings.transition, function(){ start(); });
                }
            
            },
            start = function(){
                full.trigger( 'fws.finish', { 'status' : status } );
                timers.slides = setTimeout(function(){ move('right'); }, settings.delay);
            },
            stop = function(){
                clearTimeout(timers.slides);
            },
            resize = function(){
                
                var wWidth    =    $(window).width(),
                newHeight     =    parseInt(wWidth/3, 10),
                imageCSS      =    wWidth <= smallest ? ['100%', 'auto', '9999'] : ['', '', ''],
                start         =    inner.height(),
                divCSS        =    wWidth <= 480 ? ['0', '100%', 'none'] : ['', '', ''],
                size          =    wWidth/41;
                

                size = size > settings.maxFont ? settings.maxFont : 
                            (size < settings.minFont ? settings.minFont : size);

                
                /* Total Padding for Slide Desc */
                var paddT = $('.slide-desc').innerWidth() - $('.slide-desc').width();
                var paddH = $('.slide-desc').innerHeight() - $('.slide-desc').height();

                /* Reload/Resize everything based on window width (Slider Image, Slider Inner Height, Slider Desc Position, Slider Control position, Maps width, and change placeholder for newsletter form in footer) */
                if(wWidth > 1500){
                    /* If window width more than 1500, slider image doesn't use max-height, if it lower than 1500, slider image using max height to keep image in center */
                    images.css({
                    'min-height' : settings.minHeight, 'width' : imageCSS[1], 'maxWidth' : imageCSS[2], 'max-height': 'none'
                    });
                    /* Resize inner height for slider based on window width, so it will fit for mobile browser */
                    inner.css('height',settings.minHeight);
                    /* Reposition slide desc */
                    slides.find('.slide-desc').css({
                    'top' : function(){
                       var diff = settings.minHeight - ($(this).height() + paddH + 4);
                       return diff/2;
                   }});
                    /* reposition controller slider 45 is margin between slide desc box and control button, 101 = 45 + 56 with 56 is width of control button */
                    $('.controls a.left').css({
                        'margin-left':function(){
                            var marginLeft = (($('.slide-desc').width() + paddT + 4)/2) + 101;
                            return marginLeft-(marginLeft*2);
                        }
                    });
                    $('.controls a.right').css({
                        'margin-left':function(){
                            var marginRight = (($('.slide-desc').width() + paddT + 4)/2) + 45;
                            return marginRight;
                        }
                    });
                    /* Placeholder for newsletter subcription in footer will change to "Email Adress..." only if window width less than 480px */
                    $('#subscribe-newsletter .footer-input-text[placeholder]').val("Enter your email to join newsletter...");
                    /* Resize full width header height */
                    $('#full-width-header .inner').css("height",settings.minHeight);
                    /* Map in contact page are based on window width */
                    $('#map-canvas').css({
                        'width' : wWidth,
                        'height' : settings.minHeight
                    })
                }else if(wWidth > 1000){
                    images.css({
                        'min-height':settings.minHeight ,'max-height' : settings.minHeight, 'width' : imageCSS[1], 'maxWidth' : imageCSS[2]
                    });
                    inner.css('height',settings.minHeight);
                    slides.find('.slide-desc').css({
                    'top' : function(){
                       var diff = settings.minHeight - ($(this).height() + paddH + 4);
                       return diff/2;
                   }})
                    $('.controls a.left').css({
                        'margin-left':function(){
                            var marginLeft = (($('.slide-desc').width() + paddT + 4)/2) + 101;
                            return marginLeft-(marginLeft*2);
                        }
                    });
                    $('.controls a.right').css({
                        'margin-left':function(){
                            var marginRight = (($('.slide-desc').width() + paddT + 4)/2) + 45;
                            return marginRight;
                        }
                    });
                    $('#subscribe-newsletter .footer-input-text[placeholder]').val("Enter your email to join newsletter...");
                    /* Resize full width header height */
                    $('#full-width-header .inner').css("height",settings.minHeight);
                    /* Map in contact page are based on window width */
                    $('#map-canvas').css({
                        'width' : wWidth,
                        'height' : settings.minHeight
                    })
                }else if(wWidth > 649){
                    images.css({
                        'min-height':800 ,'max-height' : 800, 'width' : imageCSS[1], 'maxWidth' : imageCSS[2]
                    });
                    inner.css('height',800);
                    slides.find('.slide-desc').css({
                    'top' : function(){
                       var diff = 800 - ($(this).height() + paddH + 4);
                       return diff/2;
                   }})
                    $('.controls a.left').css({
                        'margin-left':function(){
                            var marginLeft = (($('.slide-desc').width() + paddT + 4)/2) + 81;
                            return marginLeft-(marginLeft*2);
                        }
                    });
                    $('.controls a.right').css({
                        'margin-left':function(){
                            var marginRight = (($('.slide-desc').width() + paddT + 4)/2) + 25;
                            return marginRight;
                        }
                    });
                    $('#subscribe-newsletter .footer-input-text[placeholder]').val("Enter your email to join newsletter...");
                    /* Resize full width header height */
                    $('#full-width-header .inner').css("height",settings.minHeight);
                    /* Map in contact page are based on window width */
                    $('#map-canvas').css({
                        'width' : wWidth,
                        'height' : settings.minHeight
                    })
                }else if(wWidth > 479){
                    images.css({
                        'min-height':500 ,'max-height' : 600, 'width' : imageCSS[1], 'maxWidth' : imageCSS[2]
                    });
                    inner.css('height',500);
                    slides.find('.slide-desc').css({
                    'top' : function(){
                       var diff = 500 - ($(this).height() + paddH + 4);
                       return diff/2;
                   }})
                    $('.controls a.left').css({
                        'margin-left':function(){
                            var marginLeft = (($('.slide-desc').width() + paddT + 4)/2) + 71;
                            return marginLeft-(marginLeft*2);
                        }
                    });
                    $('.controls a.right').css({
                        'margin-left':function(){
                            var marginRight = (($('.slide-desc').width() + paddT + 4)/2) + 15;
                            return marginRight;
                        }
                    });
                    $('#subscribe-newsletter .footer-input-text[placeholder]').val("Enter your email to join newsletter...");
                    /* Resize full width header height */
                    $('#full-width-header .inner').css("height","500px");
                    /* Map in contact page are based on window width */
                    $('#map-canvas').css({
                        'width' : wWidth,
                        'height' : 500
                    })
                }else{
                     images.css({
                        'min-height':400 ,'max-height' : 400, 'width' : imageCSS[1], 'maxWidth' : imageCSS[2]
                    });
                    inner.css('height',400);
                    slides.find('.slide-desc').css({
                    'top' : function(){
                       var diff = 400 - ($(this).height() + paddH + 4);
                       return diff/2;
                   }})
                    $('.controls a.left').css({
                        'margin-left':function(){
                            var marginLeft = (($('.slide-desc').width() + paddT + 4)/2) + 61;
                            return marginLeft-(marginLeft*2);
                        }
                    });
                    $('.controls a.right').css({
                        'margin-left':function(){
                            var marginRight = (($('.slide-desc').width() + paddT + 4)/2) + 5;
                            return marginRight;
                        }
                    });
                    $('#subscribe-newsletter .footer-input-text[placeholder]').val("Email address...");
                    /* Resize full width header height */
                    $('#full-width-header .inner').css("height","400px");
                    /* Map in contact page are based on window width */
                    $('#map-canvas').css({
                        'width' : wWidth,
                        'height' : 400
                    })
                }
                /* Triangle / Diagonal line in everyhomepage also based on window width */
                $('.triangle.top').css({
                    'border-right-width' : wWidth
                })
                $('.triangle.top.promotion , .triangle.top.footer').css({
                    'border-left-width' : wWidth
                })
                $('.triangle.bottom').css({
                    'border-left-width' : wWidth
                })
                $('.triangle.bottom.promotion').css({
                    'border-right-width' : wWidth,
                    'border-left-width' : 0
                })
            },
            attachEvents = function(){
            
                $(window).resize(function(){
                    clearTimeout(timers.resize);
                    timers.resize = setTimeout(function(){ resize(); }, 100);
                }).trigger('resize');
                
                controls.on('click', function(){
                    move(this.className);
                    return false;
                });
                
                navCircles.on('click', function(){
                    move('direct', $(this).index());
                });
                
                $(document).on('keydown', function(e){
                    if(!(e.which === 37 || e.which === 39)) return; 
                    move(e.which === 37 ? 'left' : 'right');
                });
    
            };
        
            (function(){
                
                images.each(function(){
                    var w = $(this).attr('width');
                    smallest = w < smallest ? w : smallest;
                });
                
                slides.css('width', parseFloat(100/slides.length, 10)+'%')
                      .each(function(i){
                          $(this).addClass('slide-'+(i+1));
                          nav.append('<span></span>');
                      });
                
                /* inner.css({
                    height: settings.minHeight,
                    transition: settings.transition+'ms',
                    width: (slides.length*100)+'%'
                }); */
                var wWidth = $(window).width();
                if(wWidth > 1500){
                    inner.css({
                        height: settings.minHeight,
                        transition: settings.transition+'ms',
                        width: (slides.length*100)+'%'
                    });
                    $('#full-width-header .inner').css("height",settings.minHeight);
                    /* Map in contact page are based on window width */
                    $('#map-canvas').css({
                        'width' : wWidth,
                        'height' : settings.minHeight
                    })
                    $('#subscribe-newsletter .footer-input-text[placeholder]').val("Enter your email to join newsletter...");
                }else if(wWidth > 1000){
                    inner.css({
                        height: settings.minHeight,
                        transition: settings.transition+'ms',
                        width: (slides.length*100)+'%'
                    });
                    $('#full-width-header .inner').css("height",settings.minHeight);
                    /* Map in contact page are based on window width */
                    $('#map-canvas').css({
                        'width' : wWidth,
                        'height' : settings.minHeight
                    })
                    $('#subscribe-newsletter .footer-input-text[placeholder]').val("Enter your email to join newsletter...");
                }else if(wWidth > 649){
                    inner.css({
                        height: 800,
                        transition: settings.transition+'ms',
                        width: (slides.length*100)+'%'
                    });
                    $('#full-width-header .inner').css("height",settings.minHeight);
                    /* Map in contact page are based on window width */
                    $('#map-canvas').css({
                        'width' : wWidth,
                        'height' : settings.minHeight
                    })
                    $('#subscribe-newsletter .footer-input-text[placeholder]').val("Enter your email to join newsletter...");
                }else if(wWidth > 479){
                    inner.css({
                        height: 500,
                        transition: settings.transition+'ms',
                        width: (slides.length*100)+'%'
                    });
                    $('#full-width-header .inner').css("height","500px");
                    /* Map in contact page are based on window width */
                    $('#map-canvas').css({
                        'width' : wWidth,
                        'height' : 500
                    })
                    $('#subscribe-newsletter .footer-input-text[placeholder]').val("Enter your email to join newsletter...");
                }else{
                    inner.css({
                        height: 400,
                        transition: settings.transition+'ms',
                        width: (slides.length*100)+'%'
                    });
                    $('#full-width-header .inner').css("height","400px");
                    /* Map in contact page are based on window width */
                    $('#map-canvas').css({
                        'width' : wWidth,
                        'height' : 400
                    })
                    $('#subscribe-newsletter .footer-input-text[placeholder]').val("Email address...");
                }
                navCircles = nav.find('span');
                navCircles.first().addClass('current');
                nav.css('width', function(){
                    return navCircles.length*30;
                });

                nav.css('margin-left',function(){
                    return ((navCircles.length*30/2)-(navCircles.length*30));
                })
                $('.triangle.top').css({
                    'border-right-width' : wWidth
                })
                $('.triangle.top.promotion , .triangle.top.footer').css({
                    'border-left-width' : wWidth
                })
                $('.triangle.bottom').css({
                    'border-left-width' : wWidth
                })
                $('.triangle.bottom.promotion').css({
                    'border-right-width' : wWidth,
                    'border-left-width' : 0
                })
                $('#subscribe-newsletter .footer-input-text[placeholder]').val("Enter your email to join newsletter...");
                $(window).load(function() {
                    attachEvents();
                    full.trigger( 'fws.start', { 'status' : status, 'direction' : 'direct' } );
                    inner.fadeTo(1000, 1, function(){
                        start();
                    });
                });
            }());
        
        });
    };
     
}(jQuery));
