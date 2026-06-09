<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Dashboard - InvenTrack</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

  <nav class="navbar">
    <div class="nav-brand">📦 InvenTrack</div>
    <div class="nav-links">
      <a href="/inventory">Inventory</a>
      <a href="/dashboard" class="active">Dashboard</a>
    </div>
  </nav>

  <main class="container">

    <h1 class="page-title">Dashboard Overview</h1>

    <div class="stats-grid">
      <div class="stat-card blue">
        <div class="stat-icon">📦</div>
        <div class="stat-info">
          <div class="stat-value" id="total_products">--</div>
          <div class="stat-label">Total Products</div>
        </div>
      </div>
      <div class="stat-card green">
        <div class="stat-icon">🔢</div>
        <div class="stat-info">
          <div class="stat-value" id="total_quantity">--</div>
          <div class="stat-label">Total Quantity</div>
        </div>
      </div>
      <div class="stat-card purple">
        <div class="stat-icon">💰</div>
        <div class="stat-info">
          <div class="stat-value" id="total_value">--</div>
          <div class="stat-label">Inventory Value</div>
        </div>
      </div>
      <div class="stat-card red">
        <div class="stat-icon">⚠️</div>
        <div class="stat-info">
          <div class="stat-value" id="low_stock">--</div>
          <div class="stat-label">Low Stock Items</div>
        </div>
      </div>
    </div>

    <div class="card center-card">
      <p>Manage your products from the inventory page.</p>
      <a href="/inventory" class="btn-primary">Go to Inventory →</a>
    </div>
