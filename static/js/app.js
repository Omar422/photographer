$(function () {
	'use strict';

	var window_hight = $(window).height(),
		upper_navbar = $('.upper-navbar').innerHeight(),
		footer_hight = $('.main-footer').innerHeight(),
		navbar_height = $('.navbar').innerHeight();

	// Main Carousel
	$('.slider, .carousel-item').height(window_hight - navbar_height);
	$('.main-slider .carousel-item:first').addClass('active');
	$('.main-slider .carousel-indicators .rounded-circle:first').addClass('active');

	// login + signup bg # TO DO
	$('.userlogin, .userbg, .userview').height(window_hight);


	// Partner Slider
	$('.owl-carousel').owlCarousel({
		rtl: true,
		loop: true,
		center: true,
		nav: false,
		dots: false,
		autoplay: true,
		autoplayTimeout: 2500,
		autoplayHoverPause: true,
		autoWidth: true,
		responsive: {
			0: {
				// items: 1,
				margin: 50,
			},
			641: {
				// items: 2,
				margin: 80,
			},
			1008: {
				// items: 3,
				margin: 100,
			}
		}
	});

	// portfolio pagination

	// // $('.portfolio .event nav .pagination li:first').addClass('active')
	// $('.portfolio .event nav .pagination li').on('click', function () {
	// 	$(this).addClass('active').siblings().removeClass('active');
	// });

	// portfolio categories filter from list
	$('.portfolio ul.categories li').on('click', function () {
		$(this).addClass('active').siblings().removeClass('active');

		if ($(this).data('class') === 'all') {
			$('.portfolio .event .card').fadeIn(500);
			$('.portfolio .event header span').removeClass('active');
		}
		else {
			$('.portfolio .event header span[data-class="' + $(this).data('class') + '"]').addClass('active').siblings().removeClass('active');
			$('.portfolio .event .card').fadeOut(500);
			$($(this).data('class')).fadeIn(500);
		}
	});

	// portfolio categories filter from tag
	$('.portfolio .event header span').on('click', function () {
		$(this).addClass('active').siblings().removeClass('active');
		$('.portfolio .event .card').fadeOut(300);
		$($(this).data('class')).fadeIn(300);
		$('.portfolio ul.categories li[data-class="' + $(this).data('class') + '"]').addClass('active').siblings().removeClass('active');
	});

	// services categories filter from list
	$('.services ul.categories li').on('click', function () {
		$(this).addClass('active').siblings().removeClass('active');

		if ($(this).data('class') === 'all') {
			$('.services .service').fadeIn(500);
			$('.services .service .card span').removeClass('active');
		}
		else {
			$('.services .service .card span[data-class="' + $(this).data('class') + '"]').addClass('active').siblings().removeClass('active');
			$('.services .service').fadeOut(500);
			$($(this).data('class')).fadeIn(500);
		}
	});


	// services categories filter from tag
	$('.services .service .card span').on('click', function () {
		$('.services .service .card span').addClass('active').siblings().removeClass('active');
		$('.services .service').fadeOut(300);
		$($(this).data('class')).fadeIn(300);
		$('.services ul.categories li[data-class="' + $(this).data('class') + '"]').addClass('active').siblings().removeClass('active');
	});

	// services categories tags on hover

	$('.services article .service .card').hover(function () {
		$(this).find('.category-tag').css('opacity', '1');
	}).mouseleave(function () {
		$(this).find('.category-tag').css('opacity', '0');
	});

	// order status filter 
	$('.orders ul.status li').on('click', function () {
		$(this).addClass('active').siblings().removeClass('active');

		if ($(this).data('class') === 'all') {
			$('.orders table tbody tr').fadeIn(500);
		}
		else {
			$('.orders table tbody tr').fadeOut(500);
			$($(this).data('class')).fadeIn(500);
		}
	});

	///
	$("#id_username").attr('placeholder', '?????? ????????????????');
	$("#id_password").attr('placeholder', '???????? ????????????');
	$('.signupcontent article #id_password1').addClass('pass1').attr("placeholder", "???????? ???????? ????????????");
	$('.signupcontent article #id_password2').addClass('pass2').attr("placeholder", "?????? ?????????? ???????? ????????????");

	// profile

	// change password form

	$('.password-rules p').addClass('row');
	$('.password-rules p label').addClass('col-sm col-md-2');
	$('.password-rules p input').addClass('col-sm col-md-10 form-control');
	$('.password-rules p:first input').attr('placeholder', "???????? ???????????? ??????????????");
	$('.password-rules p:nth-child(2) input').attr('placeholder', "???????? ???????????? ??????????????");
	$('.password-rules p:last input').attr('placeholder', "?????????? ???????? ???????????? ??????????????");

	// reset password form
	$('.reset-form-input input').addClass('form-control').attr('placeholder', "???????? ???????????? ???????????????????? ???????? ???? ???????????????? ???? ?????????? ????????????");

	// reset password done
	$('.reset-confirm-input input').addClass('form-control');
	$('.reset-confirm-input:first input').attr('placeholder', "???????? ???????????? ??????????????");
	$('.reset-confirm-input:last input').attr('placeholder', "?????????? ???????? ???????????? ??????????????");

	// media query
	// $(window).resize(function () {
	// 	if ($(window).innerWidth() > 991) {
	// 		$('.userjoin .userbg .userview .logincontent .accountbg').css('display', 'unset');
	// 	}
	// });

});
