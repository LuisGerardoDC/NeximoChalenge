# Challenge Técnico Backend Django/Django Rest Framework

¡Bienvenido al Challenge Técnico Backend Django/Django Rest Framework! Este desafío está
diseñado para evaluar tus habilidades y conocimientos en el desarrollo de aplicaciones
backend utilizando Django y Django Rest Framework. A continuación, se detallan las
instrucciones y requisitos para completar el desafío:

## Requisitos previos:
1. Conocimiento sólido de Python y su sintaxis.
2. Experiencia previa con el framework Django y Django Rest Framework.
3. Familiaridad con el diseño de API RESTful y autenticación.
    - Instrucciones:
        1. Crea un proyecto en Django usando DRF
        2. Crea 3 endpoints:

            - `/api/register`: El endpoint debe recibir los siguientes datos:
                - Nombre completo
                - Correo electrónico
                - Contraseña
            - `/api/login`: El endpoint debe requerir correo electrónico y contraseña y regresar un token
            - `/api/payments`: Este endpoint podrá recibir un arreglo de pagos de los cuales se calcularán los impuestos que ya se pagaron y cumpliendo con las siguientes reglas:

                1. El pago recibido no tiene el IVA desglosado pero ya lo incluye
                2. Si los pagos son en dólares, este incluye además un 3% de comisión.
                3. Los pagos menores de 500 mxn están exentos de IVA.
                            
                    ### Ejemplo 1:
                    ```
                    Python
                    curl -X POST 'http://localhost:8000/api/payments/' \
                        -H 'Accept: application/json, text/plain, */*' \
                        -H 'Authorization: JWT YOUR_TOKEN_HERE' \
                        -d '[ { ... }, { ... } ]' // Data is below
                        
                        [
                            {
                                "amount": 1160,
                                "currency": "MXN"
                            }
                        ]
                        // output
                        {
                            "total": 1000, // en mxn
                            "taxes": 160, // en mxn
                            "commission": 0, // en mxn
                        } 
                    ```
                    ### Ejemplo 2:
                    ```
                    Python
                    curl -X POST 'http://localhost:8000/api/payments/' \
                        -H 'Accept: application/json, text/plain, */*' \
                        -H 'Authorization: JWT YOUR_TOKEN_HERE' \
                        -d '[ { ... }, { ... } ]' // Data is below

                        
                        [
                            {
                                "amount": 1160,
                                "currency": "MXN"
                            },
                            {
                                "amount": 400,
                                "currency": "MXN"
                            }
                        ]
                        // output
                        {
                            "total": 1400,// en mxn
                            "taxes": 160,// en mxn
                            "commission": 0,// en mxn
                        }
                    ```
                    ### Ejemplo 3:
                    ```
                    Python
                    curl -X POST 'http://localhost:8000/api/payments/' \
                        -H 'Accept: application/json, text/plain, */*' \
                        -H 'Authorization: JWT YOUR_TOKEN_HERE' \
                        -d '[ { ... }, { ... } ]' //Data is below

                        // 1 USD = 17 MXN
                        [
                            {
                                "amount": 60
                                "currency": "USD",
                            },
                            {
                                "amount": 20,
                                "currency": "USD"
                            },
                            {
                                "amount": 1160,
                                "currency": "MXN"
                            }
                        ]
                        // output
                        {
                            "total": 2187.28,
                            "taxes": 297.02,
                            "commission": 11.38
                        }
                    ```

        3. Implementa una clase custom de autenticación en Django que utilice JWT (JSON Web
        Tokens) para proteger el endpoint `/api/payments/`. Solo los usuarios autenticados
        deben poder acceder a estos endpoints.
        4. Añade pruebas unitarias para las vistas que creaste. Asegúrate de cubrir diferentes
        casos de prueba, incluyendo casos exitosos y casos de error.
        5. Usar git y enviar un zip usando:

            `git archive --format=zip --output=./backend-challenge.zip HEAD`

### Puntos adicionales (opcional):
Implementa una vista adicional que permita actualizar la contraseña de un usuario
existente al endpoint llamado `/api/password`, debe requerir autenticación.