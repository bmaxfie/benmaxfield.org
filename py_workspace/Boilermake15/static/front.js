$(document).ready(function(){
	
	setTimeout(cutBottom, 1);
	setTimeout(progressBar, 11000);
	setTimeout(toggle1, 20200);
	setTimeout(toggle2, 20600);
	setTimeout(toggle3, 21000);
	setTimeout(toggle4, 21000);
	setTimeout(toggle5, 21200);
	setTimeout(toggle6, 21200);
	setTimeout(toggle7, 21200);
	setTimeout(toggle8, 21200);
	
	function cutBottom(){
		$("#script27").hide();
		$("#script28").hide();
		$("#script29").hide();
		$("#space3").hide();
		$("#script30").hide();
		$("#script31").hide();
		$("#space4").hide();
		$("#script32").hide();
	}
	
	function progressBar(){
		$("#script4").empty().text("  0%|                    |").append("</br>").delay(3000).empty().text("  5%|=                   |").append("</br>");
		/*$("#script4").empty().append(" 10%|==                  |</br>");
		$("#script4").empty().append(" 15%|===                 |</br>");
		$("#script4").empty().append(" 20%|====                |</br>");
		$("#script4").empty().append(" 25%|=====               |</br>");
		$("#script4").empty().append(" 30%|======              |</br>");
		$("#script4").empty().append(" 35%|=======             |</br>");
		$("#script4").empty().append(" 40%|========            |</br>");
		$("#script4").empty().append(" 45%|=========           |</br>");
		$("#script4").empty().append(" 50%|==========          |</br>");
		$("#script4").empty().append(" 55%|===========         |</br>");
		$("#script4").empty().append(" 60%|============        |</br>");
		$("#script4").empty().append(" 65%|=============       |</br>");
		$("#script4").empty().append(" 70%|==============      |</br>");
		$("#script4").empty().append(" 75%|===============     |</br>");
		$("#script4").empty().append(" 80%|================    |</br>");
		$("#script4").empty().append(" 85%|=================   |</br>");
		$("#script4").empty().append(" 90%|==================  |</br>");
		$("#script4").empty().append(" 95%|=================== |</br>");
		$("#script4").empty().append("100%|====================|</br>");*/
	}
	
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