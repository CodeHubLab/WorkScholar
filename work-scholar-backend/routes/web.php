<?php

use Illuminate\Support\Facades\Route;

// Define web routes for the application

Route::get('/', function () {
    return view('welcome');
});

// Add more routes as needed for your application
Route::get('/profile', 'ProfileController@index')->name('profile.index');
Route::get('/dashboard', 'DashboardController@index')->name('dashboard.index');