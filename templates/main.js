function send_name(){
            code = document.getElementById('code_field').value
            name = document.getElementById('name_field').value
            eel.get_code(code, name)
         };
eel.expose(display_msg)
function display_msg(nameofsender, msg){
    console.log(msg)
    var msgbox = document.createElement('P')
    msgbox.innerHTML = nameofsender + ': ' + msg
    document.getElementById('chatbox').appendChild(msgbox)
    var elem = document.getElementById('chatbox');
    elem.scrollTop = elem.scrollHeight;
}
function send_msg(){
    eel.send_msg(document.getElementById('usermsg').value)
}
eel.expose(error_msg)
function error_msg(msg){
    var error = document.createElement('P')
    error.innerHTML = msg
    document.body.appendChild(error)
}
function quit_room(){
    eel.quit_room()
}
