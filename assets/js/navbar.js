const htm = window.location.href.split('/').slice(-1)[0]
const page = htm.split('.').slice(0)[0]
const navItem = '.nav-menu ul li'

if (page === 'index') {
  $(`${navItem}:nth-child(1)`).attr('class', 'active')
  $(`${navItem}:nth-child(1) .nav-underline`).css('opacity', '1')
}
if (page === 'resume') {
  $(`${navItem}:nth-child(2)`).attr('class', 'active')
  $(`${navItem}:nth-child(2) .nav-underline`).css('opacity', '1')
}
if (page === 'about') {
  $(`${navItem}:nth-child(3)`).attr('class', 'active')
  $(`${navItem}:nth-child(3) .nav-underline`).css('opacity', '1')
}
if (page === 'contacts') {
  $(`${navItem}:nth-child(4)`).attr('class', 'active')
  $(`${navItem}:nth-child(4) .nav-underline`).css('opacity', '1')
}

if (page !== 'index') {
  $(`${navItem}:nth-child(1)`).hover(
    () => {
      $(`${navItem}:nth-child(1) .nav-underline`).css('opacity', '1')
    },
    () => {
      $(`${navItem}:nth-child(1) .nav-underline`).css('opacity', '0')
    }
  )
}
if (page !== 'resume') {
  $(`${navItem}:nth-child(2)`).hover(
    () => {
      $(`${navItem}:nth-child(2) .nav-underline`).css('opacity', '1')
    },
    () => {
      $(`${navItem}:nth-child(2) .nav-underline`).css('opacity', '0')
    }
  )
}
if (page !== 'about') {
  $(`${navItem}:nth-child(3)`).hover(
    () => {
      $(`${navItem}:nth-child(3) .nav-underline`).css('opacity', '1')
    },
    () => {
      $(`${navItem}:nth-child(3) .nav-underline`).css('opacity', '0')
    }
  )
}
if (page !== 'contacts') {
  $(`${navItem}:nth-child(4)`).hover(
    () => {
      $(`${navItem}:nth-child(4) .nav-underline`).css('opacity', '1')
    },
    () => {
      $(`${navItem}:nth-child(4) .nav-underline`).css('opacity', '0')
    }
  )
}