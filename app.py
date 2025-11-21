import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Hitos de Detección de Fraude",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Definición de los Eventos ---

# Los datos de los 5 eventos, incluyendo título, descripción y la ruta de la imagen.
# NOTA: Se han actualizado las rutas de las imágenes a "timeline1.png" a "timeline5.png"
# La ruta de la imagen es relativa a la ubicación del archivo app.py en GitHub.
eventos = {
    1: {
        "titulo": "1. Sistemas de Puntuación de Fraude (FICO y Similares)",
        "descripcion": "Sentó las bases metodológicas al introducir modelos estadísticos para asignar una puntuación de riesgo a transacciones e individuos, un precursor fundamental para la detección predictiva.",
        "imagen_path": "timeline_images/timeline1.png"
    },
    2: {
        "titulo": "2. Autenticación de Doble Factor (2FA)",
        "descripcion": "Cambió el foco hacia la prevención activa de la toma de cuentas (ATO) al requerir dos o más factores de verificación. Dificultó el acceso a los defraudadores incluso con la contraseña robada.",
        "imagen_path": "timeline_images/timeline2.png"
    },
    3: {
        "titulo": "3. Adopción del Chip EMV (Chip y PIN)",
        "descripcion": "La migración del riesgo. Eliminó el fraude físico por clonación en el punto de venta al usar chips criptográficos. Esto obligó a la industria a mejorar rápidamente las defensas en el comercio electrónico.",
        "imagen_path": "timeline_images/timeline3.png"
    },
    4: {
        "titulo": "4. Uso de Machine Learning (ML) e Inteligencia Artificial (IA)",
        "descripcion": "Permitió la detección de fraude en tiempo real con alta precisión. Los algoritmos de IA y ML pueden analizar patrones sutiles en vastos volúmenes de datos, adaptándose rápidamente a nuevas tácticas.",
        "imagen_path": "timeline_images/timeline4.png"
    },
    5: {
        "titulo": "5. Detección de Huellas Digitales de Dispositivos (Device Fingerprinting)",
        "descripcion": "Crea un identificador único para cada dispositivo (PC, móvil) basado en más de un centenar de parámetros. Es esencial para identificar dispositivos de riesgo y combatir el fraude de transacciones no presentes (CNP).",
        "imagen_path": "timeline_images/timeline5.png"
    }
}

# --- Interfaz de Streamlit ---

st.title("Hitos Trascendentales en la Detección de Transacciones Fraudulentas")
st.markdown("---")

# Slider para seleccionar el evento
# El slider va del 1 al 5.
evento_seleccionado_key = st.slider(
    "Selecciona un Hito en la Línea de Tiempo:",
    min_value=1,
    max_value=5,
    step=1,
    format="Hito N° %d",
    help="Utiliza este control para navegar por los 5 hitos principales."
)

# Obtener los datos del evento seleccionado
data_evento = eventos[evento_seleccionado_key]

st.markdown("---")

# Mostrar el contenido del evento seleccionado
col1, col2 = st.columns([1, 2])

with col1:
    # Cargar y mostrar la imagen.
    # El archivo debe estar en la carpeta 'timeline_images' en el repositorio.
    st.image(
        data_evento["imagen_path"],
        caption=data_evento["titulo"],
        use_column_width=True
    )

with col2:
    st.header(data_evento["titulo"])
    st.info(data_evento["descripcion"])
    
st.markdown("---")
st.caption("Asegúrate de que las imágenes 'timeline1.png' a 'timeline5.png' estén en la carpeta 'timeline_images' de tu repositorio para que se visualicen correctamente en Streamlit Cloud.")
