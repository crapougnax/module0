# Projet d'Analyse de Sentiment

Ce projet se compose de deux parties :

1. Une API FastAPI (`sentiment_api.py`) qui analyse le sentiment d'un texte donné.
2. Une application client Streamlit (`sentiment_streamlit.py`) qui fournit une interface utilisateur pour interagir avec l'API.

## Comment exécuter le projet

Suivez ces étapes pour mettre en place et lancer l'application.

### 1. Prérequis

Assurez-vous d'avoir Python 3.6+ installé sur votre machine.

### 2. Installation

1. Clonez le dépôt (si ce n'est pas déjà fait) et naviguez jusqu'au répertoire du projet.

2. Il est recommandé de créer un environnement virtuel pour isoler les dépendances du projet :

    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
    ```

3. Installez les bibliothèques Python nécessaires :

    ```bash
    pip install fastapi uvicorn pydantic nltk loguru streamlit requests
    ```

4. Le modèle d'analyse de sentiment de NLTK (`vader_lexicon`) doit être téléchargé. Exécutez un interpréteur Python et tapez les commandes suivantes :

    ```python
    import nltk
    nltk.download('vader_lexicon')
    ```

### 3. Exécution de l'API

Ouvrez un terminal et lancez le serveur API FastAPI avec Uvicorn :

```bash
python sentiment_api.py
```

Le serveur sera accessible à l'adresse `http://127.0.0.1:9000`.

### 4. Exécution du client Streamlit

Ouvrez un **second terminal** et lancez l'application client Streamlit :

```bash
streamlit run sentiment_streamlit.py
```

L'application web s'ouvrira automatiquement dans votre navigateur à une adresse comme `http://localhost:8501`.

### 5. Utilisation

1. Assurez-vous que l'API et le client Streamlit sont en cours d'exécution dans leurs terminaux respectifs.
2. Ouvrez l'URL de l'application Streamlit dans votre navigateur.
3. Saisissez un texte dans le champ prévu à cet effet.
4. Cliquez sur le bouton "Analyser" pour voir le résultat de l'analyse de sentiment.
