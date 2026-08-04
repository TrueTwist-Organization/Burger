<?php

declare(strict_types=1);

const SITE_NAME = 'The Perfect Burger';
const SITE_ENTRY = 'index.php';

function page_url(string $page = 'index.php'): string
{
    if ($page === '' || $page === 'index' || $page === 'index.php') {
        return 'index.php';
    }

    if (!str_contains($page, '.')) {
        $page .= '.php';
    }

    return $page;
}
