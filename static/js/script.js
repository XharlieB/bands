$(document).ready(function(){
	$('.container-image-vista').mouseenter(function(){
		$('#container-reproducir').css('display', 'block');
	});
	$('.container-image-vista').mouseleave(function(){
		$('#container-reproducir').css('display', 'none')
	});
});
