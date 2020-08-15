!(($) => {
  'use strict'

  var scrolltoOffset = $('#header').outerHeight() - 1
  $(document).on('click', '.nav-menu a, .mobile-nav a, .scrollto', (e) => {
    if (
      location.pathname.replace(/^\//, '') ==
        this.pathname.replace(/^\//, '') &&
      location.hostname == this.hostname
    ) {
      var target = $(this.hash)
      if (target.length) {
        e.preventDefault()

        var scrollto = target.offset().top - scrolltoOffset

        if ($(this).attr('href') == '#header') {
          scrollto = 0
        }

        $('html, body').animate(
          {
            scrollTop: scrollto,
          },
          1500,
          'easeInOutExpo'
        )

        if ($(this).parents('.nav-menu, .mobile-nav').length) {
          $('.nav-menu .active, .mobile-nav .active').removeClass('active')
          $(this).closest('li').addClass('active')
        }

        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active')
          $('.mobile-nav-toggle i').toggleClass(
            'icofont-navigation-menu icofont-close'
          )
          $('.mobile-nav-overlay').fadeOut()
        }
        return false
      }
    }
  })

  $(document).ready(() => {
    if (window.location.hash) {
      var initial_nav = window.location.hash
      if ($(initial_nav).length) {
        var scrollto = $(initial_nav).offset().top - scrolltoOffset
        $('html, body').animate(
          {
            scrollTop: scrollto,
          },
          1500,
          'easeInOutExpo'
        )
      }
    }
  })

  if ($('.nav-menu').length) {
    var $mobile_nav = $('.nav-menu').clone().prop({
      class: 'mobile-nav d-lg-none',
    })
    $('body').append($mobile_nav)
    $('body').prepend(
      '<button type="button" class="mobile-nav-toggle d-lg-none"><i class="icofont-navigation-menu"></i></button>'
    )
    $('body').append('<div class="mobile-nav-overlay"></div>')

    $(document).on('click', '.mobile-nav-toggle', (e) => {
      $('body').toggleClass('mobile-nav-active')
      $('.mobile-nav-toggle i').toggleClass(
        'icofont-navigation-menu icofont-close'
      )
      $('.mobile-nav-overlay').toggle()
    })

    $(document).on('click', '.mobile-nav .drop-down > a', (e) => {
      e.preventDefault()
      $(this).next().slideToggle(300)
      $(this).parent().toggleClass('active')
    })

    $(document).click((e) => {
      var container = $('.mobile-nav, .mobile-nav-toggle')
      if (!container.is(e.target) && container.has(e.target).length === 0) {
        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active')
          $('.mobile-nav-toggle i').toggleClass(
            'icofont-navigation-menu icofont-close'
          )
          $('.mobile-nav-overlay').fadeOut()
        }
      }
    })
  } else if ($('.mobile-nav, .mobile-nav-toggle').length) {
    $('.mobile-nav, .mobile-nav-toggle').hide()
  }

  var nav_sections = $('section')
  var main_nav = $('.nav-menu, .mobile-nav')

  $(window).on('scroll', () => {
    var cur_pos = $(this).scrollTop() + 200

    nav_sections.each(() => {
      var top = $(this).offset().top,
        bottom = top + $(this).outerHeight()

      if (cur_pos >= top && cur_pos <= bottom) {
        if (cur_pos <= bottom) {
          main_nav.find('li').removeClass('active')
        }
        main_nav
          .find('a[href="#' + $(this).attr('id') + '"]')
          .parent('li')
          .addClass('active')
      }
      if (cur_pos < 300) {
        $('.nav-menu ul:first li:first').addClass('active')
      }
    })
  })

  $(window).scroll(() => {
    if ($(this).scrollTop() > 100) {
      $('#header').addClass('header-scrolled')
    } else {
      $('#header').removeClass('header-scrolled')
    }
  })

  if ($(window).scrollTop() > 100) {
    $('#header').addClass('header-scrolled')
  }

  $(window).on('load', () => {
    AOS.init({
      duration: 1000,
      once: true,
    })
  })
})(jQuery)
