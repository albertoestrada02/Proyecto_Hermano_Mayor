const form = document.getElementById('form');
const firstname = document.getElementById('name');
const lastname = document.getElementById('lastname');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

form.addEventListener('submit',(e)=>{
    e.preventDefault();
    validarEntradas();
});

function validarEntradas()
{
    const firstnameValue = firstname.value.trim();
    const lastnameValue = lastname.value.trim();
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();
    const password2Value = password2.value.trim();

    if(firstnameValue === '')
    {
        setErrorFor(firstname,"El nombre no fue contestado");
    }
    else
    {
        setSuccessFor(firstnameValue);
    }
    if(lastnameValue === '')
    {
        setErrorFor(lastname,"Los apellidos no fue contestados");
    }
    else
    {
        setSuccessFor(lastnameValue);
    }
    if(emailValue === '')
    {
        setErrorFor(email,"El campo email no fue contestado");
    }
    else if(!validarEmail(emailValue))
    {
        setErrorFor(email,"El email no tiene formato valido");
    }
    else
    {
        setSuccessFor(email);
    }
    if(passwordValue ==='')
    {
        setErrorFor(password,"El campo de contraseña no fue contestado");
    }
    else{
        setSuccessFor(password);
    }
    if(password2Value === '')
    {
        setErrorFor(password2,"La confirmacion de la contraseña no fue contestada");
    }
    else if(passwordValue !== password2Value)
    {
        setErrorFor(password2,"No coinciden las contraseñas");
    }
    else
    {
        setSuccessFor(password2);
    }
}
function validarEmail(email)
{
    return /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/.test(email);
}
function setErrorFor(input,mensaje)
{
    const formGroup = input.parentElement;
    const small = formGroup.querySelector('small');
    small.innerText = mensaje;
    formGroup.className = 'form-group incorrecto';

}
function setSuccessFor(input)
{
    const formGroup = input.parentElement;
    formGroup.className = 'form-group correcto';
}

