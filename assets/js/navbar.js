const htm = window.location.href.split('/').slice(-1)[0]
const page = htm.split('.').slice(0)[0]
const item = '.nav-menu ul li'

if (page === 'index') {
  $(`${item}:nth-child(1)`)
    .attr('class', 'active')
    .append('<hr class="nav-underline"/>')
}
if (page === 'resume') {
  $(`${item}:nth-child(2)`)
    .attr('class', 'active')
    .append('<hr class="nav-underline"/>')
}
if (page === 'about') {
  $(`${item}:nth-child(3)`)
    .attr('class', 'active')
    .append('<hr class="nav-underline"/>')
}
if (page === 'contacts') {
  $(`${item}:nth-child(4)`)
    .attr('class', 'active')
    .append('<hr class="nav-underline"/>')
}
