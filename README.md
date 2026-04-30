# 🎓 Asistente Virtual DUOC UC Plaza Oeste  
Arquitectura RAG con Agentes de IA y GitHub Models  

## 📌 Descripción del Proyecto

Este proyecto implementa un asistente virtual inteligente para la sede DUOC UC Plaza Oeste, diseñado para responder consultas estudiantiles utilizando exclusivamente documentación institucional oficial.

El sistema está basado en una arquitectura **Retrieval-Augmented Generation (RAG)** con recuperación semántica mediante embeddings y base vectorial FAISS.

---

## 🎯 Objetivo General

Diseñar e implementar un asistente virtual basado en IA que permita:

- Reducir consultas repetitivas al personal administrativo.
- Entregar respuestas basadas en documentación oficial.
- Disminuir tiempos de respuesta a menos de 5 segundos.

---

## 🧠 Arquitectura Implementada

El sistema utiliza:

- **LLM:** GPT-4o-mini (vía GitHub Models API)
- **Embeddings:** text-embedding-3-small
- **Vector Store:** FAISS
- **Text Splitter:** RecursiveCharacterTextSplitter
- **Framework:** LangChain

### Flujo del Sistema

1. Carga de documentos PDF institucionales.
2. División en fragmentos (chunks).
3. Generación de embeddings (Dense Retrieval).
4. Almacenamiento en base vectorial FAISS.
5. Recuperación de los 3 fragmentos más relevantes.
6. Construcción de contexto.
7. Generación de respuesta con LLM usando prompt controlado.

---

## 📂 Estructura del Proyecto
duoc-rag-assistant/
│
├── EP1_RAG_DUOC.ipynb
├── README.md
├── requirements.txt
├── data/
│ ├── admisiones_2026.pdf
│ ├── becas.pdf
│ ├── calendario_2026.pdf
│ ├── faq.pdf
│ ├── reglamento_academico.pdf


---

## 📄 Documentos Utilizados

- Reglamento Académico
- Calendario Académico
- Reglamento de Becas
- Requisitos de Admisión
- Preguntas Frecuentes Institucionales

---

## 🔒 Control de Seguridad

El sistema:

- No almacena información personal.
- Responde únicamente con información contenida en el contexto recuperado.
- Evita generar información no verificada.
- Utiliza temperatura ≤ 0.3 para reducir alucinaciones.

---

## ⚙️ Instalación y Ejecución

### 1️⃣ Clonar repositorio
git clone <URL_DEL_REPOSITORIO>

### 2️⃣ Instalar dependencias
pip install -r requirements.txt


### 3️⃣ Configurar variables de entorno

Configurar en el notebook o entorno:
OPENAI_API_KEY=TU_TOKEN_GITHUB
OPENAI_BASE_URL=https://models.inference.ai.azure.com


### 4️⃣ Ejecutar notebook

Abrir:
EP1_RAG_DUOC.ipynb


Y ejecutar las celdas en orden.

---

## 🧪 Ejemplo de Uso

Pregunta:
¿Cómo puedo realizar mi matrícula?


Respuesta:

> El proceso de matrícula se realiza a través del portal institucional en línea...

---

## 📊 Tipo de RAG Implementado

Se implementó un RAG de tipo **Dense Retrieval**, utilizando:

- Embeddings numéricos
- Búsqueda por similitud coseno
- Base vectorial FAISS

---

## 🚀 Posibles Mejoras Futuras

- Implementación de múltiples agentes (Académico / Infraestructura)
- Integración con sitio web institucional
- Interfaz web (Streamlit o FastAPI)
- Persistencia automática de índice FAISS

---

## 👨‍💻 Autor

Nombre: Ignacio Andrés Acevedo Espinoza
Carrera: Técnico Analista Programador
Institución: DUOC UC Plaza Oeste
Asignatura: ISY0101

## 🔐 Configuración

Antes de ejecutar el proyecto, crear un archivo `.env` en la raíz del proyecto con:

GITHUB_TOKEN=tu_token_aqui
GITHUB_BASE_URL=https://models.inference.ai.azure.com