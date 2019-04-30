$(document).ready(() => {
    const $projects = $('#projects');
    const $dropdownmenu = $('.dropdown-menu')

    $projects.on('mouseover', () => {
        $dropdownmenu.show();
    })
    $dropdownmenu.on('mouseleave', () => {
        $dropdownmenu.hide();
    })
})