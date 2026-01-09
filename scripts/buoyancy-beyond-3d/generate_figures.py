"""
Script to generate matplotlib figures for the "Buoyancy beyond 3D" post.

This script generates all the figures used in the post.
Run this script to regenerate all figures when needed.

Usage:
    python generate_figures.py
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# Create output directory for figures
output_dir = '../../assets/images/buoyancy-beyond-3d'
os.makedirs(output_dir, exist_ok=True)

# Set style for publication-quality figures
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12

def plot_pressure_vs_depth():
    """
    Generate a plot showing pressure as a function of depth in a static fluid.
    """
    # Parameters
    P0 = 101325  # Atmospheric pressure in Pa
    rho = 1000   # Water density in kg/m^3
    g = 9.81     # Gravity in m/s^2
    
    # Depth range
    h = np.linspace(0, 20, 100)  # Depth in meters
    
    # Pressure calculation
    P = P0 + rho * g * h
    
    # Create figure
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(h, P / 1000, 'b-', linewidth=2, label='$P(h) = P_0 + \\rho g h$')
    ax.axhline(y=P0 / 1000, color='r', linestyle='--', linewidth=1.5, 
               label=f'$P_0 = {P0/1000:.1f}$ kPa')
    
    ax.set_xlabel('Depth $h$ (m)', fontsize=14)
    ax.set_ylabel('Pressure $P$ (kPa)', fontsize=14)
    ax.set_title('Pressure vs Depth in a Static Fluid', fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='best')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'pressure_vs_depth.png'), 
                bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {output_dir}/pressure_vs_depth.png")

def plot_buoyancy_force():
    """
    Generate a plot showing buoyancy force as a function of displaced volume.
    """
    # Parameters
    rho = 1000   # Water density in kg/m^3
    g = 9.81     # Gravity in m/s^2
    
    # Volume range (in cubic meters)
    V = np.linspace(0, 5, 100)
    
    # Buoyancy force calculation
    F_b = rho * g * V
    
    # Create figure
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(V, F_b / 1000, 'g-', linewidth=2, 
            label='$F_b = \\rho g V$')
    
    ax.set_xlabel('Displaced Volume $V$ (m³)', fontsize=14)
    ax.set_ylabel('Buoyancy Force $F_b$ (kN)', fontsize=14)
    ax.set_title("Archimedes' Principle: Buoyancy Force", fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='best')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'buoyancy_force.png'), 
                bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {output_dir}/buoyancy_force.png")

def plot_submerged_object_schematic():
    """
    Generate a schematic diagram showing a submerged object with pressure forces.
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Draw water surface
    ax.axhline(y=0, color='blue', linewidth=3, label='Water Surface')
    ax.fill_between([-2, 2], -3, 0, alpha=0.3, color='lightblue', label='Fluid')
    
    # Draw a simple submerged object (rectangle)
    object_x = [-0.5, 0.5, 0.5, -0.5, -0.5]
    object_y = [-1.5, -1.5, -2.5, -2.5, -1.5]
    ax.plot(object_x, object_y, 'k-', linewidth=2, label='Submerged Object')
    ax.fill(object_x[:-1], object_y[:-1], alpha=0.5, color='gray')
    
    # Draw pressure arrows (simplified)
    # Top of object
    ax.arrow(0, -1.5, 0, -0.3, head_width=0.1, head_length=0.1, 
             fc='red', ec='red', linewidth=2, label='Pressure Force')
    # Bottom of object
    ax.arrow(0, -2.5, 0, 0.3, head_width=0.1, head_length=0.1, 
             fc='red', ec='red', linewidth=2)
    
    # Draw buoyancy force arrow (upward)
    ax.arrow(0.7, -2, 0, 0.5, head_width=0.15, head_length=0.15, 
             fc='green', ec='green', linewidth=3, label='Buoyancy Force $\\vec{F}_b$')
    
    # Add labels
    ax.text(0.8, -1.3, '$P_1$', fontsize=12, color='red')
    ax.text(0.8, -2.7, '$P_2$', fontsize=12, color='red')
    ax.text(1.2, -1.5, '$\\vec{F}_b$', fontsize=14, color='green', fontweight='bold')
    
    ax.set_xlim(-2, 2)
    ax.set_ylim(-3, 0.5)
    ax.set_xlabel('Horizontal Position', fontsize=14)
    ax.set_ylabel('Depth (m)', fontsize=14)
    ax.set_title('Submerged Object with Pressure Forces', fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right')
    ax.set_aspect('equal')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'submerged_object_schematic.png'), 
                bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {output_dir}/submerged_object_schematic.png")

if __name__ == '__main__':
    print("Generating figures for 'Buoyancy beyond 3D' post...")
    print(f"Output directory: {output_dir}\n")
    
    plot_pressure_vs_depth()
    plot_buoyancy_force()
    plot_submerged_object_schematic()
    
    print("\nAll figures generated successfully!")
