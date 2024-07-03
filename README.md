# Tercera-pre-entrega-Debenedetto
Lost and Found

Lost and Found es una aplicación web diseñada para administrar los objetos perdidos y encontrados de un hotel. El objetivo principal es facilitar la devolución de objetos perdidos a sus propietarios de manera eficiente y mejorar la experiencia del cliente.
Funcionalidades

    Registro de Objetos Encontrados: Permite al personal del hotel registrar objetos encontrados mediante un formulario en la página principal seleccionando la opción "I found an item". (Tengo pensado generar un log in para el staff)

    Registro de Objetos Perdidos: Permite a los huéspedes reportar objetos perdidos a través del formulario seleccionando la opción "I lost an item". Estos objetos se almacenan en la base de datos para su búsqueda y posible devolución. (Deberia trabajar en registrar quien es el husped y forma de contacto para poder devolver el item en el caso de encontrarlo.)

    Panel de Administración: Accesible para el personal del hotel (Front desk, Hsk) mediante autenticación. Permite:
        Filtrar objetos perdidos según las características reportadas por los huéspedes.
        Marcar un objeto como devuelto una vez que se ha encontrado y entregado al propietario.

        User: Admin
        Clave: 12345
        
  Tecnologías Utilizadas

    Django
    Python
    HTML
    CSS
    JavaScript

Uso

Una vez instalado el proyecto:

    Huéspedes:
        Desde la página principal, selecciona "I found an item" para reportar un objeto encontrado o "I lost an item" para reportar un objeto perdido.

    Personal del Hotel:
        Desde la página principal, selecciona "I found an item" para reportar un objeto encontrado.
        Accede al panel de administración (/admin) e inicia sesión con tus credenciales.
        Utiliza los filtros para buscar objetos perdidos reportados por los huéspedes.
        Marca los objetos encontrados como devueltos una vez entregados a sus propietarios.

Autor

    Autor: Cinthia Debenedetto
    Contacto: [Tu Correo Electrónico]
