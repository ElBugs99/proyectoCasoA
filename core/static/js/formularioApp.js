// document.getElementById();
/* <script src="https://code.jquery.com/jquery-3.6.0.min.js"
integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" 
crossorigin="anonymous"></script> */
//window.location

//window.location.href = 'www.google.com'

const form = document.getElementById('form');
const nombreC = document.getElementById('nombre');
const usuario = document.getElementById('usuario');
const email = document.getElementById('email');
const numero = document.getElementById('numero');
const password = document.getElementById('password');
const password2 = document.getElementById('confirm-password');

//eventos

form.addEventListener('submit', event => {
    
    event.preventDefault();

    validarFormulario();

    if (document.querySelectorAll('.success').length == 6){
        alert('Se ha registrado');
        document.location.href = 'Aporte.html'
        //window.location.reload();
    } else if (document.querySelectorAll('.error').length == 6){

        //window.location.reload();Proyecto_Semestre/Aporte.html
    }

});

usuario.addEventListener('blur', () => validarUsuario());

nombreC.addEventListener('blur', () => validarNombre());

email.addEventListener('blur', () => validarEmail());

numero.addEventListener('blur', () => validarNumero());

password.addEventListener('blur', () => validarPassword());

password2.addEventListener('blur', () => validarConfirmarPassword());

//Validaciones
const validarFormulario = () => {

    validarUsuario();
    validarNombre();
    validarEmail();
    validarNumero();
    validarPassword();
    validarConfirmarPassword();

}

const validarUsuario = () => {

    const valorUsuario = usuario.value.trim();

    if (valorUsuario === ''){
        //mostrar error
        //añadir clase error
        fijarErrorPara(usuario, '¿Olvidaste algo? ¡Usuario vacio!');

    } else if (valorUsuario.length < 3) {

        fijarErrorPara(usuario, 'Debe tener al menos 3 caracteres');

    } else {
        //añadir clase success
        fijarExitoPara(usuario);

    }
}

const validarNombre = () => {

    const valorNombreC = nombreC.value.trim();
    
    if (valorNombreC ==='') {

        fijarErrorPara(nombreC, '¿Olvidaste algo? ¡Nombre vacio!');
        return;

    } else {

        fijarExitoPara(nombreC)

    }
}

const validarEmail = () => {

    const valorEmail = email.value.trim();

    if (valorEmail === ''){

        fijarErrorPara(email, '¿Olvidaste algo? ¡Email vacio!');

    }else if (!validateEmail(valorEmail)){

        fijarErrorPara(email, 'Email no valido')

    } else {
        
        fijarExitoPara(email);
    }

}

const validarNumero = () => {

    const valorNumero = numero.value;

    if (valorNumero === ''){

        fijarErrorPara(numero, '¿Olvidaste algo? ¡Número vacio!')

    } else if (valorNumero.toString().length < 9){

        fijarErrorPara(numero, 'Número debe tener 9 digitos')
        console.log(valorNumero.toString().length)
    }else{
        fijarExitoPara(numero)
    }

}

const validarPassword = () => {

    const valorPassword = password.value.trim();

    if (valorPassword === ''){

        fijarErrorPara(password, '¿Olvidaste algo? ¡contraseña vacia!')

    } else {

        fijarExitoPara(password)
    }

}

const validarConfirmarPassword = () => {

    const valorPassword = password.value.trim();
    const valorPassword2 = password2.value.trim();

    if (password2 === ''){

        fijarErrorPara(password2, '¿Olvidaste algo? ¡contraseña vacia!')

    } else if (valorPassword != valorPassword2) {

        fijarErrorPara(password2, 'Las contraseñas no coinciden')

    }else if (valorPassword ==='' && valorPassword2 === ''){

        fijarErrorPara(password2, '¿Olvidaste algo? ¡contraseña vacia!')

    } else {

        fijarExitoPara(password2)

    }

}

const validateEmail = (email) => {
    
    return /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email);
       
  };

const fijarErrorPara = (input, mensaje) => {
    const formControl = input.parentElement; //seleccionar clase padre del input  ????
    const pError = formControl.querySelector('p');

    //añadir mensaje dentro de p
    pError.innerText = mensaje;// ¿?   

    //añadir clase error
    console.log(formControl)
    console.log(formControl.className)
    formControl.className = 'element error register-group-element';//¿?
    console.log(formControl.className)
}

const fijarExitoPara = (input) => {
    const formControl = input.parentElement;
    const pSuccess = formControl.querySelector('p');

    console.log(formControl)
    console.log(formControl.className)
    formControl.className = 'element success register-group-element';
    console.log(formControl.className)

    pSuccess.innerText = '';
}

//agregar autocompletar
//alert no funciona
//validar checkbox
//desbloquear submit
//arreglar politica de privacidad
//Hacer burbujas clickeables


//usar jquery para alguna estupidez
//display inline block 9:30
//no soy un robot Api
//===

//nombre no puede tener numeros


// const mostrarConfirmacion = elemento => {
//     const inputControl = elemento.parentElement;
//     const errorDisplay = inputControl.querySelector('.error');

//     errorDisplay.innerText = mensaje;
//     inputControl.classList.add('success');
//     inputControl.classList.remove('error');
// }

// const mostrarError = (elemento, mensaje) => {
//     const inputControl = elemento.parentElement;
//     const errorDisplay = inputControl.querySelector('.error');

//     errorDisplay.innerText = mensaje;
//     inputControl.classList.add('error');
//     inputControl.classList.remove('success');
// }




// const nameOnclick = event => {
//     console.log(event.value);
//     const regex = /([^a-zA-Z])\w+/;
//     const newValue = event.value.replace(regex, '');
//     return event.value = event.value.replace(regex, '');
//     //document.querySelector()
// }

// const validarPassword = () => {
//     if (password.value.length <= 6) {
//         document.getElementById('pass-error-msg');
//     }
// }