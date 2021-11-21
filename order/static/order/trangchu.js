// Transition "pho-title-logo" when scroll up or down
var prevScrollpos = window.pageYOffset;

window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        $(".logo-full .logo-h").css("opacity", "1");
        $(".main_links-h").css("opacity", "1");
        
        if (currentScrollPos === 0) {
            document.getElementById("pho_title-h").style.top = "165px";
            document.getElementById("pho_title-h").style.opacity = "1";
        }
    } else {
        document.getElementById("pho_title-h").style.top = "120px";
        document.getElementById("pho_title-h").style.opacity = "0";    
        $(".logo-full .logo-h").css("opacity", "0");
        $(".main_links-h").css("opacity", "0");
    }


    prevScrollpos = currentScrollPos;

    // console.log(`current scroll pos relative to edge window: ${currentScrollPos}`);

    var contentSections = $("section.col_content-h").toArray();

    // console.log(contentSections);

    for (let i = 0; i < contentSections.length; i++) {

        const boundTop = contentSections[i].getBoundingClientRect().top;
        const offsetTop = contentSections[i].offsetTop;

    }
}

// Show header after loaded
var header = document.querySelector("header");
window.onunload = function () {
  header.style.opacity = "0";
}

