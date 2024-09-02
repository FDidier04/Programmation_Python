import sqlite3  # Importe le module sqlite3 pour interagir avec la base de données SQLite
import sys     # Importe le module sys pour gérer les arguments passés en ligne de commande

class Tache:
    def __init__(self, titre, description="", status="À faire"):
        self.titre = titre
        self.description = description
        self.status = status

    def __str__(self):
        return f"Tâche: {self.titre}, Description: {self.description}, Statut: {self.status}"

    @staticmethod
    def init_db():

        print("Initialisation de la base de données...")  # Indique que la base de données est en cours d'initialisation
        conn = sqlite3.connect("taches.db")  # Connexion à la base de données (ou création de celle-ci)
        cursor = conn.cursor()  # Création d'un curseur pour interagir avec la base de données
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS taches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titre TEXT NOT NULL,
                description TEXT,
                status TEXT NOT NULL
            )
        ''')  # Exécute une commande SQL pour créer la table 'taches' si elle n'existe pas
        conn.commit()  # Sauvegarde les modifications dans la base de données
        conn.close()  # Ferme la connexion à la base de données

    @staticmethod
    def ajouter_tache(titre, description=""):
    
        print(f"Ajout de la tâche '{titre}' dans la base de données...")  # Indique que l'ajout d'une tâche est en cours
        conn = sqlite3.connect("taches.db")  # Connexion à la base de données
        cursor = conn.cursor()  # Création d'un curseur pour interagir avec la base de données
        cursor.execute("INSERT INTO taches (titre, description, status) VALUES (?, ?, ?)", 
                       (titre, description, "À faire"))  # Exécute une commande SQL pour insérer une nouvelle tâche
        conn.commit()  # Sauvegarde les modifications dans la base de données
        conn.close()  # Ferme la connexion à la base de données
        print(f"Tâche ajoutée : {titre}")  # Indique que la tâche a été ajoutée avec succès

    @staticmethod
    def mettre_a_jour_tache(tache_id, status):

        conn = sqlite3.connect("taches.db")  # Connexion à la base de données
        cursor = conn.cursor()  # Création d'un curseur pour interagir avec la base de données
        cursor.execute("UPDATE taches SET status = ? WHERE id = ?", 
                       (status, tache_id))  # Exécute une commande SQL pour mettre à jour le statut de la tâche
        conn.commit()  # Sauvegarde les modifications dans la base de données
        conn.close()  # Ferme la connexion à la base de données
        print(f"Tâche {tache_id} mise à jour avec le statut : {status}")  # Indique que la tâche a été mise à jour

    @staticmethod
    def lister_taches():

        conn = sqlite3.connect("taches.db")  # Connexion à la base de données
        cursor = conn.cursor()  # Création d'un curseur pour interagir avec la base de données
        cursor.execute("SELECT id, titre, description, status FROM taches")  # Exécute une commande SQL pour sélectionner toutes les tâches
        taches = cursor.fetchall()  # Récupère toutes les tâches sous forme de liste de tuples
        conn.close()  # Ferme la connexion à la base de données
        
        for tache in taches:
            print(f"ID: {tache[0]}, Titre: {tache[1]}, Statut: {tache[3]}")  # Affiche l'ID, le titre et le statut de chaque tâche
            if tache[2]:  # Si une description est présente
                print(f"   Description: {tache[2]}")  # Affiche la description de la tâche

    @staticmethod
    def afficher_aide():
       
        aide_texte = f"""
        
        print(aide_texte)  # Affiche le texte d'aide

if __name__ == "__main__":
    print("Démarrage du script...")  # Indique que le script a démarré
    Tache.init_db()  # Initialise la base de données

    if len(sys.argv) < 2:
        Tache.afficher_aide()  # Si aucune commande n'est fournie, affiche l'aide
    else:
        commande = sys.argv[1].lower()  # Récupère la commande passée en ligne de commande

        if commande == "add":
            if len(sys.argv) >= 3:
                titre = sys.argv[2]  # Récupère le titre de la tâche
                description = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else ""  # Récupère la description s'il y en a une
                Tache.ajouter_tache(titre, description)  # Ajoute la tâche
            else:
                print("Veuillez fournir un titre pour la tâche.")
                Tache.afficher_aide()  # Affiche l'aide si le titre est manquant

        elif commande == "list":
            Tache.lister_taches()  # Liste toutes les tâches

        elif commande == "update" and len(sys.argv) == 4:
            tache_id = int(sys.argv[2])  # Récupère l'ID de la tâche à mettre à jour
            status = sys.argv[3]  # Récupère le nouveau statut
            if status not in ["À faire", "En cours", "Terminé", "Abandonné"]:
                print(f"Statut invalide : {status}. Utilisez un des statuts suivants : 'À faire', 'En cours', 'Terminé', 'Abandonné'.")
            else:
                Tache.mettre_a_jour_tache(tache_id, status)  # Met à jour le statut de la tâche

        elif commande == "help":
            Tache.afficher_aide()  

        else:
            else:
            print("Commande non reconnue.")
            Tache.afficher_aide()