# taskTool.py

tasks = {}  # Dictionnaire pour stocker les tâches

def ajouter_tache(id_tache, description):
    """
    Ajoute une nouvelle tâche au dictionnaire.

    Args:
    - id_tache (int): Identifiant unique de la tâche.
    - description (str): Description de la tâche.

    Returns:
    - dict: Dictionnaire mis à jour des tâches.
    """
    tasks[id_tache] = {"description": description, "terminee": False}
    return tasks

def supprimer_tache(id_tache):
    """
    Supprime une tâche du dictionnaire.

    Args:
    - id_tache (int): Identifiant de la tâche à supprimer.

    Returns:
    - dict: Dictionnaire mis à jour des tâches.
    """
    if id_tache in tasks:
        del tasks[id_tache]
    return tasks

# Exemple d'utilisation
ajouter_tache(1, "Faire les courses")
ajouter_tache(2, "Répondre aux e-mails")
print(tasks)

supprimer_tache(1)
print(tasks)
