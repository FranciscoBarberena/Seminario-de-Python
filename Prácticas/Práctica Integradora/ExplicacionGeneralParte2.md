# T.P Integrador - Parte 2

## Consideraciones generales

- La idea es avanzar el Streamlit, usando librerías como Pandas y Matplotlib para implementar las pestañas restantes.
    - **Hay que agregar las librerías usadas al README!!**
- Se continúa usando el mismo repo de GitLab.
- Se usan los datasets generados en processed_datasets.
- Se usa st.session_state para almacenar información entre páginas sin perderla (*ej: el dataset que eligió el usuario*).
- No hace falta pasar todo lo de la parte 1 a su equivalente en Pandas. Sin embargo, está permitido mejorar cosas usando los nuevos contenidos dados.
    - Tener en cuenta que Pandas es una librería pesada
- El orden de las consignas no tiene por qué seguirse al pie de la letra. Si 2 ejercicios están separados pero relacionados, se pueden poner juntos.
- **Fecha de entrega: 5/6 - 23:59hs**
- **Fecha de la defensa: 8/6 en horario de práctica**
## Ejercicio 1

- Introducción a manipulación de datasets usando dataframes de Pandas.
- Se puede leer el csv completo (sin usar chunks) para esta sección.

## Ejercicio 2 (Búsqueda)

- Para hacer filtros aditivos se pueden usar máscaras.
- Para no hardcodear campos, se tendría que buscar los valores únicos de la columna (*ej: todos los valores únicos de la columna 'country'*).
- Preguntar a Emilia campos relevantes para 2C.
- El *"detalle de un registro"* es la ficha del punto 6.

## Ejercicio 3 (Visualización)

- Se pueden hacer los gráficos con Streamlit o con las librerías como Matplotlib. 

## Ejercicio 4 (Gestión de Registros)

- Implementar modificaciones, altas y bajas al Streamlit.
- Si llegase a ser necesario, se puede dividir esto en más páginas (*consultar con Emilia*).
- Según el dataset elegido, el formulario deberá tener distintos campos.
- Hay que expandir la página de logs para permitir filtrado. **No importa si los nombres de las operaciones difieren de las escritas en la conisgna**.

## Ejercicio 5 (Exploración de Datasets)

- Informa sobre todos los datasets a la vez.
- Agregar selector de markdowns de la parte 1 (documentación). **Se puede reutulizar el selector del 5B**

## Ejercicio 6 (Fichas de Datos)

- Usar Folium para el mapa interactivo.
- Las validaciones no deberían ser necesarias si se trabaja con un processed_datset.
- *Duda: Cómo hacer para contar cuántos fueron excluidos por coordenadas inválidas?*
- Para el 6D, ignorar el dataset que no tiene multimedia.
