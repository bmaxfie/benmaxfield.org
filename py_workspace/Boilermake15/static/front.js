$(document).ready(function(){
	
	$("#script27").hide();
	$("#script28").hide();
	$("#script29").hide();
	$("#space3").hide();
	$("#script30").hide();
	$("#script31").hide();
	$("#space4").hide();
	$("#script32").hide();
	
	setTimeout(toggle1, 20200);
	setTimeout(toggle2, 20600);
	setTimeout(toggle3, 21000);
	setTimeout(toggle4, 21000);
	setTimeout(toggle5, 21200);
	setTimeout(toggle6, 21200)
	setTimeout(toggle7, 21200);
	setTimeout(toggle8, 21200);
	
	function toggle1(){
		$("#script27").show();
		$("#script1").hide();
	}
	function toggle2(){
		$("#script28").show();
		$("#script2").hide();
	}
	function toggle3(){
		$("#script29").show();
		$("#script3").hide();
	}
	function toggle4(){
		$("#space3").show();
		$("#script4").hide();
	}
	function toggle5(){
		$("#script30").show();
		$("#script5").hide();
	}
	function toggle6(){
		$("#script31").show();
		$("#space1").hide();
	}
	function toggle7(){
		$("#space4").show();
		$("#script6").hide();
	}
	function toggle8(){
		$("#script32").show();
		$("#script7").hide();
	}
});