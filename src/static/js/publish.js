document.addEventListener('DOMContentLoaded', (event) => {
    let formData = {
        nombre: '',
        apellido: '',
        email: '',
        gender: '',
        titular: '',
        subtitulo: '',
        tipo: '',
        imagen: '',
        descripcion: ''
    };

    function updateFormData() {
        formData.nombre = document.getElementById('nombre').value;
        formData.apellido = document.getElementById('apellido').value;
        formData.email = document.getElementById('email').value;
        formData.gender = document.querySelector('input[name="gender"]:checked')?.value || '';
        formData.titular = document.getElementById('titular').value;
        formData.subtitulo = document.getElementById('subtitulo').value;
        formData.tipo = document.getElementById('tipo').value;
        formData.imagen = document.getElementById('imagen').value;
        formData.descripcion = document.getElementById('descripcion').value;
    }

    let validationErrors = [];

     // Función para validar los campos del formulario
     function validateForm() {
        const nameRegex = /^[a-zA-Z\s]+$/;
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        // Limpiar estilos de error previos
        document.querySelectorAll('.error').forEach((element) => {
            element.classList.remove('error');
        });

        if (!formData.nombre) {
            validationErrors.push('El nombre no debe estar vacío.');
            document.getElementById('nombre').classList.add('error');
        } else if (!nameRegex.test(formData.nombre)) {
            validationErrors.push('El nombre no debe contener números.');
            document.getElementById('nombre').classList.add('error');
        }

        if (!formData.apellido) {
            validationErrors.push('El apellido no debe estar vacío.');
            document.getElementById('apellido').classList.add('error');
        } else if (!nameRegex.test(formData.apellido)) {
            validationErrors.push('El apellido no debe contener números.');
            document.getElementById('apellido').classList.add('error');
        }

        if (!formData.email) {
            validationErrors.push('El correo electrónico no debe estar vacío.');
            document.getElementById('email').classList.add('error');
        } else if (!emailRegex.test(formData.email)) {
            validationErrors.push('El correo electrónico debe tener el formato correcto.');
            document.getElementById('email').classList.add('error');
        }

        if (!formData.gender) {
            validationErrors.push('Debe seleccionar un género.');
            document.querySelectorAll('input[name="gender"]').forEach((input) => {
                input.classList.add('radio-error');
            });
            document.getElementById('gender-radio').classList.add('radio-container-error');
        }

        if (!formData.titular) {
            validationErrors.push('El titular no debe estar vacío.');
            document.getElementById('titular').classList.add('error');
        }

        if (!formData.subtitulo) {
            validationErrors.push('El subtítulo no debe estar vacío.');
            document.getElementById('subtitulo').classList.add('error');
        }

        if (!formData.descripcion) {
            validationErrors.push('La descripción no debe estar vacía.');
            document.getElementById('descripcion').classList.add('error');
        } else if (formData.descripcion.length <= 200) {
            validationErrors.push('La descripción debe superar los 200 caracteres.');
            document.getElementById('descripcion').classList.add('error');
        }

        if(validationErrors.length > 0) {
            alert('Resuelva los siguientes errores en el formulario: \n' + validationErrors.join('\n'));
            validationErrors = [];
            return false;
        } else {
            return true;
        }
    }

    // Evento para actualizar los valores de los campos cuando cambien
    document.querySelectorAll('input, textarea, select').forEach((input) => {
        input.addEventListener('change', (event) => {
            updateFormData();
            event.target.classList.remove('error');
            if (event.target.name === 'gender') {
                document.getElementById('gender-radio').classList.remove('radio-container-error');
                document.querySelectorAll('input[name="gender"]').forEach((input) => {
                    input.classList.remove('radio-error');
                });
            }
        });
    });

    // Función para limpiar el formulario
    function clearForm() {
        document.getElementById('nombre').value = '';
        document.getElementById('apellido').value = '';
        document.getElementById('email').value = '';
        document.querySelectorAll('input[name="gender"]').forEach((input) => input.checked = false);
        document.getElementById('titular').value = '';
        document.getElementById('subtitulo').value = '';
        document.getElementById('tipo').value = '';
        document.getElementById('imagen').value = '';
        document.getElementById('descripcion').value = '';

        formData = {
            nombre: '',
            apellido: '',
            email: '',
            gender: '',
            titular: '',
            subtitulo: '',
            tipo: '',
            imagen: '',
            descripcion: ''
        };

        // Limpiar estilos de error
        document.querySelectorAll('.error').forEach((element) => {
            element.classList.remove('error');
        });
        document.querySelectorAll('.radio-error').forEach((element) => {
            element.classList.remove('radio-error');
        });
        document.getElementById('gender-radio').classList.remove('radio-container-error');
    }

    // Evento para el botón de limpiar
    document.querySelector('.reset-btn').addEventListener('click', (event) => {
        event.preventDefault();
        clearForm();
    });

    document.querySelector('.submit-btn').addEventListener('click', (event) => {
        event.preventDefault();
        if(validateForm()) {
            alert('Formulario enviado correctamente');
            clearForm();
        }
        updateFormData();
    });
});