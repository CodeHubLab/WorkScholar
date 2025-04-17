<?php

require_once __DIR__.'/../vendor/autoload.php';

use Illuminate\Contracts\Http\Kernel;
use Illuminate\Contracts\Console\Kernel as ConsoleKernel;
use Illuminate\Foundation\Application;

$app = new Application(
    $_ENV['APP_BASE_PATH'] ?? dirname(__DIR__)
);

// Bind the important interfaces into the container
$app->singleton(
    Http\Kernel::class,
    Http\Kernel::class
);

$app->singleton(
    ConsoleKernel::class,
    Console\Kernel::class
);

// Return the application instance
return $app;