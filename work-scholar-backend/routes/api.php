<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

// Example API route for user authentication
Route::post('/login', 'AuthController@login');

// Example API route for fetching user profile
Route::get('/profile', 'UserController@show')->middleware('auth:api');

// Example API route for updating user profile
Route::put('/profile', 'UserController@update')->middleware('auth:api');

// Example API route for fetching academic units
Route::get('/units', 'UnitController@index')->middleware('auth:api');

// Example API route for fetching work history
Route::get('/work-history', 'WorkHistoryController@index')->middleware('auth:api');

// Example API route for fetching department history
Route::get('/departments', 'DepartmentController@index')->middleware('auth:api');