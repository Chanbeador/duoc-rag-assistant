# 🎓 Asistente Virtual DUOC UC Plaza Oeste  

## Descripción del Proyecto

El siguiente proyecto implementa un asistente virtual inteligente para DUOC UC Plaza Oeste, diseñado para responder consultas académicas utilizando exclusivamente documentación institucional oficial, actualmente cuenta con memoria para realizar respuestas más elaboradas, al igual que generar correos a petición de los usuarios.

El sistema está basado en una arquitectura **Retrieval-Augmented Generation (RAG)** y base vectorial **FAISS**.

---

## Objetivo General

Diseñar e implementar un asistente virtual basado en IA que permita:

1.	Reducir en al menos un 40% las consultas repetitivas atendidas por personal administrativo.
2.	Entregar respuestas basadas en documentación oficial.
3.	Disminuir tiempos de respuesta a menos de 5 segundos.
4.  Redacción de correos formales respecto a solicitudes de los usuarios.


---

## Arquitectura Implementada

El sistema utiliza:

- **LLM:** GPT-4o-mini (vía GitHub Models API).
- **Embeddings:** text-embedding-3-small.
- **Vector Store:** FAISS.
- **Framework:** LangChain.
- **Agent Engine**

### Flujo del Sistema

1. Carga de documentos PDF institucionales.
2. División en fragmentos o chunks.
3. Generación de embeddings (Dense Retrieval).
4. Almacenamiento en base vectorial FAISS.
5. Recuperación de fragmentos más relevantes.
6. Construcción de contexto.
7. Generación de respuesta con LLM usando prompt controlado.

---

## Documentos Utilizados

- Reglamento Académico
- Calendario Académico
- Información sobre Becas
- Requisitos de Admisión
- Preguntas Frecuentes Institucionales

---

## Control de Seguridad

El sistema:

- No almacena información personal permanente del usuario.
- La memoria conversacional se mantiene mediante el archivo local `memory.json` para conservar contexto durante la interacción.
- Responde únicamente con información contenida en el contexto recuperado.
- Evita generar información no verificada.
- Utiliza temperatura ≤ 0.3 para reducir alucinaciones.

---

## Instalación y Ejecución

### 1 Clonar repositorio
git clone https://github.com/Chanbeador/duoc-rag-assistant.git


cd duoc-rag-assistant

### 2 Crear entorno virtual
```bash
python -m venv .venv
```

### 3 Activar entorno virtual
```powershell
.\.venv\Scripts\Activate.ps1
```

### 4 Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5 Configuración de variables de entorno
El proyecto utiliza variables de entorno para autenticar el acceso a GitHub Models.

Antes de ejecutar la aplicación, se debe crear un archivo llamado `.env` en la raíz del proyecto.

El archivo debe contener:

```env
GITHUB_TOKEN=TU_TOKEN_GITHUB
GITHUB_BASE_URL=https://models.github.ai/inference
```

Por seguridad, el archivo `.env` no debe ser subido al repositorio, ya que contiene credenciales privadas.

El proyecto incluye un archivo `.env.example` como plantilla de configuración, el cual permite conocer la estructura necesaria de las variables de entorno sin exponer información sensible.

Para utilizarlo:

1. Copiar el archivo `.env.example`.
2. Renombrar la copia como `.env`.
3. Reemplazar `TU_TOKEN_GITHUB` por un Personal Access Token válido de GitHub con acceso a GitHub Models.

Ejemplo:

```env
GITHUB_TOKEN=TU_TOKEN_GITHUB
GITHUB_BASE_URL=https://models.github.ai/inference
```

### 6 Ejecutar aplicación
```bash
streamlit run app.py
```

```bash
streamlit run dashboard.py
```

---

## Ejemplo de Uso

1.  El usuario ingresa una consulta.
2.  El agente analiza la intención de la solicitud.
3.  Se selecciona automáticamente la herramienta adecuada:
    *   Consulta RAG
    *   Redacción de correos
    *   Memoria conversacional
4.  Se ejecuta la herramienta seleccionada.
5.  La respuesta se almacena en memoria.
6.  Se entrega el resultado al usuario.

---

## 📊 Tipo de RAG Implementado

Se implementó un RAG de tipo **Dense Retrieval**, utilizando:

- Embeddings numéricos.
- Búsqueda por similitud coseno.
- Base vectorial FAISS.

---

## 👨‍💻 Autor

- Nombre: Ignacio Andrés Acevedo Espinoza

- Carrera: Técnico Analista Programador

- Institución: DUOC UC Plaza Oeste