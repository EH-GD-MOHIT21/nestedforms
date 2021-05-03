var main_div = document.getElementById('outer');
var add_more = document.getElementById('content-adderbutton');
var remove_elm = document.getElementById('content-minusbutton');
temp = 0;
indigocolor = 1;
mohit = false;

add_more.onclick = function() {

    document.getElementById("content-minusbutton").style.display = "inline-block";
    // main div
    var div = document.createElement('div');
    div.setAttribute('class', 'question-prototype');

    // qus type
    var new_field = document.createElement('textarea');

    new_field.setAttribute('name', 'question' + indigocolor);
    new_field.setAttribute('class', 'question-box');
    new_field.setAttribute('placeholder', 'Enter Your Question Here');


    // option types

    //option 1

    var div0 = document.createElement('div');
    div0.setAttribute('class', 'main-icoinput');

    // icon1

    var icon1 = document.createElement('i')
    icon1.setAttribute('class', 'far fa-circle')

    var opt1 = document.createElement('input');
    opt1.setAttribute('type', 'text');
    opt1.setAttribute('name', 'option1' + indigocolor);
    opt1.setAttribute('class', 'option-box');
    opt1.setAttribute('placeholder', 'Option A');

    //append icon1 and opt1 to div0
    div0.appendChild(icon1);
    div0.appendChild(opt1);

    // option 2

    var div1 = document.createElement('div');
    div1.setAttribute('class', 'main-icoinput');

    //icon2 

    var icon2 = document.createElement('i')
    icon2.setAttribute('class', 'far fa-circle')

    var opt2 = document.createElement('input');
    opt2.setAttribute('type', 'text');
    opt2.setAttribute('name', 'option2' + indigocolor);
    opt2.setAttribute('class', 'option-box');
    opt2.setAttribute('placeholder', 'Option B');

    //append icon2 and opt2 to div1
    div1.appendChild(icon2);
    div1.appendChild(opt2);

    // option 3

    var div2 = document.createElement('div');
    div2.setAttribute('class', 'main-icoinput');

    // icon 3

    var icon3 = document.createElement('i')
    icon3.setAttribute('class', 'far fa-circle')

    var opt3 = document.createElement('input');
    opt3.setAttribute('type', 'text');
    opt3.setAttribute('name', 'option3' + indigocolor);
    opt3.setAttribute('class', 'option-box');
    opt3.setAttribute('placeholder', 'Option C');

    //append icon3 and opt3 to div2
    div2.appendChild(icon3);
    div2.appendChild(opt3);

    // option 4

    var div3 = document.createElement('div');
    div3.setAttribute('class', 'main-icoinput');

    //icon4

    var icon4 = document.createElement('i')
    icon4.setAttribute('class', 'far fa-circle')

    var opt4 = document.createElement('input');
    opt4.setAttribute('type', 'text');
    opt4.setAttribute('name', 'option4' + indigocolor);
    opt4.setAttribute('class', 'option-box');
    opt4.setAttribute('placeholder', 'Option D');

    //append icon4 and opt4 to div3
    div3.appendChild(icon4);
    div3.appendChild(opt4);

    // final add divs to main div

    div.appendChild(new_field);
    div.appendChild(div0);
    div.appendChild(div1);
    div.appendChild(div2);
    div.appendChild(div3);

    main_div.appendChild(div);
    indigocolor += 1;
    myspecialshitquery();

}

remove_elm.onclick = function() {
    indigocolor -= 1;
    var input_tags = main_div.getElementsByClassName("question-prototype");
    if (input_tags.length > 1) {
        main_div.removeChild(input_tags[(input_tags.length) - 1]);
    }
    if (input_tags.length == 1) {
        document.getElementById("content-minusbutton").style.display = "none";
    }
}

// Auto scailing text-areas


$('#Form-title').on('input', function() {
    this.style.height = 'auto';

    this.style.height =
        (this.scrollHeight) + 'px';
});


$('#Form-Desc').on('input', function() {
    this.style.height = 'auto';

    this.style.height =
        (this.scrollHeight) + 'px';
});


function myspecialshitquery() {
    $('textarea').on('input', function() {
        this.style.height = 'auto';

        this.style.height =
            (this.scrollHeight) + 'px';
    });
}

myspecialshitquery();