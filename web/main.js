

function setImage(base64) {
	document.getElementById("qr").src = base64
}

function myFunction() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");
  
  
}

function getPathToFile() {
	
var path=eel.pythonFunction()(r => console.log(r));
 


var agenda = document.getElementById("agenda").value;
var num_usr = document.getElementById("num_usr").value;
eel.getAgenda(agenda)
eel.getNum_usr(num_usr)



};

function gotoNext(){
	eel.begin_voice()
	eel.operation()
	if(eel.done()){
		window.location.assign("final.html");
			eel.thank_voice()
	}

}
function voiceprompt(){
	eel.voice()
}




