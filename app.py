import streamlit as st

# --- Estética: Usamos layout="wide" para un mejor despliegue de contenido ---
st.set_page_config(page_title="Sesion 2 | ISIL", layout="wide") 

st.title("Desarrollo de la IA | Línea de Tiempo de Hitos Clave")
st.markdown("---")
st.write("Autor: Jesus Alvarado Huayhuaz | ISIL")
st.write("Interactúa con la barra deslizante para explorar los hitos más importantes en la historia de la Inteligencia Artificial, desde sus bases filosóficas hasta la era de los modelos generativos.")
st.markdown("---")

# --- URLs y Definición de Hitos con Información Ampliada ---

# Se usa la nueva URL de GitHub proporcionada por el usuario
base_url = "https://raw.githubusercontent.com/adrianticonatapia-debug/timeline_s1/main/timeline_images/"

hitos = {
    1: {
        "año": "1950",
        "nombre": "El Test de Turing: La Pregunta de la Máquina Pensante",
        "concepto": "Alan Turing propone un criterio fundamental para evaluar si una máquina puede exhibir un comportamiento conversacional indistinguible del humano.",
        "descripcion": "En su artículo seminal 'Computing Machinery and Intelligence', Turing propuso el 'Juego de Imitación' (Test de Turing). Este no buscaba medir la inteligencia pura, sino la capacidad de una máquina para engañar a un evaluador humano, estableciendo el listón para la Inteligencia Artificial como campo filosófico y de ingeniería. Sentó las bases de la IA simbólica.",
        "figura_clave": "Alan Turing",
        "imagen_url": base_url + "timeline1.png"
    },
    2: {
        "año": "1956",
        "nombre": "El Nacimiento Oficial de la IA: Conferencia de Dartmouth",
        "concepto": "John McCarthy acuña el término *Inteligencia Artificial* en el 'Dartmouth Summer Research Project on Artificial Intelligence'.",
        "descripcion": "Esta conferencia de verano fue el evento fundacional que reunió a los principales visionarios (McCarthy, Minsky, Simon, Newell) para formalizar la investigación. El nombre y la visión definieron el campo, promoviendo la idea de que 'cada aspecto del aprendizaje o cualquier otra característica de la inteligencia puede, en principio, ser descrita con tanta precisión que una máquina puede ser simulada para llevarla a cabo'.",
        "figura_clave": "John McCarthy, Marvin Minsky",
        "imagen_url": base_url + "timeline2.png"
    },
    3: {
        "año": "1997",
        "nombre": "Deep Blue Derrota al Campeón Mundial de Ajedrez",
        "concepto": "Deep Blue de IBM se convierte en la primera máquina en vencer a un campeón mundial de ajedrez, Garry Kasparov, en un formato de torneo.",
        "descripcion": "Esta victoria fue un hito simbólico. No se basó en la intuición, sino en la fuerza bruta de cálculo. Deep Blue podía evaluar 200 millones de posiciones por segundo. Demostró la superioridad de los sistemas de búsqueda complejos y el procesamiento paralelo para resolver problemas bien definidos, marcando la primera gran victoria de la IA sobre el intelecto humano en un juego de estrategia.",
        "figura_clave": "Garry Kasparov, Feng-hsiung Hsu (Diseñador de Deep Blue)",
        "imagen_url": base_url + "timeline3.png"
    },
    4: {
        "año": "2012",
        "nombre": "La Revolución del Deep Learning (AlexNet)",
        "concepto": "AlexNet, una red neuronal profunda, gana ImageNet por un margen significativo, desencadenando el auge del Aprendizaje Profundo.",
        "descripcion": "El equipo de Alex Krizhevsky y Geoffrey Hinton mostró el verdadero potencial de las Redes Neuronales Convolucionales (CNN) combinadas con el poder de procesamiento de las GPUs y grandes conjuntos de datos (ImageNet). Este hito fue crucial, ya que el enorme salto en precisión demostró que las arquitecturas profundas podían resolver tareas de visión por computadora que antes parecían inalcanzables, impulsando la IA moderna.",
        "figura_clave": "Alex Krizhevsky, Geoffrey Hinton",
        "imagen_url": base_url + "timeline4.png"
    },
    5: {
        "año": "2022",
        "nombre": "La Era de la IA Generativa y los Grandes Modelos de Lenguaje (LLMs)",
        "concepto": "Popularización masiva de modelos generativos como ChatGPT y Gemini, llevando capacidades avanzadas de razonamiento y creatividad al público general.",
        "descripcion": "El lanzamiento de los LLMs capaces de mantener conversaciones coherentes, escribir código, resumir textos y generar imágenes (IA de difusión) cambió la interacción pública con la tecnología. Estos modelos, entrenados con miles de millones de parámetros, demuestran capacidades emergentes, abriendo la puerta a los 'Agentes de IA' y transformando industrias completas a un ritmo sin precedentes.",
        "figura_clave": "Diversos equipos de OpenAI, Google, Meta y otros.",
        "imagen_url": base_url + "timeline5.png"
    }
}

# --- Interfaz de Streamlit ---

# Slider para seleccionar el hito
opcion = st.slider(
    "Selecciona un punto del timeline",
    min_value=1,
    max_value=5,
    value=1,
    step=1,
    format="HITO N° %d" # Formato para mejor estética
)

st.markdown("---")

# Obtener los datos del hito seleccionado
data_hito = hitos[opcion]

# Uso de columnas para una mejor estética (Imagen a la izquierda, Texto a la derecha)
col1, col2 = st.columns([1, 2.5])

with col1:
    # Muestra el año de manera destacada
    st.header(data_hito["año"])
    
    # Mostrar la imagen
    st.image(data_hito["imagen_url"], caption=data_hito["nombre"], use_column_width=True)

with col2:
    # Título y Subtítulo
    st.subheader(f":sparkles: {data_hito['nombre']}")
    st.caption(f"**Concepto Central:** {data_hito['concepto']}")

    # Información detallada
    st.markdown("---")
    st.write(data_hito["descripcion"])
    
