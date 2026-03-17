<?php
/**
 * Log des visites d'articles
 *
 * - Accepte uniquement les requêtes POST
 * - Valide le format du slug
 * - Écrit dans un fichier CSV protégé par .htaccess
 * - Aucun endpoint de lecture : les données ne sont accessibles que par FTP
 */

// Bloquer toute méthode autre que POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    exit;
}

// Lire le body JSON
$input = json_decode(file_get_contents('php://input'), true);

if (!$input || empty($input['slug'])) {
    http_response_code(400);
    exit;
}

$slug = $input['slug'];

// Valider le slug : uniquement lettres minuscules, chiffres et tirets
if (!preg_match('/^[a-z0-9-]+$/', $slug) || strlen($slug) > 200) {
    http_response_code(400);
    exit;
}

// Chemin du fichier de logs (protégé par .htaccess)
$logDir = __DIR__ . '/../logs';
$logFile = $logDir . '/visits.csv';

// Créer le dossier logs s'il n'existe pas
if (!is_dir($logDir)) {
    mkdir($logDir, 0750, true);
}

// Écrire l'en-tête CSV si le fichier n'existe pas encore
if (!file_exists($logFile)) {
    file_put_contents($logFile, "date,slug,ip_hash,user_agent_hash\n");
}

// Hasher l'IP et le User-Agent pour anonymiser tout en détectant les doublons
$ipHash = hash('sha256', $_SERVER['REMOTE_ADDR'] . date('Y-m-d'));
$uaHash = hash('sha256', $_SERVER['HTTP_USER_AGENT'] ?? '');

// Construire la ligne CSV
$date = gmdate('Y-m-d H:i:s');
$line = sprintf(
    "%s,%s,%s,%s\n",
    $date,
    $slug,
    $ipHash,
    $uaHash
);

// Écriture avec verrouillage pour éviter les corruptions en cas d'accès simultané
file_put_contents($logFile, $line, FILE_APPEND | LOCK_EX);

http_response_code(204);
