const mainMenu = document.querySelector('.mainMenu');
const closeMenu = document.querySelector('.closeMenu');
const openMenu = document.querySelector('.openMenu');




openMenu.addEventListener('click', show);
closeMenu.addEventListener('click', close);

function show() {
    mainMenu.style.display = 'flex';
    mainMenu.style.top = '0';
    document.querySelector('.openMenu').style.display = 'none';
    document.querySelector('.mainbody').style.display = 'none';
}

function close() {
    mainMenu.style.top = '-125%';
    document.querySelector('.openMenu').style.display = 'block';
    document.querySelector('.mainbody').style.display = 'flex';
}

function readyfunc() {
    clearInterval(id);
    var typed = new Typed("#typing1", {
        strings: ["NestedForms"],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });

    var typed = new Typed("#typing2", {
        strings: ["For Create Quizes.", "For Create Survays.", "For Create MCQ Exams.", "Just For Fun.", "By Mohit Satija."],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });

}

id = setInterval(readyfunc, 100);