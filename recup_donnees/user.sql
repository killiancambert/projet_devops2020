-- Création des utilisateurs avec leurs droits

CREATE USER 'root'@'127.0.0.1' IDENTIFIED BY 'rootdevops';
GRANT ALL PRIVILEGES ON *.* TO 'administrateur_delegue'@'127.0.0.1';

CREATE USER 'administrateur_delegue'@'127.0.0.1' IDENTIFIED BY 'administrateur_delegue';
GRANT ALL PRIVILEGES ON devops.* TO 'administrateur_delegue'@'127.0.0.1';

CREATE USER 'concentrateur_docker'@'127.0.0.1' IDENTIFIED BY 'concentrateur_docker';
GRANT INSERT, SELECT, UPDATE devops.* TO 'concentrateur_docker'@'127.0.0.1';

CREATE USER 'datavision'@'127.0.0.1' IDENTIFIED BY 'datavision';
GRANT SELECT ON devops.* TO 'datavision'@'127.0.0.1';
