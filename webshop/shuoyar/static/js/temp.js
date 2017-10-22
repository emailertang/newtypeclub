/**
 * 
 * @authors shuoyarNova (you@example.org)
 * @date    2017-10-04 21:41:32
 * @version $Id$
 */

var slideIndex=1;
var time =1;
showSlide(slideIndex);
function currentSlide(n) {
	showSlide(slideIndex = n);
}
function plusSlide (n) {
	showSlide(slideIndex += n);
}
function showSlide (n) {
	var i;
	var slides = document.getElementsByClassName("myslides");
	var dots = document.getElementsByClassName("header_dot");
	 	if (n < 1) {
	 		slideIndex = slides.length;
	 	}
	 	if (n >slides.length) {
	 		slideIndex = 1;
	 	}
		for (i = 0; i < slides.length; i++) {
			if (i == slideIndex-1) {
				slides[i].style.display = "block";
				dots[i].className = "header_dot active";

			}else {
				slides[i].style.display = "none";	
				dots[i].className = "header_dot";
			}
		} 

}
function showSlideByTime() {
	slideIndex++;
	showSlide(slideIndex);
}
setInterval(showSlideByTime,4000);

$(document).click(function(event) {
		if (event.target == $("#login1").get(0)) {
		$("#login1").css('display','none');
	}
});



$(".comment_btn").each(function(i,el) {
	$(el).click(function(event) {
		// console.log($(".mainsc_content_comment").eq(i));
		$(".mainsc_content_comment").eq(i).slideToggle(300);
	});
});

// function test() {
// 	var xmlhttp;
// 	if (window.XMLHttpRequest) {
// 		xmlhttp = new XMLHttpRequest();
// 	}
// 	else {
// 		xmlhttp = new ActiveObject("Microsoft.XMLHTTP");
// 	}
// 	xmlhttp.onreadystatechange = function () {
// 		if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
// 			alert(xmlhttp.responseText);
// 		}
// 	}
// 	xmlhttp.open("get", "/ajax/ajax_add", true);
// 	xmlhttp.send();

// }
$("#test1").click(function(){
	$.get("/ajax/ajax_add",function(a){
		alert(a);
	});
});



