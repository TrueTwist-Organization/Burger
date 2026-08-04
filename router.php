<?php

declare(strict_types=1);

$uri = urldecode(parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH) ?? '/');

if ($uri !== '/' && file_exists(__DIR__ . $uri) && !is_dir(__DIR__ . $uri)) {
    return false;
}

$phpFile = __DIR__ . ($uri === '/' ? '/index.php' : $uri);
if (is_dir($phpFile)) {
    $phpFile = rtrim($phpFile, '/') . '/index.php';
} elseif (!str_ends_with($phpFile, '.php')) {
    $phpFile .= '.php';
}

if (file_exists($phpFile)) {
    require $phpFile;
    return true;
}

http_response_code(404);
echo '404 Not Found';
